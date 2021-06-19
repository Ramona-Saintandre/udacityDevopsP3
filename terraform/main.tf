provider "azurerm" {
tenant_id       = var.tenant_id
subscription_id = var.subscription_id
client_id       = var.client_id
client_secret   = var.client_secret
features {}
}
resource "azurem_storage_account" "udacityp3store" {

}
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "2.63.0"
    }
  }
  }
terraform {
backend "azurerm" {
resource_group_name  = "udacityP3-CICD"
storage_account_name = "udacityp3store"
container_name       = "udacityp3blobcontain"
key                  = "terraform.tfstate"
access_key           =  "d9M+voCYERuxv3ohJFY8k2LxsfnMK1Iq0Jr99RKH3EjfTsxZ4GfGEoCdXxAra7t9ED0glU35LJ93hV0q3rj6rA==" 
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
address_prefixes_test  = var.address_prefixes_test
}

module "nsg-test" {
source           = "./modules/networksecuritygroup"
location         = var.location
application_type = var.application_type
resource_type    = "NSG"
resource_group   = module.resource_group.resource_group_name
subnet_id        = module.network.subnet_id_test
address_prefixes_test = var.address_prefixes_test
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
  location        = var.location
  application_type = var.application_type
  resource_type    = "VM"
  subnet_id       = module.network.subnet_id_test
  resource_group  = module.resource_group.resource_group_name
  public_ip_address_id = module.publicip.public_ip_address_id
  admin_username  = var.admin_username
 
  
}
