from nest.core.nest_application import NestApplication
from nest.common.enums import VersioningType

from app_module import AppModule

def bootstrap():
    app = NestApplication( AppModule )

    app.setGlobalPrefix('/api')

    app.enableVersioning(type=VersioningType.URI, defaultVersioning='2')

    app.listen()

if __name__ == "__main__":
    bootstrap()