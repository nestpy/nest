from typing import Union
from functools import wraps
from http import HTTPStatus

def HttpCode(status_code: Union[int, HTTPStatus]):
    """
    Decorator to specify the HTTP status code for a route handler.

    Args:
        status_code (Union[int, HTTPStatus]): The HTTP status code to return

    Returns:
        callable: The decorated route handler
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        code = status_code.value if isinstance(status_code, HTTPStatus) else status_code
        setattr(wrapper, "__http_code__", code)
        return wrapper
    return decorator 