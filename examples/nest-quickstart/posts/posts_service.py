from typing import List

from nest.common.decorators.core.injectable import Injectable

from users.users_service import UserService
from .posts_dto import CreatePostDto, PostModel

@Injectable()
class PostService:
    def __init__(self, user_service: UserService):
        self.posts = [PostModel(id=1, title="Post 1", content="Content 1", user_id=1)]
        self.next_id = 1
        self.user_service = user_service

    def create_post(self, post_data: CreatePostDto) -> PostModel:
        # Verificar que el usuario existe
        user = self.user_service.get_user_by_id(post_data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        post = PostModel(
            id=self.next_id,
            **post_data.dict()
        )
        self.posts.append(post)
        self.next_id += 1
        return post

    def get_posts(self) -> List[PostModel]:
        return self.posts