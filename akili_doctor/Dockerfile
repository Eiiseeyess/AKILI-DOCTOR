# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1
ENV VIRTUAL_ENV=/opt/venv

# Create and set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python3.9 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Upgrade pip
RUN pip install --upgrade pip

# Copy project files
COPY . /app/

# Install Python dependencies
RUN pip install -r requirements.txt

# Install Rasa
RUN pip install rasa

# Train Rasa model
WORKDIR /app/chatbot
RUN rasa train

# Expose ports for Django and Rasa servers
EXPOSE 8000 5005

# Create a script to run both servers
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]