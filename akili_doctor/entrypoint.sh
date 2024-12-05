#!/bin/bash

# Activate virtual environment
source /opt/venv/bin/activate

# Navigate to Django project directory
cd /app

# Run database migrations
python manage.py makemigrations Account articles
python manage.py migrate

# Start Django server in the background
python manage.py runserver 0.0.0.0:8000 &

# Navigate to chatbot directory
cd /app/chatbot

# Start Rasa server
rasa run --enable-api --port 5005 --debug