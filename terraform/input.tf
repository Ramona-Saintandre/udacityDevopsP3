# Azure GUIDS
variable "subscription_id" {}
variable "client_id" {}
variable "client_secret" {}
variable "tenant_id" {}

# Resource Group/Location
variable "location" {}
variable "resource_group" {}
variable "application_type" {}
variable "resource_type" {}

# Network
variable virtual_network_name {}
variable address_prefix_test {}
variable address_space {}

#Tags
variable "tags" {
    type = "map"
  }

# VM
variable "admin_username" {}