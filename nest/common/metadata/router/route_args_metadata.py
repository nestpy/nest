from pydantic import BaseModel, ConfigDict
from typing import List


class RouteArgs(BaseModel):
    path: str
    # TODO: Change to HttpStatus enum
    status_code: int
    methods: List[str] = []

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra='allow',
        use_enum_values=True
    )
