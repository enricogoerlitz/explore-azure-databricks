# Customer Sales Backend

## Setup

```sh
$ go mod init customer-sales-backend
$ go mod tidy
$ go get github.com/denisenkom/go-mssqldb
$ go get gorm.io/driver/sqlserver
$ go get github.com/gin-gonic/gin
$ go get gorm.io/gorm
$ go get github.com/sirupsen/logrus
```

$ go run src/main.go
```


This is a REST API project for managing customer sales using Go, Gin, and GORM.

## Project Structure

```
customer-sales-backend
├── src
│   ├── controllers
│   │   └── customer_controller.go
│   ├── models
│   │   └── customer.go
│   ├── routes
│   │   └── routes.go
│   ├── services
│   │   └── customer_service.go
│   ├── main.go
│   └── database
│       └── connection.go
├── go.mod
├── go.sum
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd customer-sales-backend
   ```

2. Install dependencies:
   ```
   go mod tidy
   ```

3. Set up your database and update the connection settings in `src/database/connection.go`.

4. Run the application:
   ```
   go run src/main.go
   ```

## Usage

The API provides endpoints for managing customers. Below are the available endpoints:

- **Create Customer**: `POST /customers`
- **Get Customer**: `GET /customers/:id`
- **Update Customer**: `PUT /customers/:id`
- **Delete Customer**: `DELETE /customers/:id`

## API Endpoints

Refer to the documentation for detailed information on request and response formats for each endpoint.