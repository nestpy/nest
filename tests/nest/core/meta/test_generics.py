import pytest
from typing import Any, Tuple, Type
from src.nest.core.meta.generics import GenericWrapper, Generic

# Ejemplo de función para probar
def sample_function(param: Any, _type_generics: Tuple[Type[Any], ...] = ()) -> str:
    return f"Received: {param}"

class TestGenericWrapper:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.wrapper = GenericWrapper(sample_function, allowed_types=(int, str))

    def test_create_wrapper(self):
        assert isinstance(self.wrapper, GenericWrapper)

    def test_getitem_with_allowed_type(self):
        wrapped_function = self.wrapper[int]  # Usando __getitem__
        result = wrapped_function(10)  # Llamando a la función envuelta
        assert result == "Received: 10"

    def test_getitem_with_disallowed_type(self):
        with pytest.raises(TypeError):
            self.wrapper[float]  # float no está permitido

    def test_call_function(self):
        result = self.wrapper(20)  # Llamando directamente a la función
        assert result == "Received: 20"

class TestGenericDecorator:
    def test_generic_decorator(self):
        @Generic(allowed_types=(int, str))
        def decorated_function(param: Any, _type_generics = ()) -> str:
            return f"Decorated: {param}"

        assert isinstance(decorated_function, GenericWrapper)

        # Probar la función decorada
        result = decorated_function(5)
        assert result == "Decorated: 5"

        with pytest.raises(TypeError):
            decorated_function[float](3.14)  # float no está permitido 