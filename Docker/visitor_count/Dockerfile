FROM node:alpine

WORKDIR /usr/app

COPY package.json .

#This is practically the same as pip install -r requirements
RUN npm install

COPY . .

CMD ["npm","start"]