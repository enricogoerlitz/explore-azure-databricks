resource "random_string" "kv_name" {
  length  = 6
  lower   = true
  upper   = false
  special = false
  numeric = false
}

resource "azurerm_key_vault" "main" {
  name                       = "eadb-${random_string.kv_name.id}-${terraform.workspace}-weu-kv"
  location                   = var.westeurope_location
  resource_group_name        = azurerm_resource_group.main.name
  tenant_id                  = data.azurerm_client_config.current.tenant_id
  sku_name                   = "standard"
  soft_delete_retention_days = 7

  public_network_access_enabled = false

  # Enable Azure RBAC for access control
  enable_rbac_authorization = false
  purge_protection_enabled  = true

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}

resource "azurerm_role_assignment" "me_kv_administrator" {
  scope                = azurerm_key_vault.main.id
  role_definition_name = "Key Vault Administrator"
  principal_id         = data.azurerm_client_config.current.object_id
}
