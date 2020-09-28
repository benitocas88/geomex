FROM ubuntu:bionic

LABEL maintainer="beni522@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    python3.8 \
    python3.8-dev \
    python3-pip \
    default-libmysqlclient-dev \
    build-essential \
    gcc \
    g++ \
    make \
    curl
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

COPY ./requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt

RUN curl -sL https://deb.nodesource.com/setup_12.x -o /tmp/setup_12.sh
RUN bash /tmp/setup_12.sh
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y nodejs yarn

WORKDIR /app/src

CMD gunicorn --workers=1 --bind=0.0.0.0:5000 --thread=1 manage:app
