from abc import ABC, abstractmethod
from nest.common.enums import DocsType, VersioningType
from nest.common.metadata import CorsOptions, DocsOptions
from typing import List


class INestApplication(ABC):
    @abstractmethod
    def enableCors(self, options: CorsOptions) -> None:
        pass

    @abstractmethod
    def enableDocs(self, type: DocsType, options: DocsOptions) -> None:
        pass

    @abstractmethod
    def enableVersioning(
        self, type: VersioningType, defaultVersion: str = "1"
    ) -> None:
        pass

    @abstractmethod
    def listen(self, host: str = "0.0.0.0", port: int = 3000) -> None:
        pass

    @abstractmethod
    def setGlobalPrefix(self, prefix: str, exclude: List[str] = []) -> None:
        pass
