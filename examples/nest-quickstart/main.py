from nest.core.nest_application import NestApplication

def bootstrap():
    app = NestApplication( )

    app.listen()

if __name__ == "__main__":
    bootstrap()