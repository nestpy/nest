from typing import ( Any, List )

class Module:
    def __init__(
        self,
        imports: List[Any] = [], 
        controllers: List[Any] = [], 
        providers: List[Any] = [], 
        exports: List[Any] = []
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