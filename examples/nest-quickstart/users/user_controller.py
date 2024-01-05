from nest.common.decorators import Controller, Get, Post, Put, Delete

@Controller('/users')
class UserController:
    
    @Get('/')
    async def findAll(self) -> str:
        return {"Hello": "World"}

    @Get('/{id}', deprecated=True)
    async def findById(self, id: str) -> str:
        return {"Hello": id}

    @Post('/')
    async def create(self) -> str:
        return {"Hello": "World"}

    @Put('/{id}')
    async def update(self, id: str) -> str:
        return {"Hello": id}

    @Delete('/{id}')
    async def delete(self, id: str) -> str:
        return {"Hello": id}
