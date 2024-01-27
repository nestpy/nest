from pydantic import BaseModel, ConfigDict

from typing import (
    Any,
    Dict,
    Optional,
    Union,
    List
)


class OpenapiArgs(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    description: Optional[str] = None
    include_in_schema: bool = True
    openapi_extra: Optional[Dict[str, Any]] = None
    responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None
    response_description: str = "Successful Response"
    summary: Optional[str] = None
    tags: Optional[List[str]] = None
