from nest.common.decorators import Module

from .user_controller import UserController

@Module(
    controllers=[UserController]
)
class UserModule:
    pass
