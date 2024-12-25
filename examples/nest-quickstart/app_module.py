from nest.common import Module

from posts.posts_module import PostsModule
from users.users_module import UsersModule

@Module(
    imports=[UsersModule, PostsModule]
)
class AppModule:
    pass