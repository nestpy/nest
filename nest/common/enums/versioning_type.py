from enum import Enum

class VersioningType(Enum):
    None = 0
    URI = 1,
    HEADER = 2,
    MEDIA_TYPE = 3
    CUSTOM = 4
