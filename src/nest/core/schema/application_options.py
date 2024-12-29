from dataclasses import dataclass
from typing import Optional, Any

from .cors_options import CorsOptions

@dataclass
class ApplicationOptions:
    """
    CORS options from [CORS package]
    """
    cors: Optional[bool | CorsOptions] = False
    """
    Whether to use underlying platform body parser.
    """
    body_parser: Optional[bool] = False
    """
    Set of configurable HTTPS options
    """
    https_options: Optional[Any] = None
    """
    Whether to register the raw request body on the request. Use `req.rawBody`.
    """
    raw_body: Optional[bool] = False
    """
    Force close open HTTP connections. Useful if restarting your application hangs due to
    keep-alive connections in the HTTP adapter.
    """
    force_close_connections: Optional[bool] = False