from typing import List, Optional
from nest.common.keys import (
    ROUTER_WATERMARK,
    ROUTE_HTTP_CODE_KEY,
    ROUTE_INFO_KEY,
    ROUTE_VERSION_KEY,
)
from nest.common.metadata import Route, RoutePathMetadata

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
                self.prefix = decorator.prefix
                self.version = decorator.version
                self.tags = [decorator.prefix]
                self.routes = self.set_routes()

            def set_routes(self) -> List['Route']:
                routes = []

                for attr_name in dir(ClassBasedView):
                    endpoint = getattr(ClassBasedView, attr_name)

                    if callable(endpoint) and hasattr(
                        endpoint,
                        ROUTER_WATERMARK
                    ):
                        route = getattr(endpoint, ROUTE_INFO_KEY)

                        status_code = getattr(
                            endpoint, ROUTE_HTTP_CODE_KEY, route.status_code
                        )

                        metadata = RoutePathMetadata(
                            controllerPath=self.prefix,
                            controllerVersion=self.version,
                            methodPath=route.path,
                            methodVersion=getattr(
                                endpoint,
                                ROUTE_VERSION_KEY,
                                None
                            )
                        )

                        routes.append(
                            Route(
                                path_metadata=metadata,
                                status_code=status_code,
                                endpoint=endpoint,
                                **route.dict(exclude={"status_code"})
                            )
                        )

                return routes

        IController.decorator = decorator
        return IController
