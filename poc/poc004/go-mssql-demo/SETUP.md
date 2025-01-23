# Commands to setup GO project

## Prerequisites

**MacBook M2 setup**

```sh
$ pip uninstall pyodbc
$ brew install unixodbc
$ pip install --no-binary :all: pyodbc
$ brew update
$ brew upgrade
$ brew tap microsoft/mssql-release https://github.com/microsoft/homebrew-mssql-release
$ brew update
$ ACCEPT_EULA=Y brew install msodbcsql17
```

**SQL Server Firewall setup (just for testing)**

rule: start=0.0.0.0, end=255.255.255.255

## Commands

```sh
$ go mod init go-mssql-demo
$ go get github.com/denisenkom/go-mssqldb
$ go run src/main.go
```
