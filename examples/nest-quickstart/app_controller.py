from nest.common.decorators import Controller, Get

@Controller('/')
class AppController:
    
    @Get('/')
    async def findAll():
        return {"Hello": "World"}
