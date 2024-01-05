from nest.core import NestApplication
from nest.common import VersioningType

from app_module import AppModule

def bootstrap():
    app = NestApplication( AppModule )

    app.setGlobalPrefix('/api')

    app.enableVersioning(type=VersioningType.URI, defaultVersioning='2')

    app.listen()

if __name__ == "__main__":
    bootstrap()
