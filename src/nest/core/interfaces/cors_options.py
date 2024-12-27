from dataclasses import dataclass
from typing import Optional, Union, List
from re import Pattern

StaticOrigin = Union[bool, str, Pattern]

@dataclass
class CorsOptions:
    origin: StaticOrigin
    methods: Optional[Union[List[str], str]]
    allowedHeaders: Optional[Union[List[str], str]]
    exposedHeaders: Optional[Union[List[str], str]]
    credentials: Optional[bool]
    maxAge: Optional[int]
