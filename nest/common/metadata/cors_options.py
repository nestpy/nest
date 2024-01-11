from pydantic import BaseModel
from typing import List


class CorsOptions(BaseModel):
    origins: List[str] = ["*"]
    methods: List[str] = ["*"]
    allowedHeaders: List[str] = ["*"]
    exposedHeaders: List[str] = ["*"]
    credentials: bool = False
    maxAge: int = 3600
