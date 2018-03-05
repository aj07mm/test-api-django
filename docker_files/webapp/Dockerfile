#FROM node:7.5
FROM node
ENV LANG C.UTF-8

WORKDIR /django

ADD test_api_django/package.json /django/package.json

# RUN npm install
RUN npm install --save-dev webpack webpack-dev-server yarn
RUN npm install --save-dev webpack-cli -D
#RUN ln -s /node_modules/.bin/ /django/node_modules

#RUN node_modules/.bin/webpack-cli --mode development --profile --json > /test_api_django/webpack-stats.json
#RUN webpack --profile --json > /django/webpack-stats.json
RUN node_modules/.bin/webpack-cli --mode development --profile --json > /django/webpack-stats.json

EXPOSE 8080

#CMD ['npm run dev']
