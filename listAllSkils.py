import requests
import json
import config

def authentication_token():
    url = "https://auth.emsicloud.com/connect/token"

    payload = "client_id=ly6xjk21ztho1xqv&client_secret=291igoyM&grant_type=client_credentials&scope=emsi_open"
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)
    jsresp=json.loads(response.text)

    return jsresp['access_token']
def alllistskils():
    url = "https://skills.emsicloud.com/versions/latest/skills"
    authtok='Bearer '+authentication_token()
    headers = {'authorization': authtok}

    response = requests.request("GET", url, headers=headers)
    content = json.loads(response.text)
    content =json.dumps(content, indent=4)
    f = open("Alllist.json", "w+")
    f.write(content)


    #print(response.text)

def searchskils(query):
    url = "https://skills.emsicloud.com/versions/latest/skills"
    querystring = {"q":query}
    authtok='Bearer '+authentication_token()
    headers = {'authorization': authtok}

    response = requests.request("GET", url, headers=headers, params=querystring)
    content = json.loads(response.text)
    content =json.dumps(content, indent=4)
    f = open("Filter.json", "w+")
    f.write(content)


def getskils_type(typeId):
    url = "https://skills.emsicloud.com/versions/latest/skills"
    authtok='Bearer '+authentication_token()

    querystring = {"typeId":typeId}

    headers = {'authorization': authtok}

    response = requests.request("GET", url, headers=headers, params=querystring)

    content = json.loads(response.text)
    content =json.dumps(content, indent=4)
    f = open("skilsbyType.json", "w+")
    f.write(content)


alllistskils()
searchskils(config.searchskil_query)
getskils_type(config.skilbytype)
