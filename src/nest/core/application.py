from typing import Type, Any, Optional, List, Union

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import uvicorn
import inspect
import logging

from .container import Container
from ..common.interfaces.version_options import VersioningOptions, URIVersioningOptions


class Application:
    def __init__(self, app: Optional[FastAPI] = None):
        self.logger = logging.getLogger(__name__)
        self.app = app or FastAPI()
        self.container = Container()
        self.modules = set()
        self.controllers: List[Any] = []
        self.global_prefix = ""
        self.versioning_options = None
        self._server = None

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
                self.container.register(provider)

        if metadata.controllers:
            for controller in metadata.controllers:
                self.controllers.append(controller)

    def set_global_prefix(self, prefix: str):
        """
        Establece un prefijo global para todas las rutas
        """
        self.global_prefix = ('/' + prefix.lstrip('/')).rstrip('/')
        return self
    
    def enable_versioning(self, **options: VersioningOptions):
        """
        Habilita la versión de las rutas
        """
        self.versioning_options = options

    def listen(self, port: int = 3000, host: str = "0.0.0.0"):
        """Inicia el servidor HTTP"""
        # Registrar todas las rutas antes de iniciar el servidor
        self._register_routes()
        
        uvicorn.run(
            self.app,
            host=host,
            port=port
        )
    
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

    def _register_routes(self):
        """Registra todas las rutas almacenadas con el prefijo global y la versión."""
        for controller_class in self.controllers:
            controller = self._instantiate_controller(controller_class)
            controller_prefix = getattr(controller.__class__, "__prefix__", "")
            controller_version = getattr(controller.__class__, "__version__", None)
            version_prefix = ""

            for method_name, method in inspect.getmembers(controller, inspect.ismethod):
                if hasattr(method, "__route__"):
                    route_path = getattr(method, "__path__", "")
                    http_method = getattr(method, "__method__", "").lower()
                    status_code = getattr(method, "__http_code__", None)
                    
                    if self.versioning_options is not None:
                        version_route = getattr(method, "__version__", None)
                        
                        if version_route is not None:
                            version_prefix = version_route
                        elif controller_version is not None:
                            version_prefix = controller_version
                        else:
                            version_prefix = self.versioning_options["default_version"]

                        version_prefix = f"/{self.versioning_options['prefix']}{version_prefix}"

                    full_path = self._normalize_path(
                        self.global_prefix,
                        version_prefix,
                        controller_prefix,
                        route_path
                    )

                    endpoint = getattr(self.app, http_method)
                    route = endpoint(full_path)(self._create_route_handler(method, status_code))

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

    async def init(self):
        """
        Inicializa la aplicación
        """
        pass

    async def close(self):
        """
        Limpia recursos cuando la aplicación se cierra
        """
        if self._server:
            await self._server.shutdown()

    def get_http_adapter(self):
        """
        Retorna el adaptador HTTP (FastAPI en este caso)
        """
        return self.app

