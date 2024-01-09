from nest.common.metadata import CorsOptions, GlobalPrefixOptions, VersioningOptions


class ApplicationConfig():
    def __init__(
        self,
        cors: bool = False,
        globalPrefix: bool = False,
        versioning: bool = False
    ):
        self.cors: bool | CorsOptions = cors
        self.globalPrefix: bool | GlobalPrefixOptions = globalPrefix
        self.versioning: bool | VersioningOptions = versioning

