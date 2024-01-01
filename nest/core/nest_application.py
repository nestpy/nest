from fastapi import FastAPI

from nest.common.interfaces import INestApplication


class NestApplication(INestApplication):

    def __init__(self):
        self.nest = FastAPI()
    
    def listen(self, host: str = '0.0.0.0', port: int = 3000) -> None:
        import uvicorn

        uvicorn.run(self.nest, host=host, port=port)