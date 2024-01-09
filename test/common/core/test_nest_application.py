from nest.common import Module
from nest.common.metadata import CorsOptions
from nest.core import NestApplication, ApplicationConfig


class TestNestApplication:        

    def test_ShouldFalseInOptions_WhenInstanceByDefault(self):
        @Module()
        class app_module: 
            pass

        config = ApplicationConfig()
        app = NestApplication(app_module, config)

        assert app.config.cors == False
        assert app.config.globalPrefix == False
        assert app.config.versioning == False

