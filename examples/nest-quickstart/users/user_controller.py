from nest.common.decorators import Controller

@Controller('/users')
class UserController:
    
    async def findAll() -> str:
        return {"Hello": "World"}

    async def findById(id: str) -> str:
        return {"Hello": id}

    async def create() -> str:
        return {"Hello": "World"}

    async def update(id: str) -> str:
        return {"Hello": id}

    async def delete(id: str) -> str:
        return {"Hello": id}
