from typing import Type, Tuple, Any
from fastapi import FastAPI

from .application import Application
from .meta.generics import Generic

class NestFactory:

    @staticmethod
    @Generic(allowed_types=[Application])
    def create(
        module: Type,
        _type_generics: Tuple[Type[Any], ...] = (Application,)
    ) -> Application:

        application = _type_generics[0]

        app = application(FastAPI())
        app.create_module(module)
        
        return app
