FROM ubuntu:jammy-20221130

LABEL maintainer="beni522@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /home/userapp
ENV PYTHONPATH $APP_ROOT/src
ENV PATH $APP_ROOT/src/static/node_modules/.bin:$APP_ROOT/.local/bin:$PATH

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    curl \
&& rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

RUN curl -fsSL https://deb.nodesource.com/setup_19.x -o /tmp/setup_19.sh
RUN bash /tmp/setup_19.sh
RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | tee /usr/share/keyrings/yarnkey.gpg >/dev/null
RUN echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y nodejs yarn

RUN useradd userapp -ms /bin/bash
USER userapp

COPY ./requirements /opt/requirements
RUN python -m pip install -U pip --disable-pip-version-check && python -m pip install --no-cache-dir pip-tools
RUN pip-sync /opt/requirements/base.txt --pip-args "--no-cache-dir --no-deps"

WORKDIR $APP_ROOT/src
COPY --chown=userapp:userapp ./src .

# USER root
# RUN apt-mark hold procps dnsutils curl libcurl4 libcurl4-openssl-dev librtmp1 nginx
# RUN apt-get autoremove --purge --allow-remove-essential -y build-essential gpgv
# USER userapp

CMD gunicorn --workers=1 --bind=0.0.0.0:5000 "app:create_app()"
