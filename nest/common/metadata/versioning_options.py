from pydantic import BaseModel

from nest.common.enums import VersioningType


class VersioningOptions(BaseModel):
    type: VersioningType = VersioningType.NONE
    defaultVersion: str = "1"
    header: str = "Api-Version"
    key: str = "v"
