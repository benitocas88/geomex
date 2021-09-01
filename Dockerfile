FROM ubuntu:hirsute

LABEL maintainer="beni522@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /home/userapp
ENV PATH $APP_ROOT/src/static/node_modules/.bin:$APP_ROOT/.local/bin:$PATH

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3.9 \
    python3.9-dev \
    python3-pip \
    default-libmysqlclient-dev \
    curl \
    python3-setuptools \
    gcc \
    libffi-dev \
&& rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1

RUN curl -fsSL https://deb.nodesource.com/setup_16.x -o /tmp/setup_16.sh
RUN bash /tmp/setup_16.sh
RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | tee /usr/share/keyrings/yarnkey.gpg >/dev/null
RUN echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y nodejs yarn

COPY ./requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR $APP_ROOT/src
COPY ./src .

CMD gunicorn --workers=1 --bind=0.0.0.0:5000 'app:create_app()'
