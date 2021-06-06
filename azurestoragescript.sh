#!/bin/bash
RESOURCE_GROUP_NAME=UdacityP3-tstate
STORAGE_ACCOUNT_NAME=udacityp3storage
CONTAINER_NAME=tstate

# Create policy assignment
# az policy definition create --name tagging-policy --mode indexed --rules policy.json

# Assign policy
# az policy assignment create --policy tagging-policy

# Create resource group
az group create --name UdacityP3-tstate --location centralus
# Create storage account
az storage account create --resource-group UdacityP3-tstate --name udacityp3storage --sku Standard_LRS --encryption-services blob --location CentralUS 


# Get storage account key
ACCOUNT_KEY=$(az storage account keys list --resource-group UdacityP3-tstate --account-name udacityp3storage --query '[0].value' -o tsv)
# Create blob container
az storage container create --name tstate --account-name udacityp3storage --account-key pMebkXhJEroMrgLYthf54aq+gDqfFO5cNP/ECUD1VOGYgK7sEie52DnYgdSY48qUxGLY7rU0nUwJOAhWyWrICw== --resource-group UdacityP3-tstate
echo "storage_account_name: udacityp3storage"
echo "container_name: tstate"
echo "access_key: $ACCOUNT_KEY"