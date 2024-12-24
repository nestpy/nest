from typing import Type
from fastapi import FastAPI

from .application import Application


class NestFactory:
    @staticmethod
    def create(module: Type) -> Application:
        """
        Crea una nueva aplicación Nest
        
        Args:
            module: El módulo raíz de la aplicación
            
        Returns:
            Application: La aplicación Nest configurada
        """
        app = Application(FastAPI())
        app.create_module(module)
        
        return app

    @staticmethod
    async def create_microservice(module: Type, options: dict = None):
        """
        Crea un nuevo microservicio
        (Lo implementaremos más adelante)
        """
        pass

    @staticmethod
    async def create_application_context(module: Type):
        """
        Crea un contexto de aplicación independiente
        (Lo implementaremos más adelante)
        """
        pass 