FROM node:latest

WORKDIR /frontend

COPY ./frontend /frontend

RUN npm install

RUN npm run build

CMD ["npm", "run", "serve"]