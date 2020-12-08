FROM ubuntu:bionic

LABEL maintainer="beni522@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_DIR /opt/geomex
ENV FLASK_APP ${APP_DIR}/app:create_app()

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3.8 \
    python3.8-dev \
    python3-pip \
    default-libmysqlclient-dev \
    curl \
    python3-setuptools \
    gcc \
&& rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1

RUN curl -sL https://deb.nodesource.com/setup_14.x -o /tmp/setup_14.sh
RUN bash /tmp/setup_14.sh
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y nodejs yarn

COPY ./requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR ${APP_DIR}
COPY ./src .

CMD gunicorn --workers=1 --bind=0.0.0.0:5000 'app:create_app()'
