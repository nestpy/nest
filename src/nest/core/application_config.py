from typing import Any, List

class ApplicationConfig:
    global_prefix: str = ''
    global_prefix_options: Any = {}
    global_pipes: List[Any] = []
    global_interceptors: List[Any] = []
    global_guards: List[Any] = []
    versioningOptions: Any
    
    def __init__(self):
        pass

    def set_global_prefix(self, prefix: str) -> None:
        self.global_prefix = prefix

    def get_global_prefix(self) -> str:
        return self.global_prefix

    def set_global_prefix_options(self, options: Any) -> None:
        self.global_prefix_options = options

    def get_global_prefix_options(self) -> Any:
        return self.global_prefix_options

    def enable_versioning(self, options: Any) -> None:
        self.versioningOptions = options

    def get_versioning(self) -> Any:
        return self.versioningOptions