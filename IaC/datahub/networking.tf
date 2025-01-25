locals {
  vnet = {
    name = "eadb-${terraform.workspace}-weu-vnet-002"
    subnet_names = {
      keyvault_pe   = "eadb-kvpe-${terraform.workspace}-snet"
      datalake_pe   = "eadb-dlpe-${terraform.workspace}-snet"
      cosmosdb_pe   = "eadb-cdbpe-${terraform.workspace}-snet"
      sql_server_pe = "eadb-sqls-${terraform.workspace}-snet"
      databricks_private = "eadb-adb-pvt-${terraform.workspace}-snet"
      databricks_public = "eadb-adb-pub-${terraform.workspace}-snet"
    }
    env = {
      dev = {
        vnet_address_space = ["10.0.12.0/26"]
        subnet_address_spaces = {
          keyvault_pe   = ["10.0.12.0/29"]
          cosmosdb_pe   = ["10.0.12.8/29"]
          sql_server_pe = ["10.0.12.16/29"]
          datalake_pe   = ["10.0.12.24/29"]
          databricks_private = ["10.0.12.32/28"]
          databricks_public = ["10.0.12.48/28"]
        }
      }
      # qa = {
      #   vnet_address_space = ["10.0.4.0/22"]
      #   subnet_address_spaces = {
      #     keyvault_pe        = ["10.0.6.16/29"]
      #     cosmosdb_pe        = ["10.0.6.24/29"]
      #     sql_server_pe      = ["10.0.6.32/29"]
      #   }
      # }
      # prod = {
      #   vnet_address_space = ["10.0.8.0/22"]
      #   subnet_address_spaces = {
      #     keyvault_pe        = ["10.0.10.16/29"]
      #     cosmosdb_pe        = ["10.0.10.24/29"]
      #     sql_server_pe      = ["10.0.10.32/29"]
      #   }
      # }
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

resource "azurerm_network_security_group" "databricks_public_nsg" {
  name                = "databricks-public-nsg"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  security_rule {
    name                       = "AllowInternetOutbound"
    priority                   = 100
    direction                  = "Outbound"
    access                     = "Allow"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "Internet"
  }

  security_rule {
    name                       = "AllowAzureLoadBalancerInbound"
    priority                   = 200
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "AzureLoadBalancer"
    destination_address_prefix = "*"
  }

  security_rule {
    name                       = "DenyAllInbound"
    priority                   = 300
    direction                  = "Inbound"
    access                     = "Deny"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}


resource "azurerm_network_security_group" "databricks_private_nsg" {
  name                = "databricks-private-nsg"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  security_rule {
    name                       = "AllowDatabricksControlPlane"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "AzureDatabricks"
    destination_address_prefix = "*"
  }

  security_rule {
    name                       = "AllowPrivateOutbound"
    priority                   = 200
    direction                  = "Outbound"
    access                     = "Allow"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "VirtualNetwork"
  }

  security_rule {
    name                       = "DenyAllInbound"
    priority                   = 300
    direction                  = "Inbound"
    access                     = "Deny"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
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

# resource "azurerm_subnet" "cosmosdb_pe" {
#   name                 = local.vnet.subnet_names.cosmosdb_pe
#   resource_group_name  = azurerm_resource_group.main.name
#   virtual_network_name = azurerm_virtual_network.main.name
#   address_prefixes     = local.vnet.env[terraform.workspace].subnet_address_spaces.cosmosdb_pe
#   service_endpoints    = ["Microsoft.AzureCosmosDB"]
# }

# resource "azurerm_subnet_network_security_group_association" "cosmosdb_pe_nsg_association" {
#   subnet_id                 = azurerm_subnet.cosmosdb_pe.id
#   network_security_group_id = azurerm_network_security_group.default_private_nsg.id
# }

# resource "azurerm_subnet" "sql_server_pe" {
#   name                 = local.vnet.subnet_names.sql_server_pe
#   resource_group_name  = azurerm_resource_group.main.name
#   virtual_network_name = azurerm_virtual_network.main.name
#   address_prefixes     = local.vnet.env[terraform.workspace].subnet_address_spaces.sql_server_pe
#   service_endpoints    = ["Microsoft.Sql"]
# }

# resource "azurerm_subnet_network_security_group_association" "sql_server_pe_nsg_association" {
#   subnet_id                 = azurerm_subnet.sql_server_pe.id
#   network_security_group_id = azurerm_network_security_group.default_private_nsg.id
# }

resource "azurerm_subnet" "datalake_pe" {
  name                 = local.vnet.subnet_names.datalake_pe
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = local.vnet.env[terraform.workspace].subnet_address_spaces.datalake_pe
  service_endpoints    = ["Microsoft.Storage"]
}

resource "azurerm_subnet_network_security_group_association" "datalake_pe_nsg_association" {
  subnet_id                 = azurerm_subnet.datalake_pe.id
  network_security_group_id = azurerm_network_security_group.default_private_nsg.id
}

resource "azurerm_subnet" "databricks_private" {
  name                 = local.vnet.subnet_names.databricks_private
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = local.vnet.env[terraform.workspace].subnet_address_spaces.databricks_private

  delegation {
    name = "databricks_workspaces_delegation"
    service_delegation {
      name = "Microsoft.Databricks/workspaces"
      actions = [
        "Microsoft.Network/virtualNetworks/subnets/action",
        "Microsoft.Network/virtualNetworks/subnets/join/action",
        "Microsoft.Network/virtualNetworks/subnets/prepareNetworkPolicies/action",
        "Microsoft.Network/virtualNetworks/subnets/unprepareNetworkPolicies/action",
      ]
    }
  }
}

resource "azurerm_subnet_network_security_group_association" "databricks_private_nsg_association" {
  subnet_id                 = azurerm_subnet.databricks_private.id
  network_security_group_id = azurerm_network_security_group.databricks_private_nsg.id
}

resource "azurerm_subnet" "databricks_public" {
  name                 = local.vnet.subnet_names.databricks_public
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = local.vnet.env[terraform.workspace].subnet_address_spaces.databricks_public

  delegation {
    name = "databricks_workspaces_delegation"
    service_delegation {
      name = "Microsoft.Databricks/workspaces"
      actions = ["Microsoft.Network/virtualNetworks/subnets/action"]
    }
  }
}

resource "azurerm_subnet_network_security_group_association" "databricks_public_nsg_association" {
  subnet_id                 = azurerm_subnet.databricks_public.id
  network_security_group_id = azurerm_network_security_group.databricks_public_nsg.id
}
