from nest.common.metadata import (
    CorsOptions,
    DocsOptions,
    GlobalPrefixOptions,
    VersioningOptions
)


class ApplicationConfig():
    def __init__(
        self,
        cors: bool = False,
        docs: bool = False,
        globalPrefix: bool = False,
        versioning: bool = False
    ):
        self.cors: bool | CorsOptions = cors
        self.docs: bool | DocsOptions = docs
        self.globalPrefix: bool | GlobalPrefixOptions = globalPrefix
        self.versioning: bool | VersioningOptions = versioning

