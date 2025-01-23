output "storage_account_name" {
  value = azurerm_storage_account.example.name
}

output "resource_group_name" {
  value = azurerm_resource_group.example.name
}

output "blob_container_name" {
  value = azurerm_storage_container.example.name
}