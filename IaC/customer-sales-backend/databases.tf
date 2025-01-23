resource "azurerm_cosmosdb_account" "main" {
  name                = "eadb-${terraform.workspace}-weu-cdb"
  location            = var.westeurope_location
  resource_group_name = azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"

  consistency_policy {
    consistency_level = "Session"
  }

  geo_location {
    location          = var.westeurope_location
    failover_priority = 0
  }

  capabilities {
    name = "EnableServerless"
  }

  public_network_access_enabled = false

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}

resource "azurerm_cosmosdb_sql_database" "customer_sales" {
  name                = "CustomerSales"
  resource_group_name = azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
}

resource "azurerm_cosmosdb_sql_container" "product_views" {
  name                = "ProductViews"
  resource_group_name = azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
  database_name       = azurerm_cosmosdb_sql_database.customer_sales.name
  partition_key_paths = ["/product_id"]
}

resource "azurerm_mssql_server" "main" {
  name                          = "eadb-${terraform.workspace}-weu-sqls"
  resource_group_name           = azurerm_resource_group.main.name
  location                      = var.westeurope_location
  version                       = "12.0"
  administrator_login           = var.db_sa_username
  administrator_login_password  = var.db_sa_password
  public_network_access_enabled = false

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}

resource "azurerm_mssql_database" "main" {
  name                 = "customersales"
  server_id            = azurerm_mssql_server.main.id
  max_size_gb          = 10
  storage_account_type = "Local"

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}
