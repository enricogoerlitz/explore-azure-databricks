terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.15.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.6.3"
    }
  }

  backend "azurerm" {
    resource_group_name  = "explore-azure-databricks-project-euwest-rg"
    storage_account_name = "exploreadbeuwestsa"
    container_name       = "exploreadb-terraform-backend"
    key                  = "terraform.be.tfstate"
  }
}

provider "azurerm" {
  features {}
  subscription_id = "012e925b-f538-41ef-8d23-b0c85e7dbe7b"
}

provider "random" {}
