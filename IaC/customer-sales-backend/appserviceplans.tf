resource "azurerm_service_plan" "main" {
  name                = "productviews-${terraform.workspace}-weu-asp"
  location            = var.westeurope_location
  resource_group_name = azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = var.app_service_plan_sku_name

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}
