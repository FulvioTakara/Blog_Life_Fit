from django.db import models

from django.contrib.auth.models import User


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(Base):
    name_cat = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        ordering = ['-id']

    def __str__(self):
        return self.name_cat


class Publication(Base):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    contents = models.TextField()
    excerpt = models.TextField()
    category = models.ForeignKey(
        Category, related_name='publications', on_delete=models.DO_NOTHING, blank=True, null=True)
    image = models.ImageField(
        upload_to='publication_img/%Y/%m/%d', blank=True, null=True)

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
        ordering = ['-id']

    def __str__(self):
        return self.title


class Comment(Base):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    coments = models.TextField()
    publication = models.ForeignKey(
        Publication, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-id']

    def __str__(self):
        return self.name
