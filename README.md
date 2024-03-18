# Telegram Funnel
Userbot-воронка для отправки сообщений пользователю telegram в рамках определенных интервалов.

### Stack:
- Python;
- SQLAlchemy;
- PostgreSQL;
- Alembic;
- Pyrogram.

### Установка и запуск:
- git clone https://github.com/Idvri/Telegram_Funnel.git - клонируем проект к себе в нужную директорию;
- python -m venv env - создаем вирт. окружение;
- venv/Scripts/activate (Windows) | source venv/bin/activate (Linux) - запускаем вирт. окружение;
- pip install -r requirements.txt - устанавливаем зависимости;
- touch .env - создаем файл для указания переменных окружения, согласно примеру (.env.example);
- alembic upgrade head - делаем миграции;
- python main.py - запускаем проект.

### Ссылки:
- https://my.telegram.org/ - создание своего API;
- https://t.me/BotFather - создание своего бота.

### Доступность:
- https://t.me/pyrogram_idvri_bot - мой бот (сейчас проект запущен).

### Функционал:
- проверка "готовых для получения сообщения" пользователей согласно статусу воронки;
- запись в БД статусов воронки;
- изменение статуса воронки в случае получения сообщений с наличием слов-триггеров либо окончания воронки;
- отправка сообщений пользователям согласно условиям.