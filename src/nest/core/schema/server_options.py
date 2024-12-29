from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class ServerOptions:
    """
    The port to listen on.
    """
    port: str | int = 3000
    """
    The host to listen on.
    """
    host: Optional[str] = '0.0.0.0'