resource "azuread_application" "dl_svc" {
  display_name                       = "eadb-dl-${terraform.workspace}-app"
}

resource "azuread_service_principal" "dl_svc_sp" {
  client_id = azuread_application.dl_svc.client_id
}

resource "azurerm_role_assignment" "dl_svc_role" {
  principal_id   = azuread_service_principal.dl_svc_sp.object_id
  role_definition_name = "Storage Blob Data Contributor"
  scope          = azurerm_storage_account.dl.id
}
