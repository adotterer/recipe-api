FROM python:3.7-alpine
MAINTAINER Andrew Dotterer

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
