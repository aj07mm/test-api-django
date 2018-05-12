FROM python:3.6
ENV LANG C.UTF-8

RUN mkdir /django
WORKDIR /django

RUN apt-get -y update

RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y python-psycopg2 postgresql-contrib build-essential

ADD requirements.txt /django/requirements.txt

RUN pip install -r requirements.txt --default-timeout=100

EXPOSE 8000
