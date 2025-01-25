resource "azurerm_storage_account" "dl" {
  name                            = "eadbdl${terraform.workspace}weusa"
  resource_group_name             = azurerm_resource_group.main.name
  location                        = var.westeurope_location
  account_tier                    = "Standard"
  account_replication_type        = "LRS"
  is_hns_enabled                  = true
  allow_nested_items_to_be_public = false
  public_network_access_enabled   = false


  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}

resource "azurerm_storage_account" "metadata" {
  name                            = "eadbmd${terraform.workspace}weusa"
  resource_group_name             = azurerm_resource_group.main.name
  location                        = var.westeurope_location
  account_tier                    = "Standard"
  account_replication_type        = "LRS"
  is_hns_enabled                  = true
  allow_nested_items_to_be_public = false
  public_network_access_enabled   = true


  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}

resource "azurerm_storage_container" "gold" {
  name                  = "gold"
  storage_account_id    = azurerm_storage_account.dl.id
  container_access_type = "private"
}

resource "azurerm_storage_container" "silver" {
  name                  = "silver"
  storage_account_id    = azurerm_storage_account.dl.id
  container_access_type = "private"
}

resource "azurerm_storage_container" "bronze" {
  name                  = "bronze"
  storage_account_id    = azurerm_storage_account.dl.id
  container_access_type = "private"
}

resource "azurerm_storage_container" "metadata" {
  name                  = "datahub-metadata"
  storage_account_id    = azurerm_storage_account.metadata.id
  container_access_type = "private"
}
