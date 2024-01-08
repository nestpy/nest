from abc import ABC, abstractmethod
from nest.common.enums import VersioningType
from typing import List

class INestApplication(ABC):

    @abstractmethod
    def enableVersioning(self, type: VersioningType, defaultVersioning: str = "1"):
        pass

    @abstractmethod
    def listen(self, host: str = "0.0.0.0", port: int = 3000) -> None:
        pass

    @abstractmethod
    def setGlobalPrefix(self, prefix: str, exclude: List[str] = []) -> None:
        pass
