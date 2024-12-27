from .interfaces.nest_application_interface import INestApplication


"""
Core Application class that manages the NestPy application lifecycle and configuration.
"""
class NestApplication:
    def __init__(
        self,
        container: Container,
        http_adapter: AbstractHttpAdapter,
        config: ApplicationConfig,
        options: Optional[Any]
    ):
        self.container = container  # Private attribute
        self.config = config        # Private attribute

    def enable_cors(self, **options: CorsOptions) -> None: pass
    
    def enable_versioning(self, **options: VersioningOptions) -> None: 
        self.config.set_versioning_options(options)

    def listen(self, *, port: int, host: str) -> None: pass

    def set_global_prefix(self, prefix: str) -> None: 
        self.config.set_global_prefix(prefix)

    

    

    

