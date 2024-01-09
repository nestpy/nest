from abc import ABC, abstractmethod
from nest.common.enums import VersioningType
from nest.common.metadata import CorsOptions
from typing import List

class INestApplication(ABC):

    @abstractmethod
    def enableCors(self, options: CorsOptions = CorsOptions()) -> None:
        pass

    @abstractmethod
    def enableVersioning(self, type: VersioningType, defaultVersioning: str = "1") -> None:
        pass

    @abstractmethod
    def listen(self, host: str = "0.0.0.0", port: int = 3000) -> None:
        pass

    @abstractmethod
    def setGlobalPrefix(self, prefix: str, exclude: List[str] = []) -> None:
        pass
