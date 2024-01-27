from nest.common.keys import ROUTE_HTTP_CODE_KEY
from nest.common.enums import HttpStatus
from typing import Callable


# TODO: Compatible with HttpStatus enum
# TODO: Compatible with String Value
def HttpCode(status: int):
    is_http_code = any(status == item.value for item in HttpStatus)
    if not is_http_code:
        raise ValueError(
            f"Value {status} is not a part of {HttpStatus.__name__}"
        )

    def decorator(fn: Callable):
        setattr(fn, ROUTE_HTTP_CODE_KEY, status)
        return fn

    return decorator
