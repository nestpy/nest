from nest.common import Module, VersioningType
from nest.common.metadata import VersioningOptions
from nest.core import NestApplication, ApplicationConfig


class TestVersioning:

    def test_ShouldDefaultConfigOptions_WhenInstanceWithVersioningTrue(self):
        @Module()
        class app_module:
            pass

        config_expect = VersioningOptions(type=VersioningType.URI)

        config = ApplicationConfig(versioning=True)
        app = NestApplication(app_module, config)

        assert config_expect.__eq__(app.config.versioning)

    def test_ShouldConfigOptions_WhenUseEnableVersioningMethod(self):
        @Module()
        class app_module:
            pass

        type_expect = VersioningType.URI

        config = ApplicationConfig()
        app = NestApplication(app_module, config)

        app.enableVersioning(type=type_expect)

        assert app.config.versioning.type == type_expect