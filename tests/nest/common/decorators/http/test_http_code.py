from http import HTTPStatus
from src.nest.common.decorators.http.http_code import HttpCode

def test_http_code_decorator_with_int():
    """
    Test that verifies the HttpCode decorator works with integer status codes.
    
    It checks:
    - The __http_code__ attribute is set correctly
    - The decorated function maintains its original functionality
    """
    @HttpCode(201)
    def test_function():
        return "test"

    assert hasattr(test_function, "__http_code__")
    assert test_function.__http_code__ == 201
    assert test_function() == "test"

def test_http_code_decorator_with_http_status():
    """
    Test that verifies the HttpCode decorator works with HTTPStatus enum values.
    
    It checks:
    - The __http_code__ attribute is set correctly with the numeric value
    - The decorated function maintains its original functionality
    """
    @HttpCode(HTTPStatus.CREATED)
    def test_function():
        return "test"

    assert hasattr(test_function, "__http_code__")
    assert test_function.__http_code__ == 201
    assert test_function() == "test"
