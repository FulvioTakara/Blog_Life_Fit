# Generated by Django 3.2.12 on 2022-04-12 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifefit', '0002_auto_20220412_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categorys'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-id'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-id'], 'verbose_name': 'Publication', 'verbose_name_plural': 'Publications'},
        ),
    ]
