from nest.common.metadata import RoutePathMetadata, VersioningOptions
from nest.core import ApplicationConfig
from nest.core.router import RoutePathFactory

import pytest

class TestRoutePathFactory:

    def test_ShouldReturnMethodVersion_WhenMethodVersionIsAStringValue(self):
        
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

    def test_ShouldReturnControllerVersion_WhenMethodVersionIsANoneValue(self):
        
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

    def test_ShouldReturnDefaultVersion_WhenControllerAndMethodVersionIsANoneValue(self):
        
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
