from nest.common.decorators import Module # Change URL for typing?
from nest.common.interfaces import INestApplication
from nest.common.metadata import GlobalPrefixOptions
from nest.core import ApplicationConfig

from fastapi import APIRouter, FastAPI

from typing import ( Any, List )


class NestApplication(INestApplication):

    def __init__(
        self, 
        appModule: Module, 
        config: ApplicationConfig = ApplicationConfig()
    ):
        self.nest = FastAPI()
        self.appModule = appModule()
        self.config = config

        self._setConfig()
        print(config.globalPrefix)


    def _setConfig(self) -> None:
        value: ApplicationConfig = ApplicationConfig()

        if type(value.globalPrefix == bool):
            value.globalPrefix = GlobalPrefixOptions(
                prefix= '/api' if value.globalPrefix else ''
            )

    def _setup(self) -> None:
        self._setupModule()
    
    def _setupModule(self) -> None:
        controllers = self.appModule.controllers

        for module in self.appModule.imports:
            controllers.extend(module().controllers)

        self._setupController(controllers)

    def _setupController(self, controllers: List[Any]) -> None:
        globalPrefix = self.config.globalPrefix.prefix
        for controller in controllers:
            router = APIRouter(
                prefix=f'{globalPrefix}{controller().prefix}',
                tags=controller().tags)
            
            for route in controller().routes:
                router.add_api_route(
                    endpoint=route.endpoint, 
                    **route.dict(exclude={'endpoint'})
                )

            self.nest.include_router(router)
    
    def listen(self, host: str = '0.0.0.0', port: int = 3000) -> None:
        import uvicorn
        
        self._setup()
        uvicorn.run(self.nest, host=host, port=port)

    def setGlobalPrefix(self, prefix: str, exclude: List[str] = []) -> None:
        self.config.globalPrefix = GlobalPrefixOptions(
            prefix=prefix,
            exclude=exclude
        )