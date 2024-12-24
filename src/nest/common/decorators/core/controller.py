from typing import Any, Type, Optional

def Controller(prefix: str = "", version: Optional[str] = None):
    """
    Decorator that marks a class as a controller.
    Controllers are responsible for handling incoming requests and returning responses.

    Args:
        prefix (str): The route prefix for all endpoints in the controller
        version (Optional[str]): API version for the controller

    Returns:
        Type[Any]: The decorated controller class
    """
    def decorator(cls: Type[Any]) -> Type[Any]:
        setattr(cls, "__controller__", True)
        setattr(cls, "__prefix__", prefix)
        setattr(cls, "__version__", version)
        
        return cls
    return decorator