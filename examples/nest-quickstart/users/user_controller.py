from typing import List

from nest.common.decorators import Controller, Get, Post, Put, Delete

from users.user_service  import UserService
from .user_dto import User


@Controller('/users')
class UserController:
    
    def __init__(self, user_service: UserService):
        self.user_service = user_service
    
    @Get('/')
    async def findAll(self) -> List[User]:
        return self.user_service.findAll()

    @Get('/{id}', deprecated=True)
    async def findById(self, id: str) -> User:
        return self.user_service.findById(id)

    @Post('/')
    async def create(self, body: User) -> User:
        return self.user_service.create(body)

    @Put('/{id}')
    async def update(self, id: str, body: User) -> User:
        return self.user_service.update(id, body)

    @Delete('/{id}')
    async def delete(self, id: str) -> bool:
        return self.user_service.delete(id)
