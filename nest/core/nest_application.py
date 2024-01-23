from nest.common.enums import DocsType, VersioningType
from nest.common.interfaces import INestApplication
from nest.common.metadata import (
    CorsOptions,
    DocsOptions,
    GlobalPrefixOptions,
    VersioningOptions,
)
from nest.core import ApplicationConfig

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import Any, List


class NestApplication(INestApplication):
    def __init__(self, appModule: Any, config: ApplicationConfig):
        self.nest = FastAPI()
        self.appModule = appModule()
        self.config = config  # TODO: Change to private readonly

        self._setConfig()
        

    def _setConfig(self) -> None:
        cors = self.config.cors
        docs = self.config.docs
        globalPrefix = self.config.globalPrefix
        versioning = self.config.versioning

        if type(cors == bool) and cors:
            self.config.cors = CorsOptions()

        if type(docs == bool) and docs:
            self.config.docs = DocsOptions(type=DocsType.SWAGGER)

        if type(globalPrefix == bool) and globalPrefix:
            self.config.globalPrefix = GlobalPrefixOptions(
                prefix="/api"
            )

        if type(versioning == bool) and versioning:
            self.config.versioning = VersioningOptions(
                type=VersioningType.URI
            )

    def _setup(self) -> None:
        self._setupDocs()
        self._setupCors()
        self._setupModule()

    def _setupCors(self) -> None:
        cors = self.config.cors

        if not cors:
            return

        if not isinstance(cors, CorsOptions):
            return

        self.nest.add_middleware(
            CORSMiddleware,
            allow_credentials=cors.credentials,
            expose_headers=cors.exposedHeaders,
            allow_headers=cors.allowedHeaders,
            allow_origins=cors.origins,
            allow_methods=cors.methods,
            max_age=cors.maxAge,
        )

    def _setupDocs(self) -> None:
        docs = self.config.docs

        if not docs:
            self.nest = FastAPI(docs_url=None, redoc_url=None)
            return

        if not isinstance(docs, DocsOptions):
            return

        docs_url = docs.swagger_url if docs.type == DocsType.SWAGGER else None
        redoc_url = docs.redoc_url if docs.type == DocsType.REDOC else None

        self.nest = FastAPI(
            docs_url=docs_url,
            redoc_url=redoc_url,
            title=docs.title,
            description=docs.description,
            summary=docs.summary,
            version=docs.version,
            terms_of_service=docs.terms_of_service,
            contact=docs.contact,
            license_info=docs.license_info,
            openapi_tags=docs.openapi_tags,
            openapi_url=docs.openapi_url,
        )

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
                    controller, route.endpoint
                )

                router.add_api_route(
                    path=self._generatePrefix(
                        f"{controller().prefix}{route.path}", route.version
                    ),
                    endpoint=route.endpoint,
                    **route.dict(exclude={"endpoint", "path", "version"}),
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

    def enableCors(self, options: CorsOptions) -> None:
        self.config.cors = options

    def enableDocs(
        self,
        type: DocsType,
        options: DocsOptions = DocsOptions()
    ) -> None:
        self.config.docs = options.copy(update={"type": type})

    def enableVersioning(
        self,
        type: VersioningType,
        defaultVersioning: str = "1"
    ) -> None:
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
