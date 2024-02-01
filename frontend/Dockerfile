FROM node:20.11-alpine

WORKDIR /frontend

COPY ./frontend /frontend

RUN npm install

RUN npm run build



CMD ["npm", "run", "serve"]