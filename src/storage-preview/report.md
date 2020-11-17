# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az storage|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az storage` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az storage account local-user|LocalUsers|[commands](#CommandsInLocalUsers)|

## COMMANDS
### <a name="CommandsInLocalUsers">Commands in `az storage account local-user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az storage account local-user list](#LocalUsersList)|List|[Parameters](#ParametersLocalUsersList)|[Example](#ExamplesLocalUsersList)|
|[az storage account local-user show](#LocalUsersGet)|Get|[Parameters](#ParametersLocalUsersGet)|[Example](#ExamplesLocalUsersGet)|
|[az storage account local-user create](#LocalUsersCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersLocalUsersCreateOrUpdate#Create)|[Example](#ExamplesLocalUsersCreateOrUpdate#Create)|
|[az storage account local-user update](#LocalUsersCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersLocalUsersCreateOrUpdate#Update)|[Example](#ExamplesLocalUsersCreateOrUpdate#Update)|
|[az storage account local-user delete](#LocalUsersDelete)|Delete|[Parameters](#ParametersLocalUsersDelete)|[Example](#ExamplesLocalUsersDelete)|
|[az storage account local-user list-key](#LocalUsersListKeys)|ListKeys|[Parameters](#ParametersLocalUsersListKeys)|[Example](#ExamplesLocalUsersListKeys)|


## COMMAND DETAILS

### group `az storage account local-user`
#### <a name="LocalUsersList">Command `az storage account local-user list`</a>

##### <a name="ExamplesLocalUsersList">Example</a>
```
az storage account local-user list --account-name "sto2527" --resource-group "res6977"
```
##### <a name="ParametersLocalUsersList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group within the user's subscription. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.|account_name|accountName|

#### <a name="LocalUsersGet">Command `az storage account local-user show`</a>

##### <a name="ExamplesLocalUsersGet">Example</a>
```
az storage account local-user show --account-name "sto2527" --resource-group "res6977" --username "user1"
```
##### <a name="ParametersLocalUsersGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group within the user's subscription. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.|account_name|accountName|
|**--username**|string|The name of local user. The username must contain lowercase letters and numbers only. It must be unique only within the storage account.|username|username|

#### <a name="LocalUsersCreateOrUpdate#Create">Command `az storage account local-user create`</a>

##### <a name="ExamplesLocalUsersCreateOrUpdate#Create">Example</a>
```
az storage account local-user create --account-name "sto2527" --permission-scopes permissions="rwdlc" \
resource-name="share1" service="file" --permission-scopes permissions="rl" resource-name="share2" service="file" \
--resource-group "res6977" --username "user1"
```
##### <a name="ParametersLocalUsersCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group within the user's subscription. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.|account_name|accountName|
|**--username**|string|The name of local user. The username must contain lowercase letters and numbers only. It must be unique only within the storage account.|username|username|
|**--permission-scopes**|array|The permission scopes of the local user.|permission_scopes|permissionScopes|
|**--home-directory**|string|Optional, local user home directory.|home_directory|homeDirectory|
|**--ssh-authorized-keys**|array|Optional, local user ssh authorized keys for SFTP.|ssh_authorized_keys|sshAuthorizedKeys|

#### <a name="LocalUsersCreateOrUpdate#Update">Command `az storage account local-user update`</a>

##### <a name="ExamplesLocalUsersCreateOrUpdate#Update">Example</a>
```
az storage account local-user update --account-name "sto2527" --home-directory "dir1" --resource-group "res6977" \
--username "user1"
```
##### <a name="ParametersLocalUsersCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group within the user's subscription. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.|account_name|accountName|
|**--username**|string|The name of local user. The username must contain lowercase letters and numbers only. It must be unique only within the storage account.|username|username|
|**--permission-scopes**|array|The permission scopes of the local user.|permission_scopes|permissionScopes|
|**--home-directory**|string|Optional, local user home directory.|home_directory|homeDirectory|
|**--ssh-authorized-keys**|array|Optional, local user ssh authorized keys for SFTP.|ssh_authorized_keys|sshAuthorizedKeys|

#### <a name="LocalUsersDelete">Command `az storage account local-user delete`</a>

##### <a name="ExamplesLocalUsersDelete">Example</a>
```
az storage account local-user delete --account-name "sto2527" --resource-group "res6977" --username "user1"
```
##### <a name="ParametersLocalUsersDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group within the user's subscription. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.|account_name|accountName|
|**--username**|string|The name of local user. The username must contain lowercase letters and numbers only. It must be unique only within the storage account.|username|username|

#### <a name="LocalUsersListKeys">Command `az storage account local-user list-key`</a>

##### <a name="ExamplesLocalUsersListKeys">Example</a>
```
az storage account local-user list-key --account-name "sto2527" --resource-group "res6977" --username "user1"
```
##### <a name="ParametersLocalUsersListKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group within the user's subscription. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--account-name**|string|The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.|account_name|accountName|
|**--username**|string|The name of local user. The username must contain lowercase letters and numbers only. It must be unique only within the storage account.|username|username|
