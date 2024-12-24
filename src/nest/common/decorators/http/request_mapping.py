from typing import Any, Type
from functools import wraps

def create_route_decorator(method: str):
    """
    Factory function to create HTTP method decorators.

    Args:
        method (str): HTTP method (GET, POST, etc.)

    Returns:
        callable: A decorator for the specified HTTP method
    """
    def decorator(path: str = ""):
        def inner(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            setattr(wrapper, "__route__", True)
            setattr(wrapper, "__path__", path)
            setattr(wrapper, "__method__", method)
            return wrapper
        return inner
    return decorator


# HTTP method decorators
Get = create_route_decorator("GET")
Post = create_route_decorator("POST")
Put = create_route_decorator("PUT")
Delete = create_route_decorator("DELETE")
Patch = create_route_decorator("PATCH")