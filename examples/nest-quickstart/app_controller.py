from nest.common.decorators import Controller, Get, HttpCode

@Controller('/')
class AppController:
    
    @Get('/')
    @HttpCode(202)
    async def findAll():
        return {"Hello": "World"}
