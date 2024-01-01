from fastapi import params, Response
from fastapi.datastructures import DefaultPlaceholder, Default
from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse

from nest.common.typing import SetIntStr, DictIntStrAny
from pydantic import BaseModel
from starlette.routing import Route as RouteBase
from typing import (
    Any,
    Dict,
    Optional,
    Sequence,
    Set,
    Type,
    Union,
    List,
)

class Route(BaseModel):
    path: str
    response_model: Optional[Type[Any]] = None
    status_code: Optional[int] = None
    tags: Optional[List[str]] = None
    dependencies: Optional[Sequence[params.Depends]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    response_description: str = "Successful Response"
    responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None
    deprecated: Optional[bool] = None
    methods: Optional[Union[Set[str], List[str]]] = None
    operation_id: Optional[str] = None
    response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = None
    response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = None
    response_model_by_alias: bool = True
    response_model_exclude_unset: bool = False
    response_model_exclude_defaults: bool = False
    response_model_exclude_none: bool = False
    include_in_schema: bool = True
    response_class: Union[Type[Response], DefaultPlaceholder] = Default(JSONResponse)
    name: Optional[str] = None
    route_class_override: Optional[Type[APIRoute]] = None
    callbacks: Optional[List[RouteBase]] = None
    openapi_extra: Optional[Dict[str, Any]] = None

    class Config:
        arbitrary_types_allowed = True