from abc import ABC, abstractmethod

from nest.core.schema import CorsOptions
from nest.core.schema import ServerOptions

class HttpAdapter(ABC):

    @abstractmethod
    def enable_cors(self, **options: CorsOptions) -> None: pass

    @abstractmethod
    def listen(self, **options: ServerOptions) -> None: pass

    @abstractmethod
    def register_routes(self) -> None: pass

    

    