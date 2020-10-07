# import requests

# url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

# querystring = {"region":"US","q":"tesla"}

# headers = {
#     'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
#     'x-rapidapi-key': "e3dc5b0e9fmsh49a871c2beed174p192c1ajsnca8bc27bb9d9"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response)

import requests
import json

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"

querystring = {"region":"US","symbol":"AAPL"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "e3dc5b0e9fmsh49a871c2beed174p192c1ajsnca8bc27bb9d9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

x = json.dumps(response.text)
y=json.loads(response.text)

print(type(response.text))
print(type(y))
print(y["financialData"]["currentPrice"])
# print(y)
# print(response.text.defaultKeyStatistics)
# print(x[defaultKeyStatistics])
