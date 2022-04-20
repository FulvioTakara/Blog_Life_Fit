from django.db import models
from django.contrib.auth.models import User


class Base:
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Categorys(Base):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'


class Publications(Base):
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_img/%Y/%m/%d',
                              width_field=200, height_field=150, blank=True, null=True)
    tittle = models.CharField(max_length=255)
    abstract = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'


class Comments(Base):
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email = models.EmailField()
    comment = models.TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
