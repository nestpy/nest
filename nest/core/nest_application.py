from fastapi import FastAPI

from nest.common.interfaces import INestApplication
from nest.common.decorators import Module # Change URL for typing?

class NestApplication(INestApplication):

    def __init__(self, appModule: Module):
        self.nest = FastAPI()
        self.appModule = appModule()

    def _setup(self) -> None:
        self._setupModule()
    
    def _setupModule(self) -> None:
        print(self.appModule)
    
    def listen(self, host: str = '0.0.0.0', port: int = 3000) -> None:
        import uvicorn
        
        self._setup()
        uvicorn.run(self.nest, host=host, port=port)