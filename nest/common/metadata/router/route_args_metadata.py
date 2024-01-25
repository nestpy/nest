from pydantic import BaseModel, ConfigDict

class RouteArgs(BaseModel):
    path: str
    status_code: int #TODO: Change to HttpStatus enum

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra='allow',
        use_enum_values=True
    )