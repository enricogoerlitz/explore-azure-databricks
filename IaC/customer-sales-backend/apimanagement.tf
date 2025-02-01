# disabled, because it spends to much time

# resource "azurerm_api_management" "main" {
#   name                = "eadb-${terraform.workspace}-weu-apim"
#   location            = var.westeurope_location
#   resource_group_name = azurerm_resource_group.main.name
#   publisher_name      = "Enrico Goerlitz"
#   publisher_email     = "rico.goerlitz@gmail.com"
#   sku_name            = var.api_management_sku_name

#   tags = merge(var.default_tags, {
#     "env" = terraform.workspace
#   })

#   notification_sender_email = "rico.goerlitz@gmail.com"

# }

# resource "azurerm_api_management_api" "product_views_api" {
#   name                = "product-views-api"
#   resource_group_name = azurerm_resource_group.main.name
#   api_management_name = azurerm_api_management.main.name
#   revision            = "1"
#   display_name        = "Product Views API"
#   path                = "product-views"
#   protocols           = ["https"]

#   import {
#     content_format = "swagger-link-json"
#     content_value  = "https://${azurerm_linux_function_app.productviews.default_hostname}/api/swagger.json"
#   }
# }

# resource "azurerm_api_management_api" "customer_sales_api" {
#   name                = "customer-sales-api"
#   resource_group_name = azurerm_resource_group.main.name
#   api_management_name = azurerm_api_management.main.name
#   revision            = "1"
#   display_name        = "Customer Sales API"
#   path                = "customersales"
#   protocols           = ["https"]

#   import {
#     content_format = "swagger-link-json"
#     content_value  = "https://${azurerm_container_app.main.latest_revision_fqdn}/swagger.json"
#   }
# }
