from nest.core import NestFactory
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

    app.listen(port=3000, host="0.0.0.0")

if __name__ == "__main__":
    bootstrap()