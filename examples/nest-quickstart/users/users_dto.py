from pydantic import BaseModel

class CreateUserDto(BaseModel):
    name: str
    email: str

class User(BaseModel):
    id: int
    name: str
    email: str
