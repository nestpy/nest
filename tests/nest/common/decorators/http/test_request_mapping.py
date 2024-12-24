from src.nest.common.decorators.http.request_mapping import Get, Post, Put, Delete, Patch

def test_get_decorator():
    """
    Test that verifies the GET route decorator works correctly.
    
    It checks:
    - The __route__ attribute is set to True
    - The path is set correctly
    - The HTTP method is set to GET
    - The decorated function maintains its original functionality
    """
    @Get("/test")
    def test_function():
        return "test"

    assert hasattr(test_function, "__route__")
    assert test_function.__route__ is True
    assert test_function.__path__ == "/test"
    assert test_function.__method__ == "GET"
    assert test_function() == "test"

def test_post_decorator():
    @Post("/test")
    def test_function():
        return "test"

    assert test_function.__method__ == "POST"

def test_put_decorator():
    @Put("/test")
    def test_function():
        return "test"

    assert test_function.__method__ == "PUT"

def test_delete_decorator():
    @Delete("/test")
    def test_function():
        return "test"

    assert test_function.__method__ == "DELETE"

def test_patch_decorator():
    @Patch("/test")
    def test_function():
        return "test"

    assert test_function.__method__ == "PATCH"

def test_route_decorator_default_path():
    @Get()
    def test_function():
        return "test"

    assert test_function.__path__ == ""
