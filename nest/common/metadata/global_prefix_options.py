from pydantic import BaseModel
from typing import List


class GlobalPrefixOptions(BaseModel):
    prefix: str = "/api"
    exclude: List[str] = []
