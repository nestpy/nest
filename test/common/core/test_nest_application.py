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

        assert app.config.cors is False
        assert app.config.globalPrefix is False
        assert app.config.versioning is False

    def test_ShouldDefaultConfigOptions_WhenInstanceWithCorsTrue(self):
        @Module()
        class app_module:
            pass

        config_expect = CorsOptions()

        config = ApplicationConfig(cors=True)
        app = NestApplication(app_module, config)

        assert config_expect.__eq__(app.config.cors)

    def test_ShouldException_WhenInstanceWithCorsNotBool(self):
        pass

    def test_ShouldException_WhenUseWildcardWithMoreValues(self):
        pass

    def test_ShouldException_WhenNotUseRequestMethodString(self):
        pass

    def test_ShouldConfigOptions_WhenUseEnableCorsMethod(self):
        @Module()
        class app_module:
            pass

        config_expect = CorsOptions(credentials=True)

        config = ApplicationConfig()
        app = NestApplication(app_module, config)

        app.enableCors(config_expect)

        assert config_expect.__eq__(app.config.cors)
