from nest.core import NestFactory
from nest.core.application import Application
from nest.common import VersioningType

from app_module import AppModule

def bootstrap():
    app = NestFactory.create(AppModule)

    app.set_global_prefix('/api')

    app.enable_versioning(
        type=VersioningType.URI,
        default_version="1",
        prefix="v"
    )

    app.listen(3000)

if __name__ == "__main__":
    bootstrap()