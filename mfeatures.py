import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
import json
import csv

access_token= 'TOKEN'

url = 'https://netskope.aha.io/api/v1/master_features'
headers = {"Authorization": "bearer " + access_token}
response = requests.get(url, headers = headers)
page_response = response.json()


total_records = page_response["pagination"]["total_records"]
total_pages = page_response["pagination"]["total_pages"]
current_page = page_response["pagination"]["current_page"]

print("Number of Master Features: %s") % (total_records)

csvfile = open("masterfeatures.csv", "a")
writer = csv.writer(csvfile, delimiter = ',')
writer.writerow(["Reference Number","Name","Link","Created At"])

while current_page <= total_pages:
	url2 = 'https://netskope.aha.io/api/v1/master_features?page=%s' % (current_page)
	print("getting data from page  %s") % current_page
	current_page = current_page + 1
	mresponse = requests.get(url2, headers = headers)
	master_features = mresponse.json()
	csvfile = open("masterfeatures.csv", "a")
	writer = csv.writer(csvfile, delimiter = ',')
	for i in master_features["master_features"]:
		row = i["reference_num"],i["name"],i["url"],i["created_at"]
		writer.writerow(row)
	csvfile.close()
