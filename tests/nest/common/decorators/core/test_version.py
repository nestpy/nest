from src.nest.common.decorators.core.version import Version

def test_version_decorator():
    """
    Test that verifies the Version decorator properly sets version metadata.
    
    It checks:
    - The __version__ attribute is set correctly
    - The decorated function maintains its original functionality
    """
    @Version("1")
    def test_function():
        return "test"

    assert hasattr(test_function, "__version__")
    assert test_function.__version__ == "1"
    assert test_function() == "test"  # Ensure the function still works