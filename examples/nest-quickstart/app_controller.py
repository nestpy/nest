from nest.common.decorators import Controller, Get, HttpCode, Header


@Controller("/")
class AppController:
    def __init__(self):
        pass

    @Get("/")
    @HttpCode(202)
    @Header("X-Cat-Dog", "custom value")
    def findAll(self):
        return {"Hello": "World"}
