from nest.core.nest_application import NestApplication

from app_module import AppModule

def bootstrap():
    app = NestApplication( AppModule )

    app.listen()

if __name__ == "__main__":
    bootstrap()