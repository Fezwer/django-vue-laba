# Используем официальный последний образ nginx
FROM nginx:latest

# Удаляем стандартный файл конфигурации nginx
RUN rm /etc/nginx/conf.d/default.conf

# Копируем наш собственный файл конфигурации nginx в контейнер
COPY nginx.conf /etc/nginx/conf.d

# Копируем содержимое папки dist в стандартную директорию nginx
COPY dist /usr/share/nginx/html

# Указываем порт, который будет использоваться для нашего приложения
EXPOSE 8080

# Это уже для старта
CMD ["nginx", "-g", "daemon off;"]