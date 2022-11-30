
import adal
import requests

context = adal.acquire_token_with_client_credentials(
'https://login.windows.net/' + '45cc25b3-b349-4a79-a6f1-2cefee3383fb',
    '4df6f284-6bc1-46a9-b9f7-4337061e809c',
    'K6N8Q~7Hn99za4mM1nj4gCedQRPGmVRcGYccndd2'
)
resource = 'https://management.azure.com/'
application_id = '4df6f284-6bc1-46a9-b9f7-4337061e809c'
application_secret = 'K6N8Q~7Hn99za4mM1nj4gCedQRPGmVRcGYccndd2'

print(context)


# token_response = context.acquire_token_with_client_credentials(resource, application_id, application_secret)



access_token = context.get('accessToken')

exit()

url = 'https://management.azure.com/subscriptions/119915bf-9cdc-404c-ab5e-c7bcae1adb7e/resourceGroups/practice/providers/Microsoft.Storage/storageAccounts/kaushik1adlsgen2?api-version=2019-04-01'
headers = {"Authorization": 'Bearer ' + access_token}

response = requests.get(url=url,headers = headers)
print(response.status_code)
print(response.text)



