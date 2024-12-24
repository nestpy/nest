from nest.common.decorators.core.module import Module

from posts.posts_module import PostsModule
from users.users_module import UsersModule

@Module(
    imports=[UsersModule, PostsModule]
)
class AppModule:
    pass