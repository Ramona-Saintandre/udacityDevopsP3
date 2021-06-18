resource "azurerm_resource_group" "udacitytest" {
  name     = var.resource_group
  location = var.location
}