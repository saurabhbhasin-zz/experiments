# get_athlete.py
import requests
import csv
# import pandas as pd
# import matplotlib.pyplot as plt

# ask for name
fname = input('Enter athlete first name:')
lname = input('Enter athlete last name:')

# construct url
url = 'https://ultrasignup.com/service/events.svc/history/%s/%s' % (fname, lname)

# prepare CSV file
csvfile = open("athlete.csv", "w")
writer = csv.writer(csvfile, delimiter=",")
writer.writerow(["Event", "Place", "Rank"])

# get relevant data and write to file
def get_athlete_races(url):
    results = requests.get(url)
    athlete_json = results.json()
    for i in athlete_json:
        for results in i['Results']:
            eventname = results.get('eventname')
            place = results.get('place')
            rank = results.get('runner_rank')
            row = eventname, place, rank
            writer.writerow(row)
        csvfile.close()


get_athlete_races(url)

# print("Calculating Median Place and Rank")
# df = pd.read_csv('athlete.csv')
# print(df.median())
#
# plt.hist(df.Rank)
# plt.show()
