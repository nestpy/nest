from typing import Dict, Type, Any
import inspect


class Container:
    def __init__(self):
        self._services: Dict[Type, Any] = {}

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
