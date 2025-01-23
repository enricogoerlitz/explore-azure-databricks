# Use an official Golang image as the build stage
FROM golang:1.23.2-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy the Go module files and download the dependencies
COPY . /app/
RUN go mod download

# Copy the rest of the application source code
# COPY ./src /app/src

# Build the Go app (statically linked binary)
RUN go build -o /app/main

# Use a minimal base image for the final container
FROM alpine:latest

# Set the working directory inside the final container
WORKDIR /app

# Copy the built binary from the builder stage
COPY --from=builder /app/main /app/main

# Expose port 8080 (same as the one used in your app)
EXPOSE 8080

# Command to run the binary
CMD ["/app/main"]