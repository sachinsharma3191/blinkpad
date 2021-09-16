FROM node:lts-alpine
#RUN npm install -g http-server
WORKDIR /app
EXPOSE 8080
COPY package*.json ./
RUN npm install
COPY . .
#RUN npm run build
# start app
CMD ["npm", "run", "serve"]