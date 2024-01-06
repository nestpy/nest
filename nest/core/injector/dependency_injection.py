from typing import Callable, Type, TypeVar, Union

T = TypeVar("T")
S = TypeVar("S")

ServiceDefinition = Union[Type[S], Callable]
ServiceResult = Union[S, Callable]


def factory(f: Callable[..., T]) -> Callable[[], T]:
    return lambda: f()


def instantiate(f: Callable[..., T]) -> T:
    return f()
