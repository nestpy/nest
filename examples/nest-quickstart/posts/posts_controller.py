from nest.common.decorators.core.controller import Controller
from nest.common.decorators.http.request_mapping import Get, Post

from .posts_dto import CreatePostDto
from .posts_service import PostService

@Controller("/posts")
class PostController:
    def __init__(self, post_service: PostService):
        self.post_service = post_service

    @Get("/")
    async def get_posts(self):
        return self.post_service.get_posts()

    @Post("/")
    async def create_post(self, post_data: CreatePostDto):
        return self.post_service.create_post(post_data)