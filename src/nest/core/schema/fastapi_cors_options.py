from dataclasses import dataclass
from typing import Optional, List

@dataclass
class FastApiCorsOptions:
    origin: Optional[str] = None
    allow_credentials: Optional[bool] = None
    allow_methods: Optional[List[str]] = None
    allow_headers: Optional[List[str]] = None
    expose_headers: Optional[List[str]] = None
    max_age: Optional[int] = None
