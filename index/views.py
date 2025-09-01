from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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


class PostCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'post_created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


