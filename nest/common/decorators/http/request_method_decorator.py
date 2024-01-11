from nest.common.keys import IS_ROUTE_KEY, ROUTE_INFO_KEY
from nest.common.metadata import Route
from typing import Callable


def Delete(path: str = "/", **kwargs):
    return _http_verb(path, "DELETE", **kwargs)


def Get(path: str = "/", **kwargs):
    return _http_verb(path, "GET", **kwargs)


def Head(path: str = "/", **kwargs):
    return _http_verb(path, "HEAD", **kwargs)


def Options(path: str = "/", **kwargs):
    return _http_verb(path, "OPTIONS", **kwargs)


def Path(path: str = "/", **kwargs):
    return _http_verb(path, "PATH", **kwargs)


def Post(path: str = "/", **kwargs):
    return _http_verb(path, "POST", 201, **kwargs)


def Put(path: str = "/", **kwargs):
    return _http_verb(path, "PUT", **kwargs)


def _http_verb(path: str, method: str, status_code: int = 200, **kwargs):
    def decorator(fn: Callable):
        route_info = Route(
            path=path, methods=[method], status_code=status_code, **kwargs
        )

        setattr(fn, IS_ROUTE_KEY, True)
        setattr(fn, ROUTE_INFO_KEY, route_info)

        return fn

    return decorator
