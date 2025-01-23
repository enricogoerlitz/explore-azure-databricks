output "main" {
  value = {
    environment         = terraform.workspace
    resource_group_name = azurerm_resource_group.main.name
  }
}
