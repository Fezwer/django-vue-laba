# Generated by Django 4.0.2 on 2022-02-18 22:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_likes_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comment_like', to=settings.AUTH_USER_MODEL),
        ),
    ]