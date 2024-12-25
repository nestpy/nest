from nest.common import Module

from .posts_controller import PostController
from .posts_service import PostService
from users.users_module import UsersModule

@Module(
    imports=[UsersModule],
    controllers=[PostController],
    providers=[PostService]
)
class PostsModule:
    pass