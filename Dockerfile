FROM python:3.8.5-slim

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential software-properties-common

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app/src
COPY ./src .
