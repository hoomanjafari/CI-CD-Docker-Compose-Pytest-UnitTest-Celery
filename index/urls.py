from django.urls import path
from .views import (IndexView, PostDetailView, PostCreateView, TestCeleryTask)


app_name = 'index'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post-create/', PostCreateView.as_view(), name='post-create'),
    path('test-celery/', TestCeleryTask.as_view(), name='test-celery'),
]
