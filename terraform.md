
    - task: TerraformTaskV1@0
      displayName: 'terraform init'
      inputs:
        provider: 'azurerm'
        command: 'init'
        workingDirectory: '$(System.DefaultWorkingDirectory)/terraform'
        backendServiceArm: 'SPProject3-Terraform'
        backendAzureRmResourceGroupName: 'udacityp3-RG'
        backendAzureRmStorageAccountName: 'udacityp3storageacct'
        backendAzureRmKey: 'terraform.tfstate'
        backendAzureRmContainerName: 'udacityp3blob'
    -task: TerraformTaskV1@0
      displayName: 'terraform validate'
      inputs:
        provider: 'azurerm'
        command: 'validate'
        workingDirectory: '$(System.DefaultWorkingDirectory)/terraform'
    - task: TerraformCLI@0
      displayName: 'terraform plan'
      inputs:
        command: 'plan'
        workingDirectory: '$(System.DefaultWorkingDirectory)/terraform'
        environmentServiceName: 'UdacityP3-sp'
        runAzLogin: true
        secureVarsFile: 'terraform.tfvars'
        allowTelemetryCollection: true
    - task: TerraformCLI@0
      inputs:
        command: 'apply'
        workingDirectory: '$(System.DefaultWorkingDirectory)/terraform'
        environmentServiceName: 'SPProject3-Terraform'
        runAzLogin: true
        secureVarsFile: 'terraform.tfvars'
        commandOptions: '-auto-approve'
        allowTelemetryCollection: true
    - task: ArchiveFiles@2
      displayName: 'Archive FakeRestAPI'
      inputs:
        rootFolderOrFile: 'automatedtesting/jmeter/fakerestapi'
        includeRootFolder: false
        archiveType: 'zip'
        archiveFile: '$(Build.ArtifactStagingDirectory)/$(Build.BuildId)-fakerestapi.zip'
    - publish: '$(Build.ArtifactStagingDirectory)/$(Build.BuildId)-fakerestapi.zip'
      displayName: 'Upload Package'
      artifact: drop-fakerestapi
    - task: ArchiveFiles@2
      displayName: 'Archive Automated Tests'
      inputs:
        rootFolderOrFile: 'automatedtesting' 
        includeRootFolder: false
        archiveType: 'zip'
        archiveFile: '$(Build.ArtifactStagingDirectory)/$(Build.BuildId)-automatedtests.zip' 
    - publish: '$(Build.ArtifactStagingDirectory)/$(Build.BuildId)-automatedtests.zip'
      displayName: 'Upload Test Package'
      artifact: drop-automatedtests
- stage:
  jobs:
  - deployment: TEST
    displayName: Deploy VM
    environment:
      name: 'TEST'
      resourceType: VirtualMachine
    pool:
      vmImage: 'Ubuntu-latest'
    
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AzureRmWebAppDeployment@4
            inputs:
              ConnectionType: 'AzureRM'
              azureSubscription: 'SPProject3'
              appType: 'webAppLinux'
              WebAppName: 'test-appservice-proj3'
              deployToSlotOrASE: true
              ResourceGroupName: 'azuredevopsproj3'
              SlotName: 'production'
              packageForLinux: '$(Pipeline.Workspace)/drop-fakerestapi/$(Build.BuildId)-fakerestapi.zip'
          - task: Bash@3
            inputs:
              targetType: 'inline'
              script: |
                # Write your commands here
                
                echo 'FakeRestAPI Running'
- stage: postDeployment
  displayName: 'Post-Deployment'
  pool:
      vmImage: 'Ubuntu-latest'
  jobs:
    - job: runnewman