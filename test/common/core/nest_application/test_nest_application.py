from nest.common import Module
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
        assert app.config.docs is False
