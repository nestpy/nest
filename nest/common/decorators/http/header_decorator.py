from fastapi import Response
from fastapi.responses import JSONResponse
from typing import Callable


def Header(header_name: str, header_value: str):
    def decorator(fn: Callable):
        async def wrapper(*args, **kwargs):
            response = await func(*args, **kwargs)

            if not isinstance(response, Response):
                response = JSONResponse(content=response)

            response.headers[header_name] = header_value
            return response
        return fn
    return decorator