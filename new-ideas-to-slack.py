import requests
import json
import datetime

access_token= 'TOKEN'

#Get the current time and compute 24 hours ago
current_time = datetime.datetime.now()
yesterday = datetime.timedelta(days=1)
tminus24 = current_time - yesterday

#Get Ideas created since last 24 hours
url = 'https://netskope.aha.io/api/v1/ideas?created_since=%s' % (tminus24)

headers = {"Authorization": "bearer " + access_token}
response = requests.get(url, headers = headers)
ideas = response.json()

for i in ideas["ideas"]:
#Store stuff in variables
    reference_num = i["reference_num"]
    name = i["name"]
    url = i["url"]
    payload = {'value1':reference_num,'value2':name,'value3':url} 
    headers = {'content-type': 'application/json'}
#Make the request to IFTTT Maker Channel
    requests.post("https://maker.ifttt.com/trigger/aha/with/key/KEY",data = json.dumps(payload),headers=headers)
