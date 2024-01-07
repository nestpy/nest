from typing import Any, Callable, List, Optional, Type
from nest.common.keys import IS_ROUTE_KEY, ROUTE_HTTP_CODE_KEY, ROUTE_INFO_KEY, ROUTE_VERSION_KEY
from nest.common.metadata import Route
from nest.core.injector.dependency_injection import factory

from inspect import Parameter, signature
from fastapi.params import Depends

from kink import inject


class Controller:
    def __init__(
            self,
            prefix: str = "/",
            version: Optional[str] = None
        ) -> None:
        self.prefix = prefix
        self.version = version

    def __call__(decorator, ClassBasedView):

        wrapper = inject()
        cls = wrapper(ClassBasedView)

        class IController(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.prefix = self.set_prefix(decorator.prefix)
                self.tags = self.set_tag(decorator.prefix)
                self.routes = self.set_routes()

            def set_prefix(self, value: str) -> str:
                if not value.startswith("/"):
                    value = f"/{value}"

                if value.endswith("/"):
                    value = value[:-1]

                return value

            def set_routes(self) -> List[Route]:
                routes = []

                for attr_name in dir(ClassBasedView):
                    endpoint = getattr(ClassBasedView, attr_name)

                    if callable(endpoint) and hasattr(endpoint, IS_ROUTE_KEY):
                        route = getattr(endpoint, ROUTE_INFO_KEY)

                        status_code = getattr(
                            endpoint, ROUTE_HTTP_CODE_KEY, route.status_code
                        )

                        version = getattr(endpoint, ROUTE_VERSION_KEY, decorator.version)

                        routes.append(
                            route.copy(
                                update={
                                    "endpoint": endpoint,
                                    "status_code": status_code,
                                    "version": version,
                                }
                            )
                        )

                return routes

            def set_tag(self, value: str) -> Optional[List[str]]:
                if value.__eq__("/"):
                    return ["/"]

                return [self.set_prefix(value)]

            def _fix_endpoint_signature(
                self, cls: Type[Any], endpoint: Callable[..., Any]
            ) -> None:
                old_signature = signature(endpoint)
                old_parameters: List[Parameter] = list(
                    old_signature.parameters.values()
                )
                old_first_parameter = old_parameters[0]

                new_self_parameter = old_first_parameter.replace(
                    default=Depends(factory(cls))
                )
                new_parameters = [new_self_parameter] + [
                    parameter.replace(kind=Parameter.KEYWORD_ONLY)
                    for parameter in old_parameters[1:]
                ]

                new_signature = old_signature.replace(
                    parameters=new_parameters
                )

                setattr(endpoint, "__signature__", new_signature)

        IController.decorator = decorator
        return IController
