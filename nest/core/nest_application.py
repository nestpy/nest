from nest.common.enums import DocsType, VersioningType
from nest.common.interfaces import INestApplication
from nest.common.metadata import (
    CorsOptions,
    DocsOptions,
    GlobalPrefixOptions,
    VersioningOptions,
)
from nest.common.utils import fix_endpoint_signature
from nest.core import ApplicationConfig
from nest.core.router import RoutePathFactory

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import Any, List


class NestApplication(INestApplication):
    def __init__(self, appModule: Any, config: ApplicationConfig):
        self.nest = FastAPI()
        self.appModule = appModule()
        # TODO: Change to private readonly
        self.config = config

    def _setup(self) -> None:
        self._setupDocs()
        self._setupCors()
        self._setupModule()

    def _setupCors(self) -> None:
        cors = self.config.getCors()

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
        docs = self.config.getDocs()

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
        PathFactory = RoutePathFactory(self.config)

        for controller in controllers:
            router = APIRouter(
                prefix='',
                tags=controller().tags
            )

            for route in controller().routes:
                fix_endpoint_signature(
                    controller, route.endpoint
                )

                router.add_api_route(
                    path=PathFactory.create(route.path_metadata),
                    endpoint=route.endpoint,
                    **route.dict(exclude={
                        "endpoint",
                        "path",
                        "path_metadata"
                    }),
                )

            self.nest.include_router(router)

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
        defaultVersion: str = "1"
    ) -> None:
        self.config.versioning = VersioningOptions(
            type=type, defaultVersion=defaultVersion
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
