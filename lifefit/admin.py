from atexit import register
from django.contrib import admin

from models import Category, Publication, Comment


@register.admin(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'update',
        'active',
        'name_cat',
    )


@register.admin(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'update',
        'active',
        'title',
        'author',
        'contents',
        'excerpt',
        'category',
        'image',
    )


@register.admin(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'update',
        'active',
        'name',
        'email',
        'contents',
        'publication',
        'author',
    )
