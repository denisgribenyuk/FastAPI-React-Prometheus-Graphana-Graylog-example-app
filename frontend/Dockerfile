# develop stage
FROM node:18-alpine AS develop-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# build stage
FROM develop-stage AS build-stage
RUN npm run build
# production stage
FROM nginx:1.15.7-alpine AS production-stage
COPY --from=build-stage /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]