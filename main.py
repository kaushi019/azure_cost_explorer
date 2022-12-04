from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.billing import BillingManagementClient


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


    response = client.generate_cost_details_report.begin_get_operation_results(
        scope="subscriptions/119915bf-9cdc-404c-ab5e-c7bcae1adb7e",
        operation_id="119915bf-9cdc-404c-ab5e-c7bcae1adb7e",
    ).result()
    print(response)


if __name__ == "__main__":
    main()