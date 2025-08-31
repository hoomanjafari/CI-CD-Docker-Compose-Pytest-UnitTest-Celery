from django.test import TestCase

from index.models import Post


class TestIndexModel(TestCase):
    # with setUp method we create our instance first then call them on other test methods
    def setUp(self):
        self.post = Post.objects.create(title='first_post', caption='this first post')

    def test_create_post_with_valid_data(self):
        self.assertTrue(
            Post.objects.filter(pk=self.post.id).exists()
        )

        # we can also do the test with this way
        # self.assertEquals(self.post.title, 'first_post')
