from nest.common.decorators import Module

from app_controller import AppController 
from users import UserModule

@Module(
    imports=[UserModule],
    controllers=[AppController],
    providers=[],
    exports=[]
)
class AppModule: 
    pass
