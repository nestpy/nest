from typing import Type, TypeVar, Callable, Any, Tuple, Optional
from functools import wraps

T = TypeVar('T')
U = TypeVar('U')


class GenericWrapper:
    def __init__(self, func: Callable[..., Any], allowed_types: Optional[Tuple[Type, ...]] = None):
        """
        Initializes the GenericWrapper.

        :param func: The function or class to wrap.
        :param allowed_types: A tuple of types that are allowed as type parameters.
        """
        self.func = func
        self.allowed_types = allowed_types

        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        """
        Makes the wrapper directly callable without type parameters.
        Uses the first allowed type as default if allowed_types is specified.
        """
        return self.func(*args, **kwargs)

    def __getitem__(self, type_generics: Type[Any]) -> Callable[..., Any]:
        """
        Allows the use of square brackets to specify type parameters.

        :param type_generics: The type or tuple of types to use as type parameters.
        :return: A callable that wraps the original function/class with type enforcement.
        """
        # Ensure type_generics is a tuple
        if not isinstance(type_generics, tuple):
            type_generics = (type_generics,)

        # Enforce type constraints if allowed_types are specified
        if self.allowed_types:
            for tp in type_generics:
                if tp not in self.allowed_types:
                    raise TypeError(f"Type {tp.__name__} is not allowed. Allowed types: {[t.__name__ for t in self.allowed_types]}")

        def wrapper(*args, **kwargs):
            kwargs['_type_generics'] = type_generics
            return self.func(*args, **kwargs)

        return wrapper


def Generic(allowed_types: Optional[Tuple[Type, ...]] = None):
    """
    Decorator to make a function or class generic with type constraints.

    :param allowed_types: A tuple of types that are allowed as type parameters.
    """
    def decorator(func: Callable[..., Any]) -> GenericWrapper:
        return GenericWrapper(func, allowed_types)
    return decorator