from nest.common.decorators.core.module import Module

from .users_controller import UserController
from .users_service import UserService

@Module(
    imports = [],
    controllers = [UserController],
    providers = [UserService],
    exports = [UserService]
)
class UsersModule:
    pass