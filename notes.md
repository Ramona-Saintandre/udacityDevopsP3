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

PS E:\udacityDevopsP3> az ad sp create-for-rbac --role="Contributor" --name="UdacityP3" --scopes="/subscriptions/1d53902c-4bc6-44c8-82da-d1a59f04c098"
Changing "UdacityP3" to a valid URI of "http://UdacityP3", which is the required format used for service principal names
Creating a role assignment under the scope of "/subscriptions/1d53902c-4bc6-44c8-82da-d1a59f04c098"
  Retrying role assignment creation: 1/36
  Retrying role assignment creation: 2/36
The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "840b397f-3123-4391-9921-8edfff601ec5",
  "displayName": "UdacityP3",
  "name": "http://UdacityP3",
  "password": "jFSAwvD4ZY_SN.hHtb3kIVpAhfKYiTlKn-",
  "tenant": "38e23809-f428-4d08-9f4e-b3b8b2df585c"