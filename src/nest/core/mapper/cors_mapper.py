from nest.core.schema import CorsOptions
from nest.core.schema import FastApiCorsOptions

def map_cors_options(cors_options: CorsOptions) -> FastApiCorsOptions:
    """
    Maps Nest CORS options to FastAPI CORSMiddleware options
    """
    fastapi_cors_options = {
        "allow_origins": cors_options.get("origin", ["*"]),
        "allow_methods": cors_options.get("methods", ["*"]),
        "allow_headers": cors_options.get("allowedHeaders", ["*"]),
        "allow_credentials": cors_options.get("credentials", False),
        "expose_headers": cors_options.get("exposedHeaders", []),
        "max_age": cors_options.get("maxAge", 600),  # 10 minutos por defecto
    }

    # Convertir string a lista si es necesario
    if isinstance(fastapi_cors_options["allow_origins"], str):
        fastapi_cors_options["allow_origins"] = [fastapi_cors_options["allow_origins"]]
    if isinstance(fastapi_cors_options["allow_methods"], str):
        fastapi_cors_options["allow_methods"] = [fastapi_cors_options["allow_methods"]]
    if isinstance(fastapi_cors_options["allow_headers"], str):
        fastapi_cors_options["allow_headers"] = [fastapi_cors_options["allow_headers"]]
    if isinstance(fastapi_cors_options["expose_headers"], str):
        fastapi_cors_options["expose_headers"] = [fastapi_cors_options["expose_headers"]]

    return fastapi_cors_options