from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer


class IndexView(APIView):
    def get(self, request):
        return Response({
            'detail': 'Ok',
        }, status=status.HTTP_200_OK)


class PostDetailView(APIView):
    def get(self, request, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        serializer = PostSerializer(instance=post)
        return Response(serializer.data, status=status.HTTP_200_OK)
