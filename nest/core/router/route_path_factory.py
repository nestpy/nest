from nest.common import VersioningType
from nest.common.metadata import RoutePathMetadata
from nest.core import ApplicationConfig


class RoutePathFactory:

    def __init__(self, applicationConfig: ApplicationConfig):
        self.config = applicationConfig

    # TODO: Support MultiVersion Array
    def create(self, metadata: RoutePathMetadata):
        # paths = []

        path = f'{metadata.controllerPath}{metadata.methodPath}'

        if (self.config.globalPrefix):
            path = f'{metadata.globalPrefix}{path}'

        if (self.config.versioning.type == VersioningType.URI):
            versionPath = self.getVersion(metadata)
            path = f'{path}{versionPath}' 
        
        
        return path


    def getVersion(self, metadata: RoutePathMetadata):
        return metadata.methodVersion \
            or metadata.controllerVersion \
            or self.config.versioning.defaultVersion

    def getVersionPrefix(self):
        pass

    def isExcludedFromGlobalPrefix(self, controllerPath: str):
        options = self.config.globalPrefix
        excludedRoutes = options.exclude

        return controllerPath in excludedRoutes
