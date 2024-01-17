from nest.core import NestApplication, ApplicationConfig
from typing import Any, Optional


class NestFactoryStatic:
    def __init___(self):
        pass

    def create(
        self,
        module: Any,
        options: Optional[dict] = None
    ) -> NestApplication:
        applicationConfig = ApplicationConfig()

        # container = NestContainer(applicationConfig)
        # graphInspector = createGraphInspector(appOptions, container);

        # self.setAbortOnError(serverOrOptions, options
        # self.registerLoggerConfiguration(appOptions)

        # self.initialize(
        #     module,
        #     container,
        #     graphInspector,
        #     applicationConfig,
        #     appOptions,
        #     httpServer,
        # );

        instance = NestApplication(
            module,
            # container,
            # httpServer,
            applicationConfig,
            # graphInspector,
            # appOptions
        )

        # target = self.createNestInstance(instance)
        # return self.createAdapterProxy[T](target, httpServer)

        return instance


NestFactory = NestFactoryStatic()
