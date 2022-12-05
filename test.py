from azure.mgmt.costmanagement        import CostManagementClient
from azure.mgmt.costmanagement.models import QueryAggregation,QueryGrouping,QueryDataset,QueryDefinition,QueryTimePeriod,QueryFilter,QueryComparisonExpression
from azure.mgmt.resource              import ResourceManagementClient
from azure.identity                   import DefaultAzureCredential
from IPython.display                  import display, HTML
from typing                           import ContextManager
from azure.identity import ClientSecretCredential

import json
import pandas as pd
import datetime as dt
import calendar
import numpy as np


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


credential = ClientSecretCredential(tenant_id['VK'], client_id['VK'], client_secret['VK'], authority=authority)


thedate = dt.datetime.combine(dt.date.today(), dt.time())
first = thedate.replace(day=1)
last = thedate.replace(day = calendar.monthrange(thedate.year, thedate.month)[1])

subscription_id = '119915bf-9cdc-404c-ab5e-c7bcae1adb7e'

scope = '/subscriptions/{}'.format(subscription_id)

client = ResourceManagementClient(credential, subscription_id)

cmgmtc = CostManagementClient(credential = credential,subscription_id=subscription_id)


query_template = ( 
  QueryDefinition( 
     type      = "ActualCost"
    , timeframe = "ThisMonth" 
   , dataset   = 
     QueryDataset(
        granularity  = "Monthly"
      , aggregation  = { 
        "totalCost": QueryAggregation(name = "Cost", function = "Sum")
        ,"totalCostUSD": QueryAggregation(name = "CostUSD", function = "Sum") 
        }
      , grouping     = [
             QueryGrouping(name = "ResourceGroupName", type = "Dimension")
            ,QueryGrouping(name = "ResourceId"       , type = "Dimension")
            ,QueryGrouping(name = "ResourceType"     , type = "Dimension")
        ]
      , filter =  
        QueryFilter(
          dimensions = 
            QueryComparisonExpression(
                name = "ResourceGroupName"
              , operator = "In"
              , values = ["RESOURCE_GROUP"]
            )
        )
     )
  )
)



replaced_query = (
  query_template.deserialize(
    json.loads(
      json.dumps(
        query_template.serialize()
      ).replace('RESOURCE_GROUP','destination_rg')
    )
  )
)

print(query_template)

print(replaced_query)

# response = cmgmtc.dimensions.by_external_cloud_provider_type(
#         external_cloud_provider_type="externalBillingAccounts",
#         external_cloud_provider_id="100",
# )
# for item in response:
#     print(item)

# result = cmgmtc.query.usage( scope = scope, parameters = replaced_query)

# data = pd.DataFrame(result.rows, columns = list(map(lambda col: col.name, result.columns)))
 
# data_sorted = data.sort_values(by='CostUSD' ,ascending = False)

# data_filtered = data_sorted

# pd.set_option('display.max_rows', data_filtered.shape[0]+1)

# display(HTML(data_filtered.to_html())) 
