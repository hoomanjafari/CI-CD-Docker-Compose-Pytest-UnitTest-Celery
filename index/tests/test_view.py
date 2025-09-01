from django.test import (TestCase, SimpleTestCase, Client)
from django.contrib.auth.models import User
from django.urls import reverse

from index.models import Post


class TestView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_1', email='test_1.email.com', password='123')
        self.post = Post.objects.create(title='2nd_post', caption='this is 2nd post')
        self.client = Client()

    # to check the views response's status code is 200 or not
    def test_url_view_status_200(self):
        url = reverse('index:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # to check the views is rendering the right template or not
    # def test_url_view_template_render(self):
    #     url = reverse('index:index')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'index.html')

    def test_view_post_detail_response_200(self):
        url = reverse('index:post-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_view_create_post_login_required(self):
        url = reverse('index:post-create')

        # to login the user for IsAuthenticate permission
        self.client.force_login(self.user)

        response = self.client.post(url, data={'title': 'first_post', 'caption': 'this is first caption'})
        self.assertEqual(response.status_code, 201)
