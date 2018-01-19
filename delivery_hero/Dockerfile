FROM python:3.6
ENV LANG C.UTF-8

RUN mkdir /django

RUN apt-get -y update
RUN apt-get install -y python-psycopg2

ADD requirements.txt /django/requirements.txt
RUN pip install -r /django/requirements.txt

WORKDIR /django

EXPOSE 8000
