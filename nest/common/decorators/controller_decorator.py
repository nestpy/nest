from typing import ( List, Optional )
from nest.common.keys import IS_ROUTE_KEY, ROUTE_INFO_KEY
from nest.common.metadata import Route

class Controller:
    def __init__( self, prefix: str = '/'): 
        self.prefix = prefix
    
    def __call__(decorator, ClassBasedView):
        class IController(ClassBasedView):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.prefix = self.set_prefix(decorator.prefix)
                self.tags = self.set_tag(decorator.prefix)
                self.routes = self.set_routes()

            
            def set_prefix(self, value: str) -> str:
                if not value.startswith("/"):
                    value = f'/{value}'

                if value.endswith("/"):
                    value = value[:-1]

                return value
            
            def set_routes(self) -> List[Route]:
                routes = []

                for attr_name in dir(ClassBasedView):
                    attr = getattr(ClassBasedView, attr_name)
                    
                    if callable(attr) and hasattr(attr, IS_ROUTE_KEY):
                        route = getattr(attr, ROUTE_INFO_KEY)
                        routes.append(route.copy(update={'attr': attr}))

                return routes

            def set_tag(self, value: str) -> Optional[List[str]]:
                if value.__eq__('/'):
                    return ['/']
                
                return [ self.set_prefix(value) ]
            
        IController.decorator = decorator
        return IController