
from azure.identity import AzureCliCredential
from azure.identity import DefaultAzureCredential
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
import os


authority = 'https://login.microsoftonline.com'
tenant_id = '45cc25b3-b349-4a79-a6f1-2cefee3383fb'
client_id = '4df6f284-6bc1-46a9-b9f7-4337061e809c'
client_secret = 'K6N8Q~7Hn99za4mM1nj4gCedQRPGmVRcGYccndd2'
subscription_id = '119915bf-9cdc-404c-ab5e-c7bcae1adb7e'

credential = ClientSecretCredential(tenant_id, client_id, client_secret, authority=authority)

token = credential.get_token("https://management.azure.com/.default") 

print(token)

resource_client = ResourceManagementClient(credential, subscription_id)
group_list = resource_client.resource_groups.list()
column_width = 40


print(type(group_list))

print("Resource Group".ljust(column_width) + "Location")
print("-" * (column_width * 2))


for group in list(group_list):
    print(f"{group.name:<{column_width}}{group.location}")

