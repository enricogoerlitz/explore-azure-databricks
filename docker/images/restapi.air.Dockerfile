# Start with a Golang base image
FROM golang:1.23.2-alpine

# Set up working directory
WORKDIR /app

# Install dependencies for air and project dependencies
RUN apk add --no-cache curl git && \
    go install github.com/air-verse/air@latest

# Copy go.mod and go.sum files
COPY . /app/
RUN go mod download

# Run Air in development mode
CMD ["air"]