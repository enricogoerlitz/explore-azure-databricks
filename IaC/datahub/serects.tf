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

# resource "azurerm_key_vault_access_policy" "me_kv_access_policy" {
#   key_vault_id = azurerm_key_vault.main.id
#   tenant_id    = data.azurerm_client_config.current.tenant_id
#   object_id    = data.azurerm_client_config.current.object_id

#   secret_permissions = [
#     "Get",
#     "List",
#     "Set",
#     "Delete",
#     "Recover",
#     "Backup",
#     "Restore"
#   ]
# }

# resource "azurerm_key_vault_access_policy" "app_kv_access_policy" {
#   key_vault_id = azurerm_key_vault.main.id
#   tenant_id    = data.azurerm_client_config.current.tenant_id
#   object_id    = azuread_service_principal.dl_svc_sp.object_id

#   secret_permissions = [
#     "Get",
#     "List"
#   ]
# }
