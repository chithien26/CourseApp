# Generated by Django 4.2.11 on 2024-03-31 02:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_tag_active_remove_tag_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='image',
            field=cloudinary.models.CloudinaryField(default=" don't know ", max_length=255, verbose_name='image'),
        ),
    ]
