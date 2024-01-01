from nest.common.decorators import Controller, Get, Post, Put, Delete

@Controller('/users')
class UserController:
    
    Get('/')
    async def findAll() -> str:
        return {"Hello": "World"}

    Get('/')
    async def findById(id: str) -> str:
        return {"Hello": id}

    Post('/')
    async def create() -> str:
        return {"Hello": "World"}

    Put('/')
    async def update(id: str) -> str:
        return {"Hello": id}

    Delete('/')
    async def delete(id: str) -> str:
        return {"Hello": id}
