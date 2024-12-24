from enum import Enum

class VersioningType(Enum):
    """
    Enum for API versioning types.
    
    Values:
        URI: Version in the URI path
        HEADER: Version in HTTP header
        MEDIA_TYPE: Version in media type
        CUSTOM: Custom versioning strategy
    """
    URI = 1
    HEADER = 2
    MEDIA_TYPE = 3
    CUSTOM = 4
