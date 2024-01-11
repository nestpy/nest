from nest.common.keys import ROUTE_VERSION_KEY
from typing import Callable


def Version(version: str):
    def decorator(fn: Callable):
        setattr(fn, ROUTE_VERSION_KEY, version)
        return fn

    return decorator
