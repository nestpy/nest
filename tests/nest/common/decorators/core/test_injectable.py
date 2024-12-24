from src.nest.common.decorators.core.injectable import Injectable

def test_injectable_decorator():
    """
    Test that verifies the Injectable decorator properly marks a class as injectable.
    
    It checks:
    - The __injectable__ attribute is set to True
    """
    @Injectable()
    class TestService:
        pass

    assert hasattr(TestService, "__injectable__")
    assert TestService.__injectable__ is True