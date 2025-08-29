from django.test import (TestCase, SimpleTestCase)

from index.serializers import PostSerializer


class TestSerializer(SimpleTestCase):
    def test_serializer_with_valid_data(self):
        serializer = PostSerializer(data={
            'title': '3rd_post',
            'caption': 'this is the 3rd post',
        })
        self.assertTrue(serializer.is_valid())

    def test_serializer_with_no_data(self):
        serializer = PostSerializer(data={})
        self.assertFalse(serializer.is_valid())
