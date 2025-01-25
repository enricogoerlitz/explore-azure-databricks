resource "azurerm_databricks_workspace" "main" {
  name                = "eadb-${terraform.workspace}-weu-adb"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "premium"

  public_network_access_enabled = true

  custom_parameters {
    virtual_network_id = azurerm_virtual_network.main.id
    public_subnet_name = azurerm_subnet.databricks_public.name
    private_subnet_name = azurerm_subnet.databricks_private.name
    private_subnet_network_security_group_association_id = azurerm_subnet_network_security_group_association.databricks_private_nsg_association.id
    public_subnet_network_security_group_association_id = azurerm_subnet_network_security_group_association.databricks_public_nsg_association.id
  }
}
