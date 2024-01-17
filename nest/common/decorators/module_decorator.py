from nest.common.decorators import Controller  # Change for typing
from typing import Any, List, TypeVar


TModule = TypeVar("TModule", bound="Module")


class Module:
    def __init__(
        self,
        imports: List[TModule] = [],
        controllers: List[Controller] = [],
        providers: List[Any] = [],
        exports: List[TModule] = [],
    ):
        self.imports = imports
        self.controllers = controllers
        self.providers = providers
        self.exports = exports

    def __call__(decorator, ClassBasedView):
        class IModule(ClassBasedView):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                self.imports = decorator.imports
                self.controllers = decorator.controllers
                self.providers = decorator.providers
                self.exports = decorator.exports

        IModule.decorator = decorator
        return IModule
