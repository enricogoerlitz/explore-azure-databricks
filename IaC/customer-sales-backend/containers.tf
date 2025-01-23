resource "azurerm_container_app_environment" "main" {
  name                = "eadb-${terraform.workspace}-weu-cae"
  location            = var.westeurope_location
  resource_group_name = azurerm_resource_group.main.name

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })

  infrastructure_subnet_id   = azurerm_subnet.container_apps_env.id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.main.id
  zone_redundancy_enabled    = false
}

resource "azurerm_container_app" "main" {
  name                         = "eadb-${terraform.workspace}-weu-ca"
  resource_group_name          = azurerm_resource_group.main.name
  container_app_environment_id = azurerm_container_app_environment.main.id

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })

  revision_mode = "Single"

  identity {
    type = "SystemAssigned"
  }

  ingress {
    allow_insecure_connections = false
    external_enabled           = true
    target_port                = 8080
    transport                  = "auto"

    traffic_weight {
      latest_revision = true
      percentage      = 100
    }
  }

  secret {
    name  = "registry-credentials"
    value = data.azurerm_container_registry.cr.admin_password
  }

  registry {
    server               = data.azurerm_container_registry.cr.login_server
    username             = data.azurerm_container_registry.cr.admin_username
    password_secret_name = "registry-credentials"
  }

  template {
    min_replicas = 1
    
    http_scale_rule {
      concurrent_requests = "10"
      name                = "http-scaler"
    }

    container {
      name   = "app"
      image  = "eadbprojectweucr.azurecr.io/restapi:v1-${terraform.workspace}"
      cpu    = 0.5
      memory = "1.0Gi"

      env {
        name  = "MODE"
        value = "release"
      }

      env {
        name  = "KEYVAULT_URL"
        value = azurerm_key_vault.main.vault_uri
      }

      env {
        name  = "DB_USER_KV_SECRET_NAME"
        value = "sql-database-username"
      }

      env {
        name  = "DB_PASSWORD_KV_SECRET_NAME"
        value = "sql-database-password"
      }

      env {
        name  = "DB_HOST"
        value = "${azurerm_mssql_server.main.name}.database.windows.net"
      }

      env {
        name  = "DB_PORT"
        value = "1433"
      }

      env {
        name  = "DB_NAME"
        value = azurerm_mssql_database.main.name
      }
    }
  }
}
