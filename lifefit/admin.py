from django.contrib import admin

from .models import Category, Publication, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'update',
        'active',
        'name_cat',
    )


@admin.register(Publication)
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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'update',
        'active',
        'name',
        'email',
        'coments',
        'publication',
        'author',
    )
