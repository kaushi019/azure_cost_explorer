from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.billing import BillingManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-costmanagement
# USAGE
    python get_details_of_the_operation_result.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CostManagementClient(
        credential=DefaultAzureCredential(),
    )
    billing_client = BillingManagementClient(
        credential = DefaultAzureCredential(), 
        subscription_id = '119915bf-9cdc-404c-ab5e-c7bcae1adb7e'
    )

    print(billing_client)

    print(client)

    # response = client.generate_cost_details_report.(
    #     scope="subscriptions/119915bf-9cdc-404c-ab5e-c7bcae1adb7e",
    #     operation_id="119915bf-9cdc-404c-ab5e-c7bcae1adb7e",
    # ).result()
    # print(response)


if __name__ == "__main__":
    main()