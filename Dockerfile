FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk add --no-cache \
    gcc \
    libc-dev \
    linux-headers \
    libffi-dev \
    openssl-dev \
    build-base

# Create and activate virtual environment
RUN python -m venv /py
ENV PATH="/py/bin:$PATH"

# Upgrade pip and install dependencies
RUN /py/bin/pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN /py/bin/pip install -r /requirements.txt

# Set working directory and copy the application code
COPY ./app /app
WORKDIR /app
