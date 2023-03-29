# DOCKER 3
FROM python:3.7-slim
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
ENV PYTHONBUFFERED 1

RUN mkdir /core
WORKDIR /core

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /core/