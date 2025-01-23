# NOTES

## CMDs

**Build image**

```sh
$ docker build --platform linux/amd64 -t eadbprojectweucr.azurecr.io/restapi:v1-dev -f restapi.Dockerfile ../../customer-sales-backend/restapi
$ docker run --name restapi-container-1 -p 8080:8081 eadbprojectweucr.azurecr.io/restapi:v1-dev
```
```

**Deploy image**

```sh
$ az acr login --name eadbprojectweucr
$ az acr update -n eadbprojectweucr --admin-enabled true
$ docker tag eadbprojectweucr.azurecr.io/restapi:v1-dev eadbprojectweucr.azurecr.io/restapi:v1-dev
$ docker push eadbprojectweucr.azurecr.io/restapi:v1-dev
```

## CI/CD

1. Build image
2. deploy image
3. restart container apps

az containerapp update \
  --name <container-app-name> \
  --resource-group <resource-group-name>


az containerapp update \
  --name eadb-qa-weu-ca \
  --resource-group explore-azure-databricks-be-qa-weu-rg