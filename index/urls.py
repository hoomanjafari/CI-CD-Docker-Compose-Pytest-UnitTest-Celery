from django.urls import path
from .views import (IndexView, PostDetailView)


app_name = 'index'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
