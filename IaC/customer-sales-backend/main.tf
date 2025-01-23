resource "azurerm_resource_group" "main" {
  name     = "explore-azure-databricks-be-${terraform.workspace}-weu-rg"
  location = var.westeurope_location

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })

  lifecycle {
    precondition {
      condition = contains(
        ["dev", "qa", "prod"],
        terraform.workspace
      )
      error_message = "The workspace (env) should be either dev, qa, or prod."
    }
  }
}
