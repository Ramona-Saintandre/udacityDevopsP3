#!/bin/bash
RESOURCE_GROUP_NAME=UdacityP3-tstate
STORAGE_ACCOUNT_NAME=udacityp3storage
CONTAINER_NAME=tstate

# Create policy assignment
# az policy definition create --name tagging-policy --mode indexed --rules policy.json

# Assign policy
# az policy assignment create --policy tagging-policy

# Create resource group
 az group create --name UdacityP3-CICD --location centralus # VM resource group
az group create --name UdacityP3-blob --location centralus # storage resource group
# Create storage account
az storage account create --resource-group UdacityP3-RG --name udacityp3storage --sku Standard_LRS --encryption-services blob --location CentralUS 

az storage account create --name udacityp3storage --resource-group UdacityP3-blob --location centralus --kind StorageV2 --sku Standard_LRS --https-only true --allow-blob-public-access false

az ad sp create-for-rbac -n "UdacityP3-SP" --role Contributor --query "{ client_id: appId, client_secret: password, tenant_id: tenant }"

# Get storage account key
ACCOUNT_KEY=$(az storage account keys list --resource-group UdacityP3-blob --account-name udacityp3storage --query '[0].value' -o tsv)
# Create blob container
az storage container create --name tstate --account-name udacityp3storage --account-key ceNydw+fKXP9/Y4uDYdgyPAOTms3YUqZUWWOoFSk7ZhAOdc/1mFsO40stDNqTcPs8qXfigcZoDRQ0V/b+xH7Qg== --resource-group UdacityP3-blob
echo "storage_account_name: udacityp3storage"
echo "container_name: tstate"
echo "access_key: $ACCOUNT_KEY"

## udacityp3-RG 
- udacitystorageacct
- udacityp3blob

## testrg 
appService-puplicip
udacityp3-test-vm 
