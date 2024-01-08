from nest.common.enums import VersioningType
from nest.common.interfaces import INestApplication
from nest.common.metadata import GlobalPrefixOptions, VersioningOptions
from nest.core import ApplicationConfig

from fastapi import APIRouter, FastAPI

from typing import Any, List


class NestApplication(INestApplication):
    def __init__(
        self,
        appModule: Any,
        config: ApplicationConfig
    ):
        self.nest = FastAPI()
        self.appModule = appModule()
        self.config = config # TODO: Change to private readonly

        self._setConfig()

    def _setConfig(self) -> None:
        globalPrefix = self.config.globalPrefix
        versioning = self.config.versioning

        if type(globalPrefix == bool):
            globalPrefix = GlobalPrefixOptions(
                prefix="/api" if globalPrefix else ""
            )

        if type(versioning == bool):
            versioning = VersioningOptions(
                type=VersioningType.URI if versioning else VersioningType.NONE
            )

    def _setup(self) -> None:
        self._setupModule()

    def _setupModule(self) -> None:
        controllers = self.appModule.controllers

        for module in self.appModule.imports:
            controllers.extend(module().controllers)

        self._setupController(controllers)

    def _setupController(self, controllers: List[Any]) -> None:
        if not isinstance(self.config.globalPrefix, GlobalPrefixOptions):
            raise ValueError("TODO")

        globalPrefix = self.config.globalPrefix.prefix

        for controller in controllers:
            router = APIRouter(
                prefix=f"{globalPrefix}",
                tags=controller().tags
            )

            for route in controller().routes:
                controller()._fix_endpoint_signature(
                    controller,
                    route.endpoint
                )

                router.add_api_route(
                    path=self._generatePrefix(
                        f"{controller().prefix}{route.path}",
                        route.version
                    ),
                    endpoint=route.endpoint,
                    **route.dict(exclude={
                        "endpoint", 
                        "path", 
                        "version"
                    }),
                )

            self.nest.include_router(router)

    def _generatePrefix(self, path: str, version: str):
        if not isinstance(self.config.versioning, VersioningOptions):
            raise ValueError("TODO")

        versioning = self.config.versioning

        if versioning.type == VersioningType.URI:
            default = versioning.defaultVersioning
            version = default if version is None else version
            return f"/v{version}{path}"

        return f"{path}"

    def enableVersioning(
        self,
        type: VersioningType,
        defaultVersioning: str = "1"
    ):
        self.config.versioning = VersioningOptions(
            type=type, defaultVersioning=defaultVersioning
        )

    def listen(self, host: str = "0.0.0.0", port: int = 3000) -> None:
        import uvicorn

        self._setup()
        uvicorn.run(self.nest, host=host, port=port)

    def setGlobalPrefix(self, prefix: str, exclude: List[str] = []) -> None:
        self.config.globalPrefix = GlobalPrefixOptions(
            prefix=prefix,
            exclude=exclude
        )
