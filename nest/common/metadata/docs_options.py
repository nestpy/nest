from pydantic import BaseModel

from nest.common.enums import DocsType

from typing import Any, Optional


class Contact(BaseModel):
    name: str
    url: str
    email: str


class LicenseInfo(BaseModel):
    name: str
    identifier: str


class ExternalDocs(BaseModel):
    description: str
    url: str


class OpenapiTags(BaseModel):
    name: str
    description: str
    externalDocs: Optional[ExternalDocs] = None


class DocsOptions(BaseModel):
    type: DocsType = DocsType.NONE
    swagger_url: str = "/docs"
    redoc_url: str = "/redoc"
    title: str = "Nestpy API Documentation"
    description: str = ""
    summary: str = ""
    version: str = "0.1.0"
    terms_of_service: str = ""
    contact: Any = None
    license_info: Any = None
    openapi_tags: Any = None
    openapi_url: str = "/openapi.json"
