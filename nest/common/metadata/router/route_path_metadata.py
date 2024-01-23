from pydantic import BaseModel

from typing import Optional

class RoutePathMetadata(BaseModel):
    controllerPath: str
    controllerVersion: Optional[str] = None
    methodPath: str
    methodVersion: Optional[str] = None
    # modulePath: str