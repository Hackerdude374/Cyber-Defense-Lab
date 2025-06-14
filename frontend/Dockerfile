# Use official Node.js image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy all other frontend files
COPY . .

# Expose port Vite uses
EXPOSE 5173

# Start dev server
CMD ["npm", "run", "dev"]
