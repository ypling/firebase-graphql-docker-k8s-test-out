FROM node:22-slim

# Create app directory
WORKDIR /usr/app

ARG node_env=production

ENV NODE_ENV $node_env

COPY package*.json /usr/app/
RUN npm install

COPY . /usr/app/
CMD node index.js