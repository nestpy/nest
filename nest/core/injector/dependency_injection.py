from typing import Any, Callable, Optional, Type, TypeVar, Union

from kink import Container
from kink import inject as kink_inject

T = TypeVar("T")
S = TypeVar("S")

ServiceDefinition = Union[Type[S], Callable]
ServiceResult = Union[S, Callable]

def factory(f: Callable[..., T]) -> Callable[[], T]:
    return lambda: f()


def instantiate(f: Callable[..., T]) -> T:
    return f()