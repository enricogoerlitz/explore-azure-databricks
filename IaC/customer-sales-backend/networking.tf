locals {
  vnet = {
    name = "eadb-${terraform.workspace}-weu-vnet-001"
    subnet_names = {
      container_apps_env = "eadb-cae-${terraform.workspace}-snet"
      azure_function     = "eadb-afn-${terraform.workspace}-snet"
      keyvault_pe        = "eadb-kvpe-${terraform.workspace}-snet"
      cosmosdb_pe        = "eadb-cdbpe-${terraform.workspace}-snet"
      sql_server_pe      = "eadb-sqls-${terraform.workspace}-snet"
    }
    env = {
      dev = {
        vnet_address_space = ["10.0.0.0/22"]
        subnet_address_spaces = {
          container_apps_env = ["10.0.0.0/23"]
          azure_function     = ["10.0.2.0/28"]
          keyvault_pe        = ["10.0.2.16/29"]
          cosmosdb_pe        = ["10.0.2.24/29"]
          sql_server_pe      = ["10.0.2.32/29"]
        }
      }
      qa = {
        vnet_address_space = ["10.0.4.0/22"]
        subnet_address_spaces = {
          container_apps_env = ["10.0.4.0/23"]
          azure_function     = ["10.0.6.0/28"]
          keyvault_pe        = ["10.0.6.16/29"]
          cosmosdb_pe        = ["10.0.6.24/29"]
          sql_server_pe      = ["10.0.6.32/29"]
        }
      }
      prod = {
        vnet_address_space = ["10.0.8.0/22"]
        subnet_address_spaces = {
          container_apps_env = ["10.0.8.0/23"]
          azure_function     = ["10.0.10.0/28"]
          keyvault_pe        = ["10.0.10.16/29"]
          cosmosdb_pe        = ["10.0.10.24/29"]
          sql_server_pe      = ["10.0.10.32/29"]
        }
      }
    }
  }

}

resource "azurerm_virtual_network" "main" {
  name                = local.vnet.name
  location            = var.westeurope_location
  resource_group_name = azurerm_resource_group.main.name
  address_space       = local.vnet.env[terraform.workspace].vnet_address_space

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}

resource "azurerm_network_security_group" "default_private_nsg" {
  name                = "eadb-dflt-pvt-${terraform.workspace}-nsg"
  location            = var.westeurope_location
  resource_group_name = azurerm_resource_group.main.name

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}

resource "azurerm_network_security_group" "https_nsg" {
  name                = "eadb-https-${terraform.workspace}-nsg"
  location            = var.westeurope_location
  resource_group_name = azurerm_resource_group.main.name

  security_rule {
    name                       = "Allow-HTTPS-Inbound"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "443"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  security_rule {
    name                       = "Allow-HTTPS-Outbound"
    priority                   = 101
    direction                  = "Outbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "443"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  tags = merge(var.default_tags, {
    "env" = terraform.workspace
  })
}

resource "azurerm_subnet" "azure_function" {
  name                 = local.vnet.subnet_names.azure_function
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = local.vnet.env[terraform.workspace].subnet_address_spaces.azure_function
  service_endpoints    = ["Microsoft.KeyVault", "Microsoft.AzureCosmosDB"]

  delegation {
    name = "web_server_farms"
    service_delegation {
      name = "Microsoft.Web/serverFarms"
      actions = [
        "Microsoft.Network/virtualNetworks/subnets/action",
      ]
    }
  }
}

resource "azurerm_subnet_network_security_group_association" "azure_function_nsg_association" {
  subnet_id                 = azurerm_subnet.azure_function.id
  network_security_group_id = azurerm_network_security_group.default_private_nsg.id
}

resource "azurerm_subnet" "keyvault_pe" {
  name                 = local.vnet.subnet_names.keyvault_pe
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = local.vnet.env[terraform.workspace].subnet_address_spaces.keyvault_pe
  service_endpoints    = ["Microsoft.KeyVault"]
}

resource "azurerm_subnet_network_security_group_association" "keyvault_pe_nsg_association" {
  subnet_id                 = azurerm_subnet.keyvault_pe.id
  network_security_group_id = azurerm_network_security_group.default_private_nsg.id
}

resource "azurerm_subnet" "cosmosdb_pe" {
  name                 = local.vnet.subnet_names.cosmosdb_pe
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = local.vnet.env[terraform.workspace].subnet_address_spaces.cosmosdb_pe
  service_endpoints    = ["Microsoft.AzureCosmosDB"]
}

resource "azurerm_subnet_network_security_group_association" "cosmosdb_pe_nsg_association" {
  subnet_id                 = azurerm_subnet.cosmosdb_pe.id
  network_security_group_id = azurerm_network_security_group.default_private_nsg.id
}

resource "azurerm_subnet" "sql_server_pe" {
  name                 = local.vnet.subnet_names.sql_server_pe
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = local.vnet.env[terraform.workspace].subnet_address_spaces.sql_server_pe
  service_endpoints    = ["Microsoft.Sql"]
}

resource "azurerm_subnet_network_security_group_association" "sql_server_pe_nsg_association" {
  subnet_id                 = azurerm_subnet.sql_server_pe.id
  network_security_group_id = azurerm_network_security_group.default_private_nsg.id
}

resource "azurerm_subnet" "container_apps_env" {
  name                 = local.vnet.subnet_names.container_apps_env
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = local.vnet.env[terraform.workspace].subnet_address_spaces.container_apps_env
  service_endpoints    = []
}

resource "azurerm_subnet_network_security_group_association" "container_apps_env_nsg_association" {
  subnet_id                 = azurerm_subnet.container_apps_env.id
  network_security_group_id = azurerm_network_security_group.https_nsg.id
}
