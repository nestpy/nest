from nest.common.metadata import (
    CorsOptions,
    DocsOptions,
    GlobalPrefixOptions,
    VersioningOptions,
)
from nest.common.enums import VersioningType


from typing import Any, List, Union


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
        self.globalPrefix: Union[bool, GlobalPrefixOptions] = globalPrefix
        self.versioning: Union[bool, VersioningOptions] = versioning

    def getCors(self):
        if(self._isTrueBoolProperty(self.cors)):
            return CorsOptions()

        return self.globalPrefix

    def getDocs(self):
        if(self._isTrueBoolProperty(self.docs)):
            return DocsOptions()

        return self.globalPrefix

    def getGlobalPrefix(self):
        if(self._isTrueBoolProperty(self.globalPrefix)):
            return GlobalPrefixOptions()

        return self.globalPrefix
    
    def setGlobalPrefix(self, prefix: str, exclude: List[str] = []):
        self.globalPrefix = GlobalPrefixOptions(prefix, exclude)

    def getVersioning(self):
        if(self._isTrueBoolProperty(self.versioning)):
            return VersioningOptions()

        return self.versioning

    def setVersioning(
        self,
        version: str,
        type: Any = VersioningType.URI,
        header: str = '',
        key: str = 'v'
    ):
        self.versioning = VersioningOptions(
            type=type,
            defaultVersion=version,
            header=header,
            key=key
        )

    def _isTrueBoolProperty(self, property: Any):
        return isinstance(property, bool) and property