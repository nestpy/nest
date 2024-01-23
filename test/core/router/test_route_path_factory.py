from nest.common.metadata import RoutePathMetadata
from nest.core import ApplicationConfig
from nest.core.router import RoutePathFactory

class TestRoutePathFactory:

    def test_ShouldReturnMethodVersion_WhenMethodVersionIsAGoodValue(self):
        
        config = ApplicationConfig()
        metadata = RoutePathMetadata(methodVersion='2', controllerVersion=3)
        routePathFactory = RoutePathFactory(config)

        version = routePathFactory.getVersion()

        assert version == '2'
