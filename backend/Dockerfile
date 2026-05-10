FROM node:20-alpine
RUN apk add --no-cache openssl
WORKDIR /app
COPY package*.json ./
RUN npm config set fetch-retry-maxtimeout 600000 && \
    npm install --no-audit --no-fund --legacy-peer-deps
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
