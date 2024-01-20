from nest.common import Module
from nest.common.metadata import GlobalPrefixOptions
from nest.core import NestApplication, ApplicationConfig


class TestGlobalPrefix:

    def test_ShouldDefaultConfigOptions_WhenInstanceWithGlobalPrefixTrue(self):
        @Module()
        class app_module:
            pass

        config_expect = GlobalPrefixOptions(prefix='/api')

        config = ApplicationConfig(globalPrefix=True)
        app = NestApplication(app_module, config)

        assert config_expect.__eq__(app.config.globalPrefix)

    def test_ShouldConfigOptions_WhenUseSetGlobalPrefixMethod(self):
        @Module()
        class app_module:
            pass

        prefix_expect ='test'
        exclude_expect = ['users']

        config = ApplicationConfig()
        app = NestApplication(app_module, config)

        app.setGlobalPrefix(
            prefix=prefix_expect,
            exclude=exclude_expect
        )

        assert app.config.globalPrefix.prefix == prefix_expect
        assert app.config.globalPrefix.exclude == exclude_expect