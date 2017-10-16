import requests
import json
import ahatoken
import csv
import logging

access_token= ahatoken.token
payload = {"idea_subscription":
                {"email":"email@address.com"}
          }
headers = {"Content-Type":"application/json", "Authorization": "bearer " + access_token}
parameters_json = json.dumps(payload)
logging.basicConfig(filename='subs.log', level=logging.DEBUG)

def AddSubscribers():
   with open('/home/pi/ideas.csv') as csvfile:
       readCSV = csv.reader(csvfile, delimiter=',')
       for row in readCSV:
           url = 'https://netskope.aha.io/api/v1/ideas/%s/subscriptions/' % row[0]
           response = requests.post(url, data = parameters_json, headers = headers)
           logging.info('Subscriber added')
   return

AddSubscribers()
