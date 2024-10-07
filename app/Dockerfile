FROM python:3.11.8-alpine3.19


ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app
RUN apk update && apk add --no-cache xz
RUN apk add python3 python3-dev
RUN apk add --no-cache git
RUN apk add --no-cache fontconfig ttf-dejavu
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg glib gobject-introspection pango pango-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt \
    && apk del .build-deps
ADD . /app/
# Django service
RUN cd /app