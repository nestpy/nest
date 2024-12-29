from abc import ABC, abstractmethod
from typing import List, Type

import inspect
from inspect import ismethod, isclass

from fastapi import FastAPI
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .http_adapter import HttpAdapter

from nest.core.schema import CorsOptions
from nest.core.schema import ServerOptions
from nest.common import VersioningOptions

class FastApiAdapter(HttpAdapter):

    def __init__(self):
        self.app = FastAPI()

    def enable_cors(self, **options: CorsOptions) -> None:
        from fastapi.middleware.cors import CORSMiddleware

        self.app.add_middleware(CORSMiddleware, **options)

    def listen(self, **options: ServerOptions) -> None:
        import uvicorn
        
        uvicorn.run(self.app, **options)

    def register_routes(self, controllers: List[Type], global_prefix: str, versioning_options: VersioningOptions):
        """Registra todas las rutas almacenadas con el prefijo global y la versión."""
        for controller in controllers:
            controller_prefix = getattr(controller.__class__, "__prefix__", "")
            controller_version = getattr(controller.__class__, "__version__", None)
            version_prefix = ""

            for method_name, method in inspect.getmembers(controller, inspect.ismethod):
                if hasattr(method, "__route__"):
                    route_path = getattr(method, "__path__", "")
                    http_method = getattr(method, "__method__", "").lower()
                    status_code = getattr(method, "__http_code__", None)
                    
                    if versioning_options is not None:
                        version_route = getattr(method, "__version__", None)
                        
                        if version_route is not None:
                            version_prefix = version_route
                        elif controller_version is not None:
                            version_prefix = controller_version
                        else:
                            version_prefix = versioning_options["default_version"]

                        version_prefix = f"/{versioning_options['prefix']}{version_prefix}"

                    full_path = self._normalize_path(
                        global_prefix,
                        version_prefix,
                        controller_prefix,
                        route_path
                    )

                    endpoint = getattr(self.app, http_method)
                    route = endpoint(full_path)(self._create_route_handler(method, status_code))
        
    def _normalize_path(self, *paths: str) -> str:
        """
        Normaliza y combina paths asegurando que tengan el formato correcto.
        """
        # Filtrar paths vacíos
        valid_paths = [p for p in paths if p]
        
        # Combinar paths y asegurar formato correcto
        result = '/'.join(p.strip('/') for p in valid_paths)
        
        # Asegurar que empiece con / y no termine con /
        return f"/{result}".rstrip('/')

    def _instantiate_controller(self, controller_class: Type):
        """Crea una instancia del controlador con sus dependencias"""
        init_params = inspect.signature(controller_class.__init__).parameters
        dependencies = {}

        for name, param in init_params.items():
            if name != 'self' and param.annotation != inspect._empty:
                service_class = param.annotation
                dependencies[name] = self.container.get(service_class)

        return controller_class(**dependencies)

    def _create_route_handler(self, route_handler, status_code=None):
        """Crea un manejador de ruta con código de estado personalizado"""
        async def handler(*args, **kwargs):
            response = await route_handler(*args, **kwargs)
            if isinstance(response, Response):
                return response
            return JSONResponse(
                content=jsonable_encoder(response),
                status_code=status_code or 200
            )
        handler.__signature__ = inspect.signature(route_handler)
        return handler
