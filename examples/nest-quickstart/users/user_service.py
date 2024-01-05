from typing import List

from .user_repository import UserRepository
from .user_dto import User

class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def findAll(self) -> List[User]:
        return self.user_repository.findAll()

    async def findById(self, id: str) -> User:
        return self.user_repository.findById(id)

    async def create(self, payload: User) -> User:
        return self.user_repository.create(payload)

    async def update(self, id: str, payload: User) -> User:
        return self.user_repository.update(id, payload)

    async def delete(self, id: str) -> bool:
        return self.user_repository.delete(id)