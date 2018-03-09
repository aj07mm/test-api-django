FROM node
ENV LANG C.UTF-8

WORKDIR /django

ADD test_api_django/package.json /django/package.json

RUN npm install

EXPOSE 3000
