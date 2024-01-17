from nest.common.decorators import Module

from app_controller import AppController
from users.user_module import UserModule


@Module(imports=[UserModule], controllers=[AppController])
class AppModule:
    pass
