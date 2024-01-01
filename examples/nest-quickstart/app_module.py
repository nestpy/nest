from nest.common.decorators import Module

from app_controller import AppController 

@Module(
    imports=[],
    controllers=[AppController]
)
class AppModule: 
    pass
