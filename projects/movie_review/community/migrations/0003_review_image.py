# Generated by Django 3.1.2 on 2020-10-08 05:21

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20201008_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='%Y/%m/%d'),
        ),
    ]
