from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Publication, Comment
from .serializers import CategorySerializer, PublicationSerializer, CommentSerializer


"""
API V1
"""


class CategorysAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PublicationsAPIView(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_queryset(self):
        if self.kwargs.get('category_pk'):
            return self.queryset.filter(category_id=self.kwargs.get('category_pk'))
        return self.queryset.all()


class PublicationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_object(self):
        if self.kwargs.get('category_pk'):
            return get_object_or_404(self.get_queryset(), category_id=self.kwargs.get('category_pk'), pk=self.kwargs.get('publication_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('publication_pk'))


class CommentsAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.kwargs.get('publication_pk'):
            return self.queryset.filter(publication_id=self.kwargs.get('publication_pk'))
        return self.queryset.all()


class CommentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_object(self):
        if self.kwargs.get('publication_pk'):
            return get_object_or_404(self.get_queryset(), publication_id=self.kwargs.get('publication_pk'), pk=self.kwargs.get('comment_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('comment_pk'))


"""
API V2
"""


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def publications(self, request, pk=None):
        category = self.get_object()
        serializer = PublicationSerializer(
            category.publications.all(), many=True)
        return Response(serializer.data)


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        publication = self.get_object()
        serializers = CommentSerializer(publication.comments.all(), many=True)
        return Response(serializers.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
