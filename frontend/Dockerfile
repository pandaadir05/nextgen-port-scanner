# frontend/Dockerfile
FROM node:16-alpine

# Install 'serve' globally to serve static files
RUN npm install -g serve

# Copy the production build (make sure to build before building the Docker image)
COPY build /app/build

WORKDIR /app

EXPOSE 3000

# Serve the build directory on port 3000
CMD ["serve", "-s", "build", "-l", "3000"]
