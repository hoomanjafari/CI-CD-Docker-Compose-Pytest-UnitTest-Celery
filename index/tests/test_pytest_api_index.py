import pytest

from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def common_user():
    return User.objects.create_user(username='test_1', email='test_1@email.com', password='test_1WQ')


@pytest.mark.django_db
class TestIndexApi:

    def test_post_get_response_200_status(self, client, common_user):
        url = reverse('index:index')
        response = client.get(url)
        assert response.status_code == 200

    def test_post_create_response_201_status(self, client, common_user):
        url = reverse('index:post-create')
        data = {
            'title': 'pytest_1',
            'caption': 'pytest_1',
        }
        client.force_login(user=common_user)
        response = client.post(url, data=data)
        assert response.status_code == 201

    def test_post_valid_data_400_status(self, client, common_user):
        url = reverse('index:post-create')
        data = {
            'title': 'pytest_1',
        }
        client.force_authenticate(user=common_user)
        response = client.post(url, data=data)
        assert response.status_code == 400
