from fastapi import params, Response
from fastapi.datastructures import DefaultPlaceholder, Default
from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse

from nest.common.typing import SetIntStr, DictIntStrAny
from pydantic import BaseModel, ConfigDict
from starlette.routing import Route as RouteBase
from typing import (
    Any,
    Callable,
    Dict,
    Optional,
    Sequence,
    Set,
    Type,
    Union,
    List,
)

ResponseType = Union[Type[Response], DefaultPlaceholder]


class OpenapiArgs(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    description: Optional[str] = None
    include_in_schema: bool = True
    openapi_extra: Optional[Dict[str, Any]] = None
    responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None
    response_description: str = "Successful Response"
    summary: Optional[str] = None
    tags: Optional[List[str]] = None


class RouteArgs(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    path: str
    status_code: Optional[int] = None
    methods: Optional[Union[Set[str], List[str]]] = None
    response_model: Optional[Type[Any]] = None
    dependencies: Optional[Sequence[params.Depends]] = None
    deprecated: Optional[bool] = None
    operation_id: Optional[str] = None
    response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = None
    response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = None
    response_model_by_alias: bool = True
    response_model_exclude_unset: bool = False
    response_model_exclude_defaults: bool = False
    response_model_exclude_none: bool = False
    response_class: ResponseType = Default(JSONResponse)
    name: Optional[str] = None
    route_class_override: Optional[Type[APIRoute]] = None
    callbacks: Optional[List[RouteBase]] = None


class Route(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

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
    response_class: ResponseType = Default(JSONResponse)
    name: Optional[str] = None
    route_class_override: Optional[Type[APIRoute]] = None
    callbacks: Optional[List[RouteBase]] = None
    openapi_extra: Optional[Dict[str, Any]] = None
    endpoint: Optional[Callable[..., Any]] = None
    version: Optional[str] = None
