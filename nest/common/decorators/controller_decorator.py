from typing import ( List, Optional )

class Controller:
    def __init__( self, prefix: str = '/'): 
        self.prefix = prefix
    
    def __call__(decorator, ClassBasedView):
        class IController(ClassBasedView):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.prefix = self.set_prefix(decorator.prefix)
                self.tags = self.set_tag(decorator.prefix)
                self.routes = []

            
            def set_prefix(self, value: str) -> str:
                if not value.startswith("/"):
                    value = f'/{value}'

                if value.endswith("/"):
                    value = value[:-1]

                return value
            
            # TODO: Create options kind tag in DocsOptions
            def set_tag(self, value: str) -> Optional[List[str]]:
                if value.__eq__('/'):
                    return ['/']
                
                return [ self.set_prefix(value) ]
            
        IController.decorator = decorator
        return IController