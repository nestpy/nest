from typing import Union, List, Optional, Callable, Any
from dataclasses import dataclass

from ..enums.version_type import VersioningType


VERSION_NEUTRAL = object() # TODO: Create own Simbol class

VersionValue = Union[
    str, 
    type(VERSION_NEUTRAL), 
    List[Union[str, type(VERSION_NEUTRAL)]]
]

# @dataclass
# class VersionOptions:
#     version: Optional[VersionValue]

@dataclass
class VersioningCommonOptions:
    default_version: Optional[VersionValue] = None

@dataclass
class HeaderVersioningOptions(VersioningCommonOptions):
    type: VersioningType = VersioningType.HEADER
    header: str = "X-Version"

@dataclass
class URIVersioningOptions(VersioningCommonOptions):
    type: VersioningType = VersioningType.URI
    prefix: Optional[Union[str, bool]] = False

@dataclass
class MediaTypeVersioningOptions(VersioningCommonOptions):
    type: VersioningType = VersioningType.MEDIA_TYPE
    key: str = "version"

@dataclass
class CustomVersioningOptions(VersioningCommonOptions):
    type: VersioningType = VersioningType.CUSTOM
    extractor: Callable[[Any], Union[str, List[str]]] = lambda request: request.headers.get("X-Version")

VersioningOptions = Union[
    HeaderVersioningOptions, 
    URIVersioningOptions, 
    MediaTypeVersioningOptions, 
    CustomVersioningOptions
]

