from nest.common.decorators import Controller, Get, HttpCode


@Controller("/")
class AppController:
    def __init__(self):
        pass

    @Get("/")
    @HttpCode(202)
    def findAll(self):
        return {"Hello": "World"}
