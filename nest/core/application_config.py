from nest.common.metadata import (
    CorsOptions,
    DocsOptions,
    GlobalPrefixOptions,
    VersioningOptions,
)

from typing import Union


class ApplicationConfig:
    def __init__(
        self,
        cors: bool = False,
        docs: bool = False,
        globalPrefix: bool = False,
        versioning: bool = False,
    ):
        self.cors: Union[bool, CorsOptions] = cors
        self.docs: Union[bool, DocsOptions] = docs
        self.globalPrefix: bool | GlobalPrefixOptions = globalPrefix
        self.versioning: bool | VersioningOptions = versioning
