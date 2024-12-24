from functools import wraps

def Version(version: str):
    """
    Decorator to specify the API version for a route or controller.
    
    Example:
        @Version("1")
        @Controller("/users")
        class UserController:
            pass

    Args:
        version (str): The version identifier

    Returns:
        callable: The decorated function or class
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        setattr(wrapper, "__version__", version)
        return wrapper
    return decorator