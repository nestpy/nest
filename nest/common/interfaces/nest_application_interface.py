from abc import ABC, abstractmethod


class INestApplication(ABC):
    @abstractmethod
    def listen(self, host: str = "0.0.0.0", port: int = 3000) -> None:
        pass
