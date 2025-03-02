# Use a lightweight Node.js image
FROM node:16-alpine

# Install 'serve' globally to serve static files
RUN npm install -g serve

# Copy the production build into the container
COPY build /app/build

# Set the working directory
WORKDIR /app

# Expose port 3000
EXPOSE 3000

# Start the static file server to serve the build folder
CMD ["serve", "-s", "build", "-l", "3000"]
