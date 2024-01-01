from nest.common.decorators import Module

@Module(
    imports=['A'],
    controllers=['B'],
    providers=['C'],
    exports=['D']
)
class AppModule: 
    pass
