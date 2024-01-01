from nest.common.decorators import Controller, Get, Post, Put, Delete

@Controller('/users')
class UserController:
    
    @Get('/')
    async def findAll() -> str:
        return {"Hello": "World"}

    @Get('/{id}', deprecated=True)
    async def findById(id: str) -> str:
        return {"Hello": id}

    @Post('/')
    async def create() -> str:
        return {"Hello": "World"}

    @Put('/{id}')
    async def update(id: str) -> str:
        return {"Hello": id}

    @Delete('/{id}')
    async def delete(id: str) -> str:
        return {"Hello": id}
