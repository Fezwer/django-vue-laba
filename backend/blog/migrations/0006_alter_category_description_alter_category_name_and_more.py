# Generated by Django 5.0.6 on 2024-06-26 06:07

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_category_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_approved',
            field=models.BooleanField(default=False, verbose_name='Одобрен'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comment_like', to=settings.AUTH_USER_MODEL, verbose_name='Лайки'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.post', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(upload_to='posts/featured_images/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Избранный'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_like', to=settings.AUTH_USER_MODEL, verbose_name='Лайки'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_at',
            field=models.DateField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='site',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='site',
            name='logo',
            field=models.ImageField(upload_to='site/logo/', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='users/avatars/default.jpg', upload_to='users/avatars/%Y/%m/%d/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(max_length=500, null=True, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='user',
            name='joined_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=30, null=True, verbose_name='Местоположение'),
        ),
        migrations.AlterField(
            model_name='user',
            name='website',
            field=models.CharField(max_length=100, null=True, verbose_name='Веб-сайт'),
        ),
    ]
