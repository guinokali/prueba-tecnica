#STEP 1 BUILD OF REACT PROJECT
FROM node:alpine AS build
WORKDIR /react-testing-demo
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build

#STEP 2 CREATE NGINX SERVER
FROM nginx:alpine AS prod-stage
COPY --from=build /react-testing-demo/app/build /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx","-g","daemon off"]