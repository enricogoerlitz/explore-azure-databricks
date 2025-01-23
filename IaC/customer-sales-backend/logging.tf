resource "azurerm_log_analytics_workspace" "main" {
  name                = "eadb-${terraform.workspace}-weu-laws"
  location            = var.westeurope_location
  resource_group_name = azurerm_resource_group.main.name
  sku                 = "PerGB2018"
  retention_in_days   = 30

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}

resource "azurerm_application_insights" "main" {
  name                = "eadb-${terraform.workspace}-weu-ai"
  location            = var.westeurope_location
  resource_group_name = azurerm_resource_group.main.name
  application_type    = "web"
  workspace_id        = azurerm_log_analytics_workspace.main.id

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}
