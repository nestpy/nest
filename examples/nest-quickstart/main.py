from nest.core import NestFactory
from nest.common import VersioningType

from app_module import AppModule

from nest.common.metadata import CorsOptions

def bootstrap():
    app = NestFactory.create(AppModule)

    app.setGlobalPrefix("/api")

    app.enableVersioning(type=VersioningType.URI, defaultVersioning="2")

    app.enableCors( 
        CorsOptions(
            credentials=True,
            origins=['http://localhost:3000'],
            allow_methods=['GET']
        ) 
    )

    app.listen()


if __name__ == "__main__":
    bootstrap()
