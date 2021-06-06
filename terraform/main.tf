provider "azurerm" {
  tenant_id       = "38be56ef-db1d-447d-8bfb-0aa8fbbbf271"
  subscription_id = "25283872-c0f5-4f2e-9c2a-f19f8e24b3c4"
  client_id       = "77be2256-863f-44e4-9f67-618ee68eade2"
  client_secret   = "I~ZrxBbwG_bmFd0kV4O4kXLl7wJRJ0dG_G"
  features {}
}
terraform {
  backend "azurerm" {
   resource_group_name  = "UdacityP3-blob"
    storage_account_name = "udacityp3storage"
    container_name       = "tstate"
    key                  = "terraform.tfstate"
    
  }
}
module "resource_group" {
  source               = "./modules/resource_group"
  resource_group       = var.resource_group
  location             = var.location
}
module "network" {
  source               = "./modules/network"
  location             = var.location
  virtual_network_name = var.virtual_network_name
  address_space        = var.address_space
  application_type     = var.application_type
  resource_type        = "VNET"
  resource_group       = module.resource_group.resource_group_name
  address_prefix_test  = var.address_prefix_test
}

module "nsg-test" {
  source           = "./modules/networksecuritygroup"
  location         = var.location
  application_type = var.application_type
  resource_type    = NSG
  resource_group   = module.resource_group.resource_group_name
  subnet_id        = module.network.subnet_id_test
  address_prefix_test = var.address_prefix_test
}
module appservice {
  source           = "./modules/appservice"
  location         = var.location
  application_type = var.application_type
  resource_type    = "AppService"
  resource_group   = module.resource_group.resource_group_name
  #tags             = local.tags
}
module "publicip" {
  source           = "./modules/publicip"
  location         = var.location
  application_type = var.application_type
  resource_type    = "publicip"
  resource_group   = module.resource_group.resource_group_name
}
module "vm" {
  source          = "./modules/vm"
  name            = "vm-udacityP3"
  location        = var.location
  subnet_id       = module.network.subnet_id_test
  resource_group  = module.resource_group.resource_group_name
  public_ip_address_id = module.publicip.public_ip_address_id
  admin_username  = var.admin_username
  public_key_path = var.public_key_path
}
