# Используем официальный образ Python
FROM python:3.12

# Устанавливаем переменную окружения PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри Docker контейнера
WORKDIR /app

# Копируем файлы зависимостей и устанавливаем их
COPY requirements.txt /app/
RUN pip install django-ckeditor
RUN pip install graphene-file-upload
RUN pip install django-graphql-jwt
RUN pip install django-cors-headers
RUN pip install Pillow 
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта внутрь Docker контейнера
COPY . /app/

# Экспортируем порт 8000
EXPOSE 8000

# Запускаем сервер Django
CMD python manage.py runserver 0.0.0.0:8000