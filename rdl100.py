#RDL100.py

import requests
import json
from statistics import median
from bs4 import BeautifulSoup
import csv

# 2016 Stuff
url2016 = 'https://ultrasignup.com/service/events.svc/results/35456/json?_search=false&nd=1508212876228&rows=1500&page=1&sidx=status+asc%2C+&sord=asc'
response2016 = requests.get(url2016)
results = response2016.json()

age2 = []
ftime = []
for i in results:
        # print(i["formattime"],i["firstname"],i["lastname"])
    age2.append(i["age"])
    ftime.append(i["formattime"])
print("The median age of athletes at RDL100 2016 was:")
print(median(age2))
print("The median finish time of athletes at RDL100 2016 was:")
print(median(ftime))

# 2017 Stuff
race = 'https://ultrasignup.com/entrants_event.aspx?did=42474'
csvfile = open("all_entrants.csv", "w")
writer = csv.writer(csvfile, delimiter = ',')
headerrow = 'Rank', 'Age Rank', 'Projected Time', 'Age Group', 'First Name', 'Last Name', 'City', 'State'
writer.writerow(headerrow)

def entrants_to_CSV(race):
    page = requests.get(race).text
    soup = BeautifulSoup(page, 'lxml')
    all_entrants = soup.find("table", {"class" : "ultra_grid"})
    for row in all_entrants.findAll('tr')[2:]:
        col = row.findAll('td')
        rank = col[0].get_text().strip()
        age_rank = col[1].get_text().strip()
        projected_time = col[3].get_text()
        ag = col[4].get_text().strip()
        fname = col[5].get_text().strip()
        lname = col[6].get_text().strip()
        city = col[7].get_text().strip()
        state = col[8].get_text().strip()
        # finishes = col[12].get_text()
        entry = rank, age_rank, projected_time, ag, fname, lname, city, state
        writer.writerow(entry)
    csvfile.close()
entrants_to_CSV(race)
