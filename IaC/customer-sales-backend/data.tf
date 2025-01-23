data "azurerm_client_config" "current" {}

data "azurerm_container_registry" "cr" {
  name                = var.project_acr_name
  resource_group_name = var.project_resourcegroup_name
}