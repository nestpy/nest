from src.nest.common.decorators.core.controller import Controller

def test_controller_decorator():
    """
    Test that verifies the Controller decorator properly sets metadata on the class.
    
    It checks:
    - The __controller__ attribute is set to True
    - The prefix is correctly set
    - The version is correctly set
    """
    @Controller(prefix="/api", version="1")
    class TestController:
        pass

    assert hasattr(TestController, "__controller__")
    assert TestController.__controller__ is True
    assert TestController.__prefix__ == "/api"
    assert TestController.__version__ == "1"

def test_controller_decorator_default_values():
    """
    Test that verifies the Controller decorator uses correct default values.
    
    It checks:
    - The __controller__ attribute is set to True
    - Empty string is used as default prefix
    - None is used as default version
    """
    @Controller()
    class TestController:
        pass

    assert hasattr(TestController, "__controller__")
    assert TestController.__controller__ is True
    assert TestController.__prefix__ == ""
    assert TestController.__version__ is None