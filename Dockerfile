FROM python:3.8.3-slim

ENV APP_USER=python

RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}
RUN apt-get update -y

WORKDIR /home/python/app

ADD . ./

RUN apt-get install \
    build-essential \
    software-properties-common \
    python3-pip \
    python3-dev \
    default-libmysqlclient-dev -y
RUN pip3 install --no-cache-dir -r ./requirements.txt
RUN pip3 install pandas pip-upgrader
RUN apt-get purge -y --auto-remove

USER ${APP_USER}:${APP_USER}
