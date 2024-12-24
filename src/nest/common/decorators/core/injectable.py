from typing import Any, Type

def Injectable():
    """
    Decorator that marks a class as injectable.
    Injectable classes can be injected as dependencies into other classes.

    Returns:
        Type[Any]: The decorated injectable class
    """
    def decorator(cls: Type[Any]) -> Type[Any]:
        setattr(cls, "__injectable__", True)
        return cls
    return decorator