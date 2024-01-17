from nest.common import Injectable
from typing import List

from .user_dto import User


@Injectable()
class UserRepository:
    def __init__(self):
        self.users = [
            User(id="1", username="Manuel S. Lemos", email="mslemos@nespy.com")
        ]

    async def findAll(self) -> List[User]:
        return self.users

    async def findById(self, id: str) -> User:
        return [user for user in self.users if user.id == id][0]

    async def create(self, payload: User) -> User:
        self.users.append(payload)
        return payload

    async def update(self, id: str, payload: User) -> User:
        user = self.findById(id)
        index = self.users.index(user)
        self.users[index] = payload
        return payload

    async def delete(self, id: str) -> bool:
        user = self.findById(id)
        index = self.users.index(user)
        self.users.pop(index)
        return True
