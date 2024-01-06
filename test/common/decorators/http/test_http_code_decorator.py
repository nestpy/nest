from nest.common import HttpCode, HttpStatus
from nest.common.keys import ROUTE_HTTP_CODE_KEY

import pytest


class TestHttpCode:
    
    def test_HttpCodeDecorator_AssignsStatusCodeToFunction_UsingIntParam(self):

        def fn(): pass
        status = 200

        http_code_decorator = HttpCode(status)
        fn_decorated = http_code_decorator(fn)

        assert hasattr(fn_decorated, ROUTE_HTTP_CODE_KEY)
        assert getattr(fn_decorated, ROUTE_HTTP_CODE_KEY) == status

    def test_HttpCodeDecorator_RaisesValueError_InvalidIntStatus(self):

        status = 315

        with pytest.raises(ValueError) as exception:
            HttpCode(status)

        message = f"Value {status} is not a part of {HttpStatus.__name__}"
        assert str(exception.value) == message

    def test_ShouldAssinsStatusCodeToFunction_UsingEnumParam(self): pass
