# SETUP Backend Infrastructure

## Prerequisites

1. Azure Subscription
2. Resource Group: `<YOUR_RESSOURCE_GROUP>`
3. Storage Account: `<YOUR_BACKEND_STORAGE_ACCOUNT>`
4. Container: `YOUR_BACKEND_STORAGE_ACCOUNT_CONTAINER>`
5. Container Registry: `YOUR_CONTAINER_REGISTRY>`
6. Terraform installed locally ("4.15.0")
7. Visual Studio Code
    - Extensions: Azure Functions; Azure Resources

## Build Infrastructure

### Run Terraform Commands

```sh
# Setup terraform
$ terraform init
$ terraform workspace new dev
$ terraform workspace new qa
$ terraform workspace new prod
$ terraform workspace select dev

# Generate an session alias for easy terraform cmd management
$ alias tfplan='terraform plan -var-file=$(terraform workspace show).tfvars -var="db_sa_username=<YOUR_DB_USERNAME>" -var="db_sa_password=<YOUR_DB_PASSWORD>!"'
$ alias tfapply='terraform apply -var-file=$(terraform workspace show).tfvars -var="db_sa_username=adminuser" -var="db_sa_password=adminpw1!" -auto-approve'

# Execute cmd
$ tfplan
$ tfapply
```

## Manual Tasks

### 1. Add Keys to Key Vault

1. `cosmos-db-access-key` => CosmosDB Primary Key
2. `sql-database-username` => SQL Server username
3. `sql-database-password` => SQL Server password

### 2. Deploy Azure Function

1. Open Azure Function in an dedicated VS Code Window
2. Go to Azure Tab
3. Select deployed Azure Function
4. Click: Deploy Azure Function

### 3. Create API Management (if not managed by terraform)

Add two APIs:
1. Azure Function: /product-views
2. Container Apps: /customersales

### 4. DNS Mapping

Add the API Management endpoint to Route 53.

[🔗 How to configure an Curstom Domain](https://learn.microsoft.com/en-us/azure/app-service/manage-custom-dns-migrate-domain#1-get-a-domain-verification-id)

