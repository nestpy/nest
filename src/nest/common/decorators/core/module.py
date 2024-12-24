from dataclasses import dataclass
from typing import Any, Type, List, Optional

@dataclass
class ModuleMetadata:
    """
    Metadata configuration for modules.
    
    Attributes:
        controllers (List[Type]): List of controllers to be registered
        providers (List[Type]): List of providers/services to be registered
        imports (List[Type]): List of other modules to import
        exports (List[Type]): List of providers to be exported
    """
    controllers: List[Type] = None
    providers: List[Type] = None
    imports: List[Type] = None
    exports: List[Type] = None

    def __post_init__(self):
        self.controllers = self.controllers or []
        self.providers = self.providers or []
        self.imports = self.imports or []
        self.exports = self.exports or []

def Module(
    *,
    controllers: List[Type] = None,
    providers: List[Type] = None,
    imports: List[Type] = None,
    exports: List[Type] = None
):
    """
    Decorator that marks a class as a module.
    Modules are used to organize the application structure.

    Args:
        controllers: List of controllers to be registered in this module
        providers: List of providers to be registered in this module
        imports: List of other modules to import
        exports: List of providers to be exported from this module

    Returns:
        Type[Any]: The decorated module class
    """
    def decorator(cls: Type[Any]) -> Type[Any]:
        metadata = ModuleMetadata(
            controllers=controllers,
            providers=providers,
            imports=imports,
            exports=exports
        )
        setattr(cls, "__module__", True)
        setattr(cls, "__metadata__", metadata)
        return cls

    return decorator