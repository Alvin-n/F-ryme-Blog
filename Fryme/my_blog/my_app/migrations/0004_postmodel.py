# Generated by Django 3.2.7 on 2021-09-20 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0003_auto_20210919_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('head_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('tags', models.CharField(blank=True, max_length=100, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]