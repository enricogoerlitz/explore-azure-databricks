variable "project_resourcegroup_name" {
  description = "The name of the resource group for the project"
  type        = string
  default     = "explore-azure-databricks-project-euwest-rg"

}

variable "default_tags" {
  description = "The default tags for all resources"
  type        = map(string)
  default = {
    "project" = "explore-azure-databricks"
  }
}

variable "westeurope_location" {
  description = "The location for the resources"
  type        = string
  default     = "westeurope"
}
