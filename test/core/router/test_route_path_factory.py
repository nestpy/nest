from nest.common.metadata import RoutePathMetadata, VersioningOptions
from nest.core import ApplicationConfig
from nest.core.router import RoutePathFactory

import pytest

class TestRoutePathFactory:


    @pytest.mark.parametrize('config,metadata,expect', [
        ( ApplicationConfig(), RoutePathMetadata(controllerPath='/users', methodPath='/created'), '/users/created' ),
        ( ApplicationConfig(), RoutePathMetadata(controllerPath='users', methodPath='created'), '/users/created' ),
        ( ApplicationConfig(), RoutePathMetadata(controllerPath='users', methodPath='/'), '/users' ),
        ( ApplicationConfig(), RoutePathMetadata(controllerPath='/', methodPath='/created'), '/created' ),
        ( ApplicationConfig(), RoutePathMetadata(controllerPath='/', methodPath='/'), '/' ),
        ( ApplicationConfig(globalPrefix=True), RoutePathMetadata(controllerPath='/', methodPath='/'), '/api' ),
        ( ApplicationConfig(globalPrefix=True, versioning=True), RoutePathMetadata(controllerPath='/', methodPath='/'), '/api/v1' ),
        ( ApplicationConfig(globalPrefix=True, versioning=True), RoutePathMetadata(controllerPath='/users', methodPath='/', controllerVersion='2'), '/api/v2/users' ),
        ( ApplicationConfig(versioning=True), RoutePathMetadata(controllerPath='/users', methodPath='/created', methodVersion='2'), '/v2/users/created' ),
    ])
    def testCreate_ShouldReturnPath_WhenUseMetadata(self, config: ApplicationConfig, metadata: RoutePathMetadata, expect: str):
        routePathFactory = RoutePathFactory(config)
        path = routePathFactory.create(metadata)

        assert path == expect

    def testGetVersion_ShouldReturnMethodVersion_WhenMethodVersionIsAStringValue(self):
        
        config = ApplicationConfig()
        metadata = RoutePathMetadata(
            controllerPath='/users',
            controllerVersion='3',
            methodPath='/created',
            methodVersion='2'
        )

        routePathFactory = RoutePathFactory(config)
        version = routePathFactory.getVersion(metadata)

        assert version == metadata.methodVersion

    def testGetVersion_ShouldReturnControllerVersion_WhenMethodVersionIsANoneValue(self):
        
        config = ApplicationConfig()
        metadata = RoutePathMetadata(
            controllerPath='/users',
            controllerVersion='3',
            methodPath='/created',
            methodVersion=None
        )

        routePathFactory = RoutePathFactory(config)
        version = routePathFactory.getVersion(metadata)

        assert version == metadata.controllerVersion

    def testGetVersion_ShouldReturnDefaultVersion_WhenControllerAndMethodVersionIsANoneValue(self):
        
        config = ApplicationConfig(
            versioning=VersioningOptions( defaultVersion='1' )
        )

        metadata = RoutePathMetadata(
            controllerPath='/users',
            controllerVersion=None,
            methodPath='/created',
            methodVersion=None
        )

        routePathFactory = RoutePathFactory(config)
        version = routePathFactory.getVersion(metadata)

        assert version == config.versioning.defaultVersion
