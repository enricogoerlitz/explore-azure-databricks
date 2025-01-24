# SETUP Backend

## Infrastructure

**RUN terraform commands**
```sh
$ terrafrom init
$ terraform workspace select <env>
$ terraform apply -auto-approve
```

## Azure Functions

**1. Add keys to key vault**

1. `cosmos-db-access-key` => CosmosDB Primary Key
2. `sql-database-username` => SQL Server username
2. `sql-database-password` => SQL Server password

<br>

**2. Deploy Azure Function**
