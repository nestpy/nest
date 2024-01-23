from pydantic import BaseModel


class RoutePathMetadata(BaseModel):
    controllerPath: str
    controllerVersion: str
    methodPath: str
    methodVersion: str
    # modulePath: str