from typing import Type, Tuple, Any, Optional
from fastapi import FastAPI
from .application import Application
from .meta.generics import Generic

class NestFactory:

    @staticmethod
    def create(module: Type) -> Application:

        app = Application(FastAPI())
        app.create_module(module)
        
        return app

    @staticmethod
    @Generic(allowed_types=[Application])
    def create_v2(
        module: Type,
        http_adapter: AbstractHttpAdapter,
        options: Optional[Any] = None,
        _type_generics: Tuple[Type[Any], ...] = (NestApplication,)
    ) -> NestApplication:

        application = _type_generics[0]


        config = ApplicationConfig()
        container = NestContainer()

        app = application(
            container,
            http_adapter,
            config,
            options
        )
        
        return app

    
