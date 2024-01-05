from kink import inject

from typing import ( Type, TypeVar )

T = TypeVar("T")

def Injectable():
    def decorator(cls: Type[T]) -> Type[T]:
        return inject(cls)
    return decorator