from nest.common import Get
from nest.common.keys import ROUTER_WATERMARK, ROUTE_INFO_KEY
from nest.common.metadata import RouteArgs


class TestRequestMethod:

    def test_GetDecorator_AssignsRouteArgsToFunction_UsingPathParam(self):

        path: str = '/get'
        user_expect = RouteArgs(
            path=path,
            methods=['GET'],
            status_code=200
        )

        def fn(): pass

        get_decorator = Get(path)
        fn_decorated = get_decorator(fn)

        assert hasattr(fn_decorated, ROUTER_WATERMARK)
        assert getattr(fn_decorated, ROUTER_WATERMARK)

        assert hasattr(fn_decorated, ROUTE_INFO_KEY)
        assert user_expect.__eq__(getattr(fn_decorated, ROUTE_INFO_KEY))

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
