from nest.common.decorators import Controller

@Controller('/')
class AppController:
    
    async def findAll():
        return {"Hello": "World"}
