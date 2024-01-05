from nest.common.decorators import Module

from users.user_controller import UserController
from users.user_service import UserService
from users.user_repository import UserRepository

@Module(
    controllers=[UserController],
    providers=[UserService, UserRepository]
)
class UserModule:
    pass

