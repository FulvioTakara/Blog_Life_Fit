from rest_framework import serializers
from .models import Category, Publication, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name_cat',
            'created',
            'active',
        )


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = (
            'id',
            'title',
            'contents',
            'excerpt',
            'category',
            'author',
            'image',
            'created',
            'active',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kargs = {
            'email': {'write_olny': True}
        }
        model = Comment
        fields = (
            'id',
            'name',
            'email',
            'coments',
            'publication',
            'author',
            'created',
            'active',
        )
