data "azurerm_client_config" "current" {}

# data "azurerm_cosmosdb_account" "main" {
#   name                = "eadb-${terraform.workspace}-weu-cdb"
#   resource_group_name = azurerm_resource_group.main.name
# }

# data "azurerm_mssql_server" "main" {
#   name                = "eadb-${terraform.workspace}-weu-sqls"
#   resource_group_name = azurerm_resource_group.main.name
# }
