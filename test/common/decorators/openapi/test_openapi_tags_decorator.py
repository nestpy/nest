from nest.common.decorators import ApiTags
from nest.common.keys import OPENAPI_TAGS_KEY


class TestApiTags():

    def test_ShouldAssinsListTagsToFunction_UsingListStrParam(self):

        tags = ['one', 'two']

        @ApiTags(tags)
        def fn(): pass

        assert hasattr(fn, OPENAPI_TAGS_KEY)
        assert getattr(fn, OPENAPI_TAGS_KEY) == tags

    def test_ShouldAssinsListTagsToFunction_UsingStrParam(self):

        tags = 'one'

        @ApiTags(tags)
        def fn(): pass

        assert hasattr(fn, OPENAPI_TAGS_KEY)
        assert getattr(fn, OPENAPI_TAGS_KEY) == [tags]
