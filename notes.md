 ## Log Analytics 
[Log Analytics agent overview](https://docs.microsoft.com/en-us/azure/azure-monitor/agents/log-analytics-agent)  
[Overview of Log Analytics in Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview)  
[Log Analytics tutorial](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial)  
[Analyze your Azure infrastructure by using Azure Monitor logs](https://docs.microsoft.com/en-us/learn/modules/analyze-infrastructure-with-azure-monitor-logs/?WT.mc_id=cloudskillschallenge_8351edfe-a67a-46d4-81cd-6439844b72ac)  
## Selenium

## Postman

## Jmeter


az ad sp create-for-rbac --name UdacityP3 --query "{client_id: appId, client_secret: password, tenant_id: tenant}"

## login information 4/18/2021
{
    "cloudName": "AzureCloud",
    "homeTenantId": "38e23809-f428-4d08-9f4e-b3b8b2df585c",
    "id": "1d53902c-4bc6-44c8-82da-d1a59f04c098",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Udacity Devops",
    "state": "Enabled",
    "tenantId": "38e23809-f428-4d08-9f4e-b3b8b2df585c",
    "user": {
      "name": "thenewmona@gmail.com",
      "type": "user"
    }
  }
]
PS E:\udacityDevopsP3>


## Storage account resources   
[Upload a file to Azure Storage Account using Terraform.](https://www.youtube.com/watch?v=zrVFl2Yfuxs)
## Service principal 
**[az ad sp: commands](https://docs.microsoft.com/en-us/cli/azure/ad/sp?view=azure-cli-latest)
The above resource is a list of commands for service principals. 
Including how to list them, delete them, and modify them. 
[Azure Service Principal - SPN-video tutorial](https://www.youtube.com/watch?v=-F9yzj4Kjeo)
[Keep your Azure Subscription Clean Automatically](https://dev.to/azure/keep-your-azure-subscription-clean-automatically-mmi)

## 5/30/2021

E:\udacityDevopsP3>az ad sp create-for-rbac --name UdacityP3-quality --query "{client_id: appId, client_secret: password, tenant_id: tenant}"
Changing "UdacityP3-quality" to a valid URI of "http://UdacityP3-quality", which is the required format used for service principal names
In a future release, this command will NOT create a 'Contributor' role assignment by default. If needed, use the --role argument to explicitly create a role assignment.
Creating 'Contributor' role assignment under scope '/subscriptions/1d53902c-4bc6-44c8-82da-d1a59f04c098'
The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. For more information, see https://aka.ms/azadsp-cli
{
  "client_id": "2f50d87a-b33b-4719-adc8-728994d71a72",
  "client_secret": "igIPJ4TxTnP-h9-8Z4adEBln9fjW0U0liG",
  "tenant_id": "38e23809-f428-4d08-9f4e-b3b8b2df585c"
}

6/1 
E:\udacityDevopsP3>az account show
{
  "environmentName": "AzureCloud",
  "homeTenantId": "38e23809-f428-4d08-9f4e-b3b8b2df585c",
  "id": "1d53902c-4bc6-44c8-82da-d1a59f04c098",
  "isDefault": true,
  "managedByTenants": [],
  "name": "Udacity Devops",
  "state": "Enabled",
  "tenantId": "38e23809-f428-4d08-9f4e-b3b8b2df585c",
  "user": {
    "name": "thenewmona@gmail.com",
    "type": "user"
  }
}

  [Using the Azure CLI to Create Azure DevOps Pipelines](https://www.youtube.com/watch?v=jz-1RUNy1Rg)
  [Using Terraform in Azure DevOps Pipelines PART 1](https://www.youtube.com/watch?v=kqwzqWcSCYM&list=PL5uEazNEXQMIE3wgtVw5uICq2rxRe8VI9)
  [Using Terraform in Azure DevOps Pipelines PART 2](https://www.youtube.com/watch?v=x631jUw1J04)