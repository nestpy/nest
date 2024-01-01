from nest.common.decorators import Module

from users.user_controller import UserController

@Module(
    controllers=[UserController]
)
class UserModule:
    pass

