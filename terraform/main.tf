provider "azurerm" {
  tenant_id       = var.tenant_id
  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  features {}
}
terraform {
  backend "azurerm" {
   resource_group_name  = "UdacityP3-tstate"
    storage_account_name = "udacityp3storage"
    container_name       = "tstate"
    key                  = "terraform.tfstate"
    access_key           =  "dYVXU5EvgiaiOPHgZT0+9Op4eSWKbPnXJofHvwxgb3aYz9ByhjVTsio+PkpgNTAnHMCQSprOPCgaAp0hlsrFvA=="
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
  name            = "vm-test-automation"
  location        = var.location
  subnet_id       = module.network.subnet_id_test
  resource_group  = module.resource_group.resource_group_name
  public_ip       = module.publicip.public_ip_address_id
  admin_username  = var.admin_username
  #packer_image    = var.packer_image
  public_key_path = var.public_key_path
}
