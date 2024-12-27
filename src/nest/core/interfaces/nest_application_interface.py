from abc import ABC, abstractmethod
from .cors_options import CorsOptions
from .version_options import VersioningOptions

class INestApplication(ABC):

    @abstractmethod
    def enable_cors(self, **options: CorsOptions) -> None: pass
    
    @abstractmethod
    def enable_versioning(self, **options: VersioningOptions) -> None: pass

    @abstractmethod
    def listen(self, *, port: int, host: str) -> None: pass

    @abstractmethod
    def set_global_prefix(self, prefix: str) -> None: pass
