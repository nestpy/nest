from pydantic import BaseModel


class CreatePostDto(BaseModel):
    title: str
    content: str
    user_id: int

class PostModel(BaseModel):
    id: int
    title: str
    content: str
    user_id: int