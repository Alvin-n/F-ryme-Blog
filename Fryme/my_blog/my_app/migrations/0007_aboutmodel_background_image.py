# Generated by Django 3.2.7 on 2021-09-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_aboutmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
    ]
