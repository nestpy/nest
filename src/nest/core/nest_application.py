from typing import Any, Optional

from .application_config import ApplicationConfig

from nest.core.schema import ApplicationOptions
from nest.core.schema import ServerOptions
from nest.core.schema import CorsOptions
from nest.core.adapters import HttpAdapter
from nest.core.injector import NestContainer
from nest.common import VersioningOptions
"""
Core Application class that manages the NestPy application lifecycle and configuration.
"""
class NestApplication:
    def __init__(
        self,
        container: NestContainer,
        config: ApplicationConfig,
        http_adapter: HttpAdapter,
        options: ApplicationOptions
    ):
        self.container = container
        self.config = config
        self.http_adapter = http_adapter
        self.options = options


    def enable_cors(self, **options: CorsOptions) -> None: 
        self.http_adapter.enable_cors(options)
    
    def enable_versioning(self, **options: VersioningOptions) -> None: 
        self.config.enable_versioning(options)

    def listen(self, **options: ServerOptions) -> None: 
        self.http_adapter.register_routes(
            controllers=self.container.controllers,
            global_prefix=self.config.get_global_prefix(),
            versioning_options=self.config.get_versioning()
        )
        
        self.http_adapter.listen(**options)

    def set_global_prefix(self, prefix: str) -> None: 
        self.config.set_global_prefix(prefix)