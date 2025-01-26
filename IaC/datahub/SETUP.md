# SETUP Datahub Infrastructure

## Prerequisites

1. Azure Subscription
2. Resource Group: `<YOUR_RESSOURCE_GROUP>`
3. Storage Account: `<YOUR_BACKEND_STORAGE_ACCOUNT>`
4. Container: `YOUR_BACKEND_STORAGE_ACCOUNT_CONTAINER>`
5. Terraform installed locally ("4.15.0")
6. Visual Studio Code

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
$ alias tfplan='terraform plan -var-file=$(terraform workspace show).tfvars'
$ alias tfapply='terraform apply -var-file=$(terraform workspace show).tfvars -auto-approve'

# Execute cmd
$ tfplan
$ tfapply
```

## Manual Tasks

### 1. Generate Client Secret

1. Go to the registered app
2. Genereate and copy Client Secret Value

### 2. Add Keys to Key Vault

1. `dl-svc-client-secret`
2. `dl-svc-client-id`
3. `tenant-id`

### 3. Setup databricks


1. Create Compute Cluster
2. Create Secret Scope
    - #secrets/createScope
3. Mount datalake containers
4. Setup git integration
    1. DB: User Settings > Linked Accounts > Configure


### 4. Mount or add Data Lake to Databricks
