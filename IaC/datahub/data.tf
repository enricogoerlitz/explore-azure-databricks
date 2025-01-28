data "azurerm_client_config" "current" {}

data "azurerm_cosmosdb_account" "main" {
  name                = "eadb-${terraform.workspace}-weu-cdb"
  resource_group_name = "explore-azure-databricks-be-${terraform.workspace}-weu-rg"
}
