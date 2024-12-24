from http import HTTPStatus

from nest.common.decorators.http.http_code import HttpCode
from nest.common.decorators.http.request_mapping import Get, Post, Delete
from nest.common.decorators.core.controller import Controller
from nest.common.decorators.core.version import Version

from fastapi import HTTPException

from .users_service import UserService
from .users_dto import CreateUserDto

@Controller("/users", version="2")
class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    @HttpCode(201)
    @Get("/")
    async def get_users(self):
        return self.user_service.get_users()

    @Get("/{user_id}")
    @Version("2")
    async def get_user(self, user_id: int):
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @Post("/")
    @HttpCode(HTTPStatus.CREATED)
    @Version("3")
    async def create_user(self, user_data: CreateUserDto):
        return self.user_service.create_user(user_data)

    @Delete("/{user_id}")
    @HttpCode(204)
    async def delete_user(self, user_id: int):
        if not self.user_service.delete_user(user_id):
            raise HTTPException(status_code=404, detail="User not found")
        return None