import requests
import json
url = "https://auth.emsicloud.com/connect/token"

payload = "client_id=ly6xjk21ztho1xqv&client_secret=291igoyM&grant_type=client_credentials&scope=emsi_open"
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)
jsresp=json.loads(response.text)

print(jsresp['access_token'])
