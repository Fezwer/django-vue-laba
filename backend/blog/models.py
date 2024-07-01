from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Общая информация для всего сайта
class Site(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    logo = models.ImageField(upload_to='site/logo/', verbose_name='Логотип')

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = '1. Сайты'

    def __str__(self):
        return self.name


# Новая модель пользователя
class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='users/avatars/%Y/%m/%d/', default='users/avatars/default.jpg', verbose_name='Аватар')
    bio = models.TextField(max_length=500, null=True, verbose_name='Биография')
    location = models.CharField(max_length=30, null=True, verbose_name='Местоположение')
    joined_date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = '2. Пользователи'

    def __str__(self):
        return self.username


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(verbose_name='Ссылка')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = '3. Категории'

    def __str__(self):
        return self.name


# Модель тега
class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(verbose_name='Ссылка')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = '4. Теги'

    def __str__(self):
        return self.name


# Модель поста
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='Ссылка')
    content = RichTextField(verbose_name='Содержание')
    featured_image = models.ImageField(
        upload_to='posts/featured_images/%Y/%m/%d/', verbose_name='Изображение')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    is_featured = models.BooleanField(default=False, verbose_name='Избранный')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    modified_at = models.DateField(auto_now=True, verbose_name='Дата изменения')

    # Каждый пост может получать лайки от нескольких пользователей, и каждый пользователь может лайкать несколько постов
    likes = models.ManyToManyField(User, related_name='post_like', verbose_name='Лайки')

    # Каждый пост принадлежит одной категории и имеет много тегов, каждый тег имеет много постов
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    tag = models.ManyToManyField(Tag, verbose_name='Теги')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = '5. Посты'

    def __str__(self):
        return self.title

    def get_number_of_likes(self):
        return self.likes.count()

# Модель комментария
class Comment(models.Model):
    content = models.TextField(max_length=1000, verbose_name='Содержание')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_approved = models.BooleanField(default=True, verbose_name='Одобрен')

    # Каждый комментарий может получать лайки от нескольких пользователей, и каждый пользователь может лайкать несколько комментариев
    likes = models.ManyToManyField(User, related_name='comment_like', verbose_name='Лайки')

    # Каждый комментарий принадлежит одному пользователю и одному посту
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, verbose_name='Пост')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = '6. Комментарии'

    def __str__(self):
        if len(self.content) > 50:
            comment = self.content[:50] + '...'
        else:
            comment = self.content
        return comment

    def get_number_of_likes(self):
        return self.likes.count()

  
