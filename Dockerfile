FROM ubuntu:bionic

LABEL maintainer="beni522@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    software-properties-common \
    build-essential \
    gcc \
    g++ \
    make \
    curl \
    python3.8 \
    python3.8-dev \
    python3-pip \
    default-libmysqlclient-dev
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1

RUN curl -sL https://deb.nodesource.com/setup_12.x -o /tmp/setup_12.sh
RUN bash /tmp/setup_12.sh
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y nodejs yarn

COPY ./requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app/src
COPY ./src/wsgi.py .

CMD gunicorn -c wsgi.py manage:app
