# Используем официальный образ Node.js
FROM node:14

# Устанавливаем рабочую директорию внутри Docker контейнера
WORKDIR /app

# Копируем все файлы проекта внутрь Docker контейнера
COPY . /app/

# Устанавливаем зависимости и собираем проект
RUN npm cache clean --force
RUN npm update -g npm
RUN npm install
RUN npm run build

# Экспортируем порт 8080
EXPOSE 8080

# Запускаем сервер разработки Vue
CMD npm run serve