from nest.common.enums import VersioningType
from nest.common.metadata import RoutePathMetadata
from nest.core import ApplicationConfig


class RoutePathFactory:

    def __init__(self, applicationConfig: ApplicationConfig):
        self.config = applicationConfig

    # TODO: Support MultiVersion Array
    def create(self, metadata: RoutePathMetadata):
        # paths = []

        path = self.concatPaths(metadata.controllerPath, metadata.methodPath)

        if (
            self.config.versioning and
            self.config.getVersioning().type == VersioningType.URI
        ):
            key = self.config.getVersioning().key
            number = self.getVersion(metadata)

            versionPath = f'{key}{number}'
            path = self.concatPaths(versionPath, path)

        if (self.config.globalPrefix):
            globalPrefix = self.config.getGlobalPrefix().prefix
            path = self.concatPaths(globalPrefix, path)

        return path

    def concatPaths(self, firstPath: str, lastPath: str):

        firstPath = firstPath.strip('/')
        lastPath = lastPath.strip('/')

        path = f'/{firstPath}/{lastPath}'

        return self.formatPath(path)

    def formatPath(self, path):
        if path in [' ', '', '/', '//']:
            return '/'

        return path.replace('//', '/').rstrip('/')

    def getVersion(self, metadata: RoutePathMetadata):
        return metadata.methodVersion \
            or metadata.controllerVersion \
            or self.config.getVersioning().defaultVersion

    def getVersionPrefix(self):
        pass

    def isExcludedFromGlobalPrefix(self, controllerPath: str):
        options = self.config.getGlobalPrefix()
        excludedRoutes = options.exclude

        return controllerPath in excludedRoutes
