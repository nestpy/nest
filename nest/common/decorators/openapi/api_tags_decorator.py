from typing import Callable, List
from nest.common.keys import OPENAPI_TAGS_KEY


def ApiTags(tags: str | List[str]):
    tags = [tags] if type(tags) is str else tags

    def decorator(fn: Callable):
        setattr(fn, OPENAPI_TAGS_KEY, tags)

        return fn

    return decorator
