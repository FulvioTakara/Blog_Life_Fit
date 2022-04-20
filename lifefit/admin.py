from django.contrib import admin

from .models import Categorys, Publications, Comments


@admin.register(Categorys)
class CategorysAdmin(admin.ModelAdmin):
    list_display = (
        'create',
        'update',
        'active',
        'name',
    )


@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
    list_display = (
        'create',
        'update',
        'active',
        'category',
        'image',
        'tittle',
        'abstract',
        'content',
        'author',
    )


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'create',
        'update',
        'active',
        'publication',
        'author',
        'email',
        'comment',
    )
