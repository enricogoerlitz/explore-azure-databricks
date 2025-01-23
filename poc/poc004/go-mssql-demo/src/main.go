// Go connection Sample Code:
package main

import (
	"context"
	"database/sql"
	"fmt"
	"log"

	_ "github.com/microsoft/go-mssqldb"
)

var db *sql.DB
var server = "testing-sql-server-1.database.windows.net"
var port = 1433
var user = "adminuser"
var password = "adminpw1!"
var database = "testing-sql-database-1"

func main() {
	// Build connection string
	connString := fmt.Sprintf("server=%s;user id=%s;password=%s;port=%d;database=%s;",
		server, user, password, port, database)
	// server=testing-sql-server-1.database.windows.net;user id=adminuser;password=adminpw1!;port=1433;database=testing-sql-database-1;
	println(connString)
	var err error
	// Create connection pool
	db, err = sql.Open("sqlserver", connString)
	if err != nil {
		log.Fatal("Error creating connection pool: ", err.Error())
	}
	ctx := context.Background()
	err = db.PingContext(ctx)
	if err != nil {
		log.Fatal(err.Error())
	}
	fmt.Printf("Connected!")
}
