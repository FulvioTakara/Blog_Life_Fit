from django.urls import path

from .views import (
    CategoryAPIView,
    CategorysAPIView,
    PublicationAPIView,
    PublicationsAPIView,
    CommentAPIView,
    CommentsAPIView,
)

urlpatterns = [
    path('categorys/', CategorysAPIView.as_view(), name='categorys'),
    path('categorys/<int:pk>/', CategoryAPIView.as_view(), name='category'),

    path('categorys/<int:category_pk>/publications',
         PublicationsAPIView.as_view(), name='category_publications'),
    path('categorys/<int:category_pk>/publications/<int:publication_pk>/',
         PublicationAPIView.as_view(), name='category_publication'),

    path('publications/', PublicationsAPIView.as_view(), name='publications'),
    path('publications/<int:publication_pk>/',
         PublicationAPIView.as_view(), name='publication'),

    path('publications/<int:publication_pk>/comments',
         CommentsAPIView.as_view(), name='publication_comments'),
    path('publications/<int:publication_pk>/comments/<int:comment_pk>/',
         CommentAPIView.as_view(), name='publication_comment'),

    path('comments/', CommentsAPIView.as_view(), name='comments'),
    path('comments/<int:comment_pk>/', CommentAPIView.as_view(), name='comment'),
]
