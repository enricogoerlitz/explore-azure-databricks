resource "azurerm_linux_function_app" "productviews" {
  name                       = "productviewsx-${terraform.workspace}-weu-fn"
  location                   = var.westeurope_location
  resource_group_name        = azurerm_resource_group.main.name
  service_plan_id            = azurerm_service_plan.main.id
  storage_account_name       = azurerm_storage_account.main.name
  storage_account_access_key = azurerm_storage_account.main.primary_access_key

  app_settings = {
    "FUNCTIONS_WORKER_RUNTIME"       = "python"
    "PYTHON_VERSION"                 = "3.11"
    "WEBSITE_RUN_FROM_PACKAGE"       = "1"
    "APPINSIGHTS_INSTRUMENTATIONKEY" = azurerm_application_insights.main.instrumentation_key
    "KEYVAULT_URL"                   = azurerm_key_vault.main.vault_uri
    "COSMOS_DB_ENDPOINT"             = azurerm_cosmosdb_account.main.endpoint
  }

  site_config {
    application_stack {
      python_version = "3.11"
    }
    vnet_route_all_enabled = true
  }

  identity {
    type = "SystemAssigned"
  }

  virtual_network_subnet_id = azurerm_subnet.azure_function.id

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}
