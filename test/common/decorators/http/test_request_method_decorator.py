from nest.common import Delete, Get, Head, Options, Path, Put
from nest.common.keys import IS_ROUTE_KEY, ROUTE_INFO_KEY
from nest.common.metadata import Route


class TestRequestMethod:

    def test_GetDecorator_AssignsRouteArgsToFunction_UsingPathParam(self):

        path: str = '/get'
        user_expect = Route(
            path=path, 
            methods=['GET'], 
            status_code=200
        )

        def fn(): pass

        get_decorator = Get(path)
        fn_decorated = get_decorator(fn)

        assert hasattr(fn_decorated, IS_ROUTE_KEY)
        assert getattr(fn_decorated, IS_ROUTE_KEY)
        
        assert hasattr(fn_decorated, ROUTE_INFO_KEY)
        assert user_expect.__eq__(getattr(fn_decorated, ROUTE_INFO_KEY))

    def test_GetDecorator_AssignsRouteArgsToFunction_UsingDefaultParam(self):

        user_expect = Route(
            path='/',
            methods=['GET'], 
            status_code=200
        )

        def fn(): pass

        get_decorator = Get()
        fn_decorated = get_decorator(fn)

        assert hasattr(fn_decorated, IS_ROUTE_KEY)
        assert getattr(fn_decorated, IS_ROUTE_KEY)
        
        assert hasattr(fn_decorated, ROUTE_INFO_KEY)
        assert user_expect.__eq__(getattr(fn_decorated, ROUTE_INFO_KEY)) 