from kink import inject

from typing import Any, Callable


def Injectable():
    def decorator(cls: Callable[..., Any]) -> Callable[..., Any]:
        return inject(cls)

    return decorator
