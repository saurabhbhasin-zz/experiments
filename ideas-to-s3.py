import requests
import json
import datetime
import csv
import boto3

s3 = boto3.resource('s3')

access_token= 'TOKEN'

current_time = datetime.datetime.now()
yesterday = datetime.timedelta(days=1)
tminus24 = current_time - yesterday

url = 'https://netskope.aha.io/api/v1/ideas?created_since=%s' % (tminus24)

headers = {"Authorization": "bearer " + access_token}
response = requests.get(url, headers = headers)
ideas = response.json()

csvfile = open("ideas.csv", "w")
writer = csv.writer(csvfile, delimiter = ',')
#writer.writerow(["Reference Number","Name","Link"])

for i in ideas["ideas"]:
    row = i["reference_num"],i["name"],i["url"]
    writer.writerow(row)
csvfile.close()

data = open('ideas.csv','rb')
s3.Bucket('ahaideasnetskoppe').put_object(Key='ideas.csv', Body=data)
