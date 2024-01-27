from typing import Any, Callable, List, Type

from nest.core.injector.dependency_injection import factory

from inspect import Parameter, signature
from fastapi.params import Depends


def fix_endpoint_signature(
    cls: Type[Any], endpoint: Callable[..., Any]
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
        parameter.replace(
            kind=Parameter.KEYWORD_ONLY
        )
        for parameter in old_parameters[1:]
    ]

    new_signature = old_signature.replace(
        parameters=new_parameters
    )

    setattr(endpoint, "__signature__", new_signature)
