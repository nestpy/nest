from dataclasses import dataclass
from typing import Optional, Union, List
from re import Pattern

StaticOrigin = Union[bool, str, Pattern]

"""
Interface describing CORS options that can be set.
"""
@dataclass
class CorsOptions:
    """
    Configures the Access-Control-Allow-Origins CORS header.  See [here for more detail.](https://github.com/expressjs/cors#configuration-options)
    """
    origin: StaticOrigin
    """
    Configures the Access-Control-Allow-Methods CORS header.
    """
    methods: Optional[ List[str] | str] 
    """
    Configures the Access-Control-Allow-Headers CORS header.
    """
    allowedHeaders: Optional[ List[str] | str]
    """
    Configures the Access-Control-Expose-Headers CORS header.
    """
    exposedHeaders: Optional[ List[str] | str]
    """
    Configures the Access-Control-Allow-Credentials CORS header.
    """
    credentials: Optional[bool]
    """
    Configures the Access-Control-Max-Age CORS header.
    """
    maxAge: Optional[int] 