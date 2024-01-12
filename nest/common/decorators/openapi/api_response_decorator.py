from typing import Any, Callable, Dict
from nest.common.keys import OPENAPI_RESPONSE_KEY


def ApiResponse(response: Dict[int, Any]):
    def decorator(fn: Callable):
        setattr(fn, OPENAPI_RESPONSE_KEY, response)

        return fn

    return decorator
