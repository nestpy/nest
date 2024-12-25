from typing import List, Optional

from nest.common import Injectable

from .users_dto import User, CreateUserDto

@Injectable()
class UserService:
    def __init__(self):
        self.users = [
            User(id=1, name="John Doe", email="john@example.com"),
            User(id=2, name="Jane Doe", email="jane@example.com")
        ]
        self.next_id = 3

    def get_users(self) -> List[User]:
        return self.users

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return next((user for user in self.users if user.id == user_id), None)

    def create_user(self, user_data: CreateUserDto) -> User:
        new_user = User(
            id=self.next_id,
            name=user_data.name,
            email=user_data.email
        )
        self.users.append(new_user)
        self.next_id += 1
        return new_user

    def update_user(self, user_id: int, user_data: CreateUserDto) -> Optional[User]:
        user = self.get_user_by_id(user_id)
        if user:
            user.name = user_data.name
            user.email = user_data.email
            return user
        return None

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if user:
            self.users = [u for u in self.users if u.id != user_id]
            return True
        return False
