# Use a full Node base image (not Alpine to avoid native dependency issues)
FROM node:20

# Set working directory inside the container
WORKDIR /app

# Copy only package files first for better Docker caching
COPY package*.json ./

# Install dependencies and ignore optional native build errors (Rollup workaround)
RUN npm install --legacy-peer-deps || true

# Copy the rest of your frontend code
COPY . .

# Expose Vite's dev server port
EXPOSE 5173

# Start the development server
CMD ["npm", "run", "dev"]
