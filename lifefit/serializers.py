from numbers import Real
from rest_framework import serializers
from .models import Category, Publication, Comment


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


class PublicationSerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail'
    )

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
            'comments',
        )


class CategorySerializer(serializers.ModelSerializer):
    publications = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='publication-detail',
    )

    class Meta:
        model = Category
        fields = (
            'id',
            'name_cat',
            'created',
            'active',
            'publications',
        )
