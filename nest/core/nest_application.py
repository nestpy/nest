from typing import ( Any, List )

from fastapi import APIRouter, FastAPI

from nest.common.interfaces import INestApplication
from nest.common.decorators import Module # Change URL for typing?
from nest.core import ApplicationConfig

class NestApplication(INestApplication):

    def __init__(
        self, 
        appModule: Module, 
        config: ApplicationConfig = ApplicationConfig()
    ):
        self.nest = FastAPI()
        self.appModule = appModule()
        self.config = config


    def _setup(self) -> None:
        self._setupModule()
    
    def _setupModule(self) -> None:
        controllers = self.appModule.controllers

        for module in self.appModule.imports:
            controllers.extend(module().controllers)

        self._setupController(controllers)

    def _setupController(self, controllers: List[Any]) -> None:
        for controller in controllers:
            router = APIRouter(
                prefix=f'{controller().prefix}',
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