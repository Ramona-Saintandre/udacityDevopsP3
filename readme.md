
![Build Status](https://dev.azure.com/ramonasaintandre0285/UdacityP3-ensuringquality/_apis/build/status/Ramona-Saintandre.udacityDevopsP3?branchName=master)  


# Udacity-Azure-Devops-P3: Ensuring Quality Releases

## Project Overview

In this project, I will demonstrate the skills learned about ensuring quality releases in the [**Udacity Nanodegree: DevOps Engineer for Microsoft Azure**](https://www.udacity.com/course/cloud-devops-using-microsoft-azure-nanodegree--nd082). Using Microsoft Azure.

 In this project I will create a VM using Terraform, along with Packer to deploy an app to Azure AppService.  
  Then, I will  test environments and run automated tests, using various tools such as Jmeter, Selenium, and Postman.   
   To finalize this project I will utilize [**Azure Log Analytics**](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview) to provide insight into my application's behavior by querying custom log files.

### Dependencies
| Dependency | Link |  
| ------ | ------ |
 | **Python** | https://www.python.org/downloads/ |
 | **Terraform** | https://www.terraform.io/downloads.html |
 | **Packer** | https://www.packer.io/ |
 | **JMeter** |  https://jmeter.apache.org/download_jmeter.cgi|
 | **Postman** | https://www.postman.com/downloads/ |
 | **Selenium** | https://sites.google.com/a/chromium.org/chromedriver/getting-started |
 **Azure DevOps** | https://dev.azure.com/ramonasaintandre0285/UdacityP3-ensuringquality
 **Azure CLI**  | https://aka.ms/cli_ref |
 **Azure Log Analytics**

### Project Steps
1. This is the starter repo for the project.

```sh
git clone https://github.com/jfcb853/Udacity-DevOps-Azure-Project-3
```
#### 1. Installation & Configuration
Login to Azure:<br>
**`az login`**

Create the password based authentication service principal for your project and query it for your ID and SECRET data: <br>
    **`az ad sp create-for-rbac --name SPProject3 --query "{client_id: appId, client_secret: password, tenant_id: tenant}"`**<br>
Make note of the password because it can't be retrieved, only reset.

![Service Principal info](projectimages/Service%20Principal%20info.png)
Login to the Service Principal using the following command with you credentials from the previous step: <br>
    **`az login --service-principal --username APP_ID --tenant TENANT_ID --password CLIENT_SECRET`**
Configure the storage account and state backend. 

You will need to create a Storage Account, before you can us Azure Storage as a backend.


You can also use the commands in the ```azurestoragescript.sh``` file in the repo to this.    
[Click Here](https://docs.microsoft.com/en-us/azure/developer/terraform/store-state-in-azure-storage) for instructions on creating the Azure storage account and backend.  

Replace the values below in terraform/environments/test/main.tf files with the output from the Azure CLI:

    * storage_account_name
    * container_name
    * key
    * access_key  
 

Create a Service Principal for Terraform and replace the below values in the terraform/environments/test/terraform.tfvars files with the output from the Azure CLI.

    * subscription_id
    * client_id
    * client_secret
    * tenant_id
[Click Here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret) if you need help with the steps for creating a service principal.  
![Service Principal in Azure](https://drive.google.com/file/d/1sbaZxiEwA3mQWtgGs5YFarjspEeSHS2n/view?usp=sharing)

#### 2. Azure DevOps

1. Create a new Azure Pipeline from the **`azure-pipelines.yaml`** file or start building one from scratch if you prefer.

2. Create a new service connection: In Azure Devops go to Project Settings > Service Connections > New Service Connection > Azure Resource Manager > Next > Service Principal (Automatic) > Next > Subscription. After choosing your subscription provide a name for the service connection.

3. If the pipeline runs now it will fail since no resources are provisioned yet in Azure.

4. Create an SSH key to log in to your VM.  
5.  [Click Here](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/mac-create-ssh-keys) for instructions on setting up an SSH key.

6. This SSH key can be saved and added to Azure Pipelines as a secure file. I also loaded my terraform.tfvars to Azure Pipelines as a secure file along with a .env file with my access-key.

7. Create your Azure resources (Most can be provisioned via Terraform using the Pipeline by adding tasks and jobs to the `azure-pipelines.yml` file utilizing ```terraform init```, ```terraform plan```, and ```terraform apply``` commands).


![TerraForm apply](projectimages/terraformapply-success.png)
1. Once the resources are deployed you will have to follow the instructions on setting up an environment in Azure Pipelines to register the Linux VM so your app can be deployed to it. You can find that documentation [here](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/environments-virtual-machines?view=azure-devops). In Azure DevOps under Pipelines > Environments > TEST > Add resource > Select "Virtual Machines" > Next > Under Operating System select "Linux".  You will be given a registration script to copy. SSH into your VM and paste this script into the terminal and run it. This will register your VM and allow Azure Pipelines to act as an agent to run commands on it.

![TEST-VM Environment](projectimages/P3VM.png)

1. Build the FakeRestAPI and Automated Testing artifacts and publish them to the artifact staging directory in the Pipeline.

![Build image](projectimages/projectbuild-url.png)  

2. Deploy the FakeRestAPI to your App Service on your VM. The URL for my webapp is (need to add URL)  
   It should look like the image below.

![Fake Rest Deploy](projectimages/MyFakerSight.png)


## 3. Running Tests in Pipeline

## Postman
Test Type | Technology | Stage in CI/CD pipeline | Status
:--- | :--- | :--- | :---:  
Integration | Postman | Test Stage - runs during build stage  | :white_check_mark:  

Goal | Status  
:--- | :---:  
Verify dummy API's can pass by running them through Newman| :white_check_mark:

[Install Postman](https://www.postman.com/downloads/). 
With the starter files I was able to test the dummy API locally with different environment variables and then export the results as a collection to my project directory.   
Once the collection files have been pushed to GitHub you will need to create a script to run a Data Validation and Regression test in the Pipeline and create a report of the results.   
The command line Collection Runner  

[Newman](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/#:~:text=Newman%20is%20a%20command%20line,integration%20servers%20and%20build%20systems.)   
was used to perform these tests.   
The following script was used:

```
    sudo npm install -g newman reporter
    echo 'Starting Tests...'
    echo 'Running Regression Test'
    newman run automatedtesting/postman/RegressionTest.postman_collection.json  --delay-request 15000 --reporters cli,junit --suppress-exit-code /
    echo 'Running Data Validation Test'
    newman run automatedtesting/postman/DataValidation.postman_collection.json  --delay-request 12000 --reporters cli,junit --suppress-exit-code
```
![Newman  Table](projectimages/newmantable.png)

 The results of the tests will also appear in the Pipeline output like so:

![Regression Test](projectimages/regression%20test%20output.png) 

![Postman Run](projectimages/Postman%20run%20report.jpg)  



#### Selenium
Test Type | Technology | Stage in CI/CD pipeline | Status
:--- | :--- | :--- | :---:    
Functional | Selenium | Test Stage - runs in custom linux VM | :white_check_mark:  

Goal | Status  
:--- | :---:  
Direct the output of the Selenium Test Suite to a log file, and execute the Test Suite. | :white_check_mark:  

The project requires that Selenium is installed on the VM to test the UI functionality of `https://www.saucedemo.com/` website.   

![Swag Shop Inventory](projectimages/swag_shirts.png)

ems were added to the shopping cart, and what items were removed from the shopping cart.

![SwagShop](projectimages/swag%20checkout.png)

I created the python code locally and made sure the test was working before ingesting it into the Pipeline.   
To this:

1. [Download the latest Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/). Make sure chromedriver is added to PATH.
2. Run
        **`pip install -U selenium`**

3. You can test Selenium by executing the **`login.py`** file in the Selenium folder. It should open the site and add all items to the shopping cart and then remove them from the shopping cart.
4. A script will need to be created to perform these tasks in the CLI in the Azure Pipelines  at this point. Make sure the script includes logging the items being added and removed from the cart that can be sent to an output file.
5. 
![Selenium Logs](projectimages/selenium%20logs.png)
![Selenium run 627](projectimages/selenium_run_627.png)
![pipeline run 627](projectimages/pipeline_run_627.png)
![Selenium run 628](projectimages/selenium_run_6_28.png)
![pipeline run 628](projectimages/pipeline_run_628.png)



#### JMeter  

![Jmeter install](projectimages/Jmeter%20install.png)
Test Type | Technology | Stage in CI/CD pipeline | Status
:--- | :--- | :--- | :---:
Performance | JMeter | Test Stage - runs against the AppService| :white_check_mark:    

Goal | Status
:--- | :---:  
Stress Test |:white_check_mark:
Endurance Test |:white_check_mark:


Two tests suites were created using the Starter API files.  
 (Stress Test and Endurance Test) You will need to replace the `APPSERVICEURL` with the Url of your AppService once it's deployed.  

In the Pipeline scripts were created to install JMeter and run the Stress and Endurance Tests.  

For the Pipeline two users were used for the tests so the free-tier resources wouldn't be maxed out.  

Before submission the tests will need to be ran simulating 30 users for a max duration of 60 seconds.  
The data output from these tests will need to generate an HTML report.  

**Note:** This may also be done non-CI/CD by [Installing JMeter](https://jmeter.apache.org/download_jmeter.cgi) and running the tests.
**Note:** This may also be done non-CI/CD.
![Jmeter summary](projectimages/Jmeter%20local%20summary%20report.png)

![Jmeter stress test](projectimages/Jmeter%20pipeline%20stress%20test.png) 

![Jmeter stress test](projectimages/Jmeter%20endurance%20test.png)  

![Jmeter pipeline run](projectimages/Jmeter%20endurance%20pipeline%20run.png) 

#### 4. Setup Log Analytics

![Log Analytics](projectimages/application%20logs%206_25.png)

Goal | Status
:--- | :---:  
Configure custom logging in Azure Monitor to ingest this log file. This may be done non-CI/CD. | :check_mark:  

A Log Analytics Workspace will need to be created to ingest the Selenium Log output file.  
 [This Resource](https://docs.microsoft.com/en-us/azure/azure-monitor/agents/data-sources-custom-logs) could be helpful in setting up Log Analytics.

Go to the app service > Diagnostic Settings > + Add Diagnostic Setting. Click AppServiceHTTPLogs and Send to Log Analytics Workspace. Select a workspace (can be an existing default workspace) > Save. Go back to the app service > App Service Logs. Turn on Detailed Error Messages and Failed Request Tracing > Save. Restart the app service.

Return to the Log Analytics Workspace > Logs and run a query such as `Perf`to see some log results and check that Log Analytics is working properly.

#### 5. Setup Custom Logging
In Log Analytics Workspace go to Advanced Settings > Data > Custom Logs > Add + > Choose File. Select the seleniumlog.txt file created from the Pipeline run. (I downloaded a copy to my local machine and uploaded a copy to the Azure VM via SSH) > Next > Next. Enter the paths for the Linux machine where the file is located, such as:
*    ` /seleniumlog.txt`
*   ` <your path>/seleniumlog.txt`
![Custom logging setup](projectimages/customloggingsetup.png) 

![Selenium Test Log output](projectimages/SeleniumTestLogs629.png)

![Selenium Run](projectimages/selennium%20run%20628.png)

Give it a name and click Done. 

Return to the Log Analytics Workspace > Virtual Machines. Click on your VM, then Connect. An agent will be installed on the VM that allows Azure to collect the logs from it. (Under Settings > Agents you should see you have "1 Linux Computer Connected")

Return to the Log Analytics Workspace > logs. Under Queries you can enter the name of the custom log created in the previous query and click Run. It's possible this could take a while to show logs. The logs may only show if the timestamp on the log file is updated after the agent was installed. You may also need to reboot the VM.
![Log output](projectimages/Loggingoutput.png)  

**Note:** This may also be done non-CI/CD.

#### 6. Setup Email Alerts
Goal | Status
:--- | :---:  
Configure an Action Group (email) | :white_check_mark:  

The project also calls for creating an alert rule with an HTTP 404 condition. It also requires an action group to be created with Email notification. After the alert takes effect, visit the URL of the AppService and try to cause 404 errors by visiting non-existent pages. After the 2nd 404 error an email alert should be triggered. To set this up:

![alerts](projectimages/appServicealerts.png)  
![alerts](projectimages/Malertscreation.png)  
![alerts](projectimages/alert%20rules.png)   
  
In Azure Portal go to the AppService > Alerts > New Alert Rule. Add the HTTP 404 condition with a threshold value of 1. This creates an alert once there are at least 2 404 errors. Click **Done**. Now create the action group with the notification type set to **Email/SMS message/Push/Voice** choosing the email option. Give it a name and severity level.

![Email Alert](projectimages/InkedAzure%20email%20alert_LI.jpg)

## Enchancements 

One of the enchancements that I would like to do with this project, is to recreate it using [Azure Bicep](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/bicep-tutorial-create-first-bicep?tabs=azure-powershell). 


## Note to reviewer

**More images can be found in the /projectimagefolder

I tried to re-run my Jmeter test to get the required screenshots. U
Unfortnately I have exceeded my quota, and I can not longer run anymore test against my service without paying. 

So it would be greatly appreciated if this is taken into consideration when reviewing my project. 

Thanks you 

I have already exceeded my 50$ budget for this project. 
![quota reached](projectimages/appservicequota.png)  
![cost](projectimages/costanalysis.png)  
 ![JmeterStress HTML report](projectimages/st)
![Jmeter Stress XML](projectimages/stresstesthtml629.png) 
![Jmeter HTML](projectimages/JmeterHTMLreports.png)  
![Jmeter endurance XML](projectimages/endurancecsv629.png)
![JmeterEndurnce HTML report](projectimages/Jmeterendurancehtml629.png)

As you can see from the previous screen shots, they were passing. 
I just did not include the URL timestamp in the screenshot. 

![JmeterEndurnce HTML report 626 passed ](projectimages/Jmeter%20endurance%20test.png)
![JmeterStress HTML report 626 passed ](projectimages/Jmeter%20stress%20test.png)

Thank you 