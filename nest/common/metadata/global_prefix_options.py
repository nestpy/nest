from pydantic import BaseModel
from typing import ( List )

class GlobalPrefixOptions(BaseModel):
    exclude: List[str] = []
    prefix: str = ''