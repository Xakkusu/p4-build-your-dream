# Generated by Django 4.2.17 on 2024-12-18 17:59

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0002_rename_author_buildpost_build_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildpost',
            name='image_alt',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='buildpost',
            name='image_of_build',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='build image'),
        ),
    ]
