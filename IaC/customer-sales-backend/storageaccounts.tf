resource "azurerm_storage_account" "main" {
  name                            = "exploreadb${terraform.workspace}weusa"
  resource_group_name             = azurerm_resource_group.main.name
  location                        = var.westeurope_location
  account_tier                    = "Standard"
  account_replication_type        = "LRS"
  is_hns_enabled                  = true
  allow_nested_items_to_be_public = false

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}

resource "azurerm_storage_container" "monitoring" {
  name                  = "monitoring"
  storage_account_id    = azurerm_storage_account.main.id
  container_access_type = "private"
}

resource "azurerm_storage_container" "functions" {
  name                  = "functions"
  storage_account_id    = azurerm_storage_account.main.id
  container_access_type = "private"
}
