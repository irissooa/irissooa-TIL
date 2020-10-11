# Generated by Django 3.1.2 on 2020-10-08 01:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like_comment',
            field=models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='like',
            field=models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]