from nest.common import Get, Post
from nest.common.keys import ROUTER_WATERMARK, ROUTE_INFO_KEY
from nest.common.metadata import RouteArgs

import pytest

class TestRequestMethod:

    @pytest.mark.parametrize("path,route_expect,method", [
        ('/', RouteArgs(path='/', methods=['GET'], status_code=200), Get),
        ('/', RouteArgs(path='/', methods=['GET'], status_code=200), Get),
        ('/api', RouteArgs(path='/api', methods=['GET'], status_code=200), Get),
        ('/', RouteArgs(path='/', methods=['POST'], status_code=201), Post),
        ('/', RouteArgs(path='/', methods=['POST'], status_code=201), Post),
        ('/api', RouteArgs(path='/api', methods=['POST'], status_code=201), Post)
    ])
    def test_GetDecorator_AssignsRouteArgsToFunction_UsingPathParam(self, path, route_expect, method):

        @method(path)
        def fn(): pass

        assert hasattr(fn, ROUTER_WATERMARK)
        assert getattr(fn, ROUTER_WATERMARK)

        assert hasattr(fn, ROUTE_INFO_KEY)
        assert route_expect.__eq__(getattr(fn, ROUTE_INFO_KEY))

    def test_GetDecorator_AssignsRouteArgsToFunction_UsingDefaultParam(self):

        user_expect = RouteArgs(
            path='/',
            methods=['GET'],
            status_code=200
        )

        def fn(): pass

        get_decorator = Get()
        fn_decorated = get_decorator(fn)

        assert hasattr(fn_decorated, ROUTER_WATERMARK)
        assert getattr(fn_decorated, ROUTER_WATERMARK)

        assert hasattr(fn_decorated, ROUTE_INFO_KEY)
        assert user_expect.__eq__(getattr(fn_decorated, ROUTE_INFO_KEY))
