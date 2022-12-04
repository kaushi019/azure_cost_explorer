from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.billing import BillingManagementClient
from azure.mgmt.costmanagement import CostManagementClient

import json


authority = 'https://login.microsoftonline.com'
tenant_id = {
    'VK' : '45cc25b3-b349-4a79-a6f1-2cefee3383fb',
    'KV' : '19d34b9b-ff87-409e-83f0-197d456e8547'
} 
client_id = {
    'VK' : '4df6f284-6bc1-46a9-b9f7-4337061e809c',
    'KV' : '486c2b62-b02a-4e11-83ca-646da9068223'
}
client_secret = {
    'VK' : 'K6N8Q~7Hn99za4mM1nj4gCedQRPGmVRcGYccndd2',
    'KV' : 'ksk8Q~FX9rGZvV.5uYPOquQZywpTJ9oqOFTN_dh0'
}
subscription_id = {
    'VK' : '119915bf-9cdc-404c-ab5e-c7bcae1adb7e',
    'KV' : '5c057149-3b68-448d-8621-f2dae62d2f35'
}
scope = '/subscriptions/{}'.format(subscription_id['VK'])


credential = ClientSecretCredential(tenant_id['VK'], client_id['VK'], client_secret['VK'], authority=authority)

billing_client = BillingManagementClient(
    credential,
    subscription_id['VK']
)

cost_client = CostManagementClient(
    credential,
    subscription_id['VK']
)

billing_url = 'https://management.azure.com/providers/Microsoft.Billing/billingAccounts?api-version=2019-10-01-preview'
billing_profile = {
    'VK' : 'Vennela Kailasa',
    'KV' : 'Kaushik Veligatla'
}
billing_id = {
    'VK' : '518ff86d-a6cf-4271-9f9c-5e9e43128a0c',
    'KV' : 'e3899987-a70b-4adf-acb7-477dfaed24ed'
}


invoices = billing_client.invoices.list_by_billing_subscription('2022-11-08','2022-12-07') 


available_bal = billing_client.available_balances.get(billing_profile_name=billing_profile['VK'],billing_account_name=billing_id['VK'])
# addr = billing_client.address

a = cost_client.generate_reservation_details_report.begin_by_billing_profile_id


# print(available_bal)
# print(json.dumps(addr))

print(a)


