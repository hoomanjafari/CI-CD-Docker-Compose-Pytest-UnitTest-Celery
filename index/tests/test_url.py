from django.test import (TestCase, SimpleTestCase)
from django.urls import (resolve, reverse)

from index.views import (IndexView, PostDetailView)


class TestUrl(SimpleTestCase):
    def test_url_resolve(self):
        url = reverse('index:index')
        self.assertEqual(
            resolve(url).func.view_class,
            IndexView
        )


class TestPostDetail(SimpleTestCase):
    def test_post_detail_url_resolve(self):
        url = reverse('index:post-detail', kwargs={'pk': 1})
        self.assertEqual(
            resolve(url).func.view_class,
            PostDetailView,
        )
