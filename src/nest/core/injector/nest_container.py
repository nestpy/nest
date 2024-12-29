from typing import Set, Type, Dict, Any, List
import inspect

class NestContainer:
    def __init__(self):
        self.modules: Set[Type] = set()
        self.controllers: List[Any] = []
        self._services: Dict[Type, Any] = {}

    def create_module(self, module_class: Type):
        """Registra un módulo y sus dependencias"""
        if module_class in self.modules:
            return
            
        if not hasattr(module_class, "__metadata__"):
            raise ValueError(f"{module_class.__name__} must be decorated with @Module()")

        self.modules.add(module_class)
        metadata = getattr(module_class, "__metadata__")

        if metadata.imports:
            for import_module in metadata.imports:
                self.create_module(import_module)

        if metadata.providers:
            for provider in metadata.providers:
                self.register(provider)

        if metadata.controllers:
            for controller in metadata.controllers:
                controller_instance = self._instantiate_controller(controller)
                self.controllers.append(controller_instance)

    def register(self, service_class: Type):
        if service_class != inspect._empty and not hasattr(service_class, "__injectable__"):
            raise ValueError(f"{service_class.__name__} must be decorated with @Injectable()")
        
        if service_class not in self._services:
            dependencies = {}
            
            # Solo verificar anotaciones si el constructor está definido en la clase
            if '__init__' in service_class.__dict__:
                # Obtener las dependencias del constructor
                init_params = inspect.signature(service_class.__init__).parameters
                
                # Verificar que todos los parámetros (excepto self) tengan anotaciones de tipo
                for name, param in init_params.items():
                    if name != 'self' and param.annotation == inspect._empty:
                        raise ValueError("All constructor parameters must have type annotations")
                
                # Preparar las dependencias necesarias
                for name, param in init_params.items():
                    if name != 'self':
                        dependency_class = param.annotation
                        dependencies[name] = self.get(dependency_class)
            
            # Crear instancia con sus dependencias
            instance = service_class(**dependencies)
            self._services[service_class] = instance
        
        return self._services[service_class]

    def get(self, service_class: Type):
        if service_class not in self._services:
            return self.register(service_class)
        return self._services[service_class]

    def _instantiate_controller(self, controller_class: Type):
        """Crea una instancia del controlador con sus dependencias"""
        init_params = inspect.signature(controller_class.__init__).parameters
        dependencies = {}

        for name, param in init_params.items():
            if name != 'self' and param.annotation != inspect._empty:
                service_class = param.annotation
                dependencies[name] = self.get(service_class)

        return controller_class(**dependencies)