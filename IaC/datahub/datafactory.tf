resource "azurerm_data_factory" "main" {
  name                = "eadb-${terraform.workspace}-weu-adf"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  github_configuration {
    account_name    = "enricogoerlitz"
    repository_name = "explore-azure-databricks-project"
    branch_name     = "dev"
    root_folder     = "/datahub/ADF"
  }
}