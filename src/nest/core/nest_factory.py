from typing import Type, Tuple, Any, Optional
from fastapi import FastAPI

from .nest_application import NestApplication
from .application_config import ApplicationConfig

from nest.core.meta import Generic
from nest.core.schema import ApplicationOptions
from nest.core.adapters import HttpAdapter, FastApiAdapter
from nest.core.injector import NestContainer

class NestFactory:

    @staticmethod
    @Generic(allowed_types=[NestApplication])
    def create(
        module: Type,
        http_adapter: Optional[HttpAdapter] = FastApiAdapter(),
        options: Optional[ApplicationOptions] = ApplicationOptions(),
        _type_generics: Tuple[Type[Any], ...] = (NestApplication,)
    ) -> NestApplication:

        application = _type_generics[0]

        """
        If _type_generics is empty, we are creating a FastApi application.

        Depends on the type of application, we will create a different HttpAdapter.

        If http_adapter is empty, we will create a HttpAdapter.
        Verify if the http_adapter is same as the application type.

        Mix the options with the http_adapter.

        If options is empty, we will create a ApplicationOptions.
        """
        if http_adapter is None:
            http_adapter = FastApiAdapter()
        
        config = ApplicationConfig()
        container = NestContainer()

        container.create_module(module)

        app = application(
            container,
            config,
            http_adapter,
            options
        )

        return app


    def initialize(
        cls,
        module: Type,
        container: NestContainer,
        config: ApplicationConfig,
        http_adapter: Optional[Any],
        options: Optional[ApplicationOptions],
    ):
        pass
        
