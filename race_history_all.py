import requests
import csv

with open("names.csv", "r") as f:
    csv_reader = csv.reader(f, delimiter=",")
    for row in csv_reader:
        fname = (row[1])
        lname = (row[2])
        fullname = fname + lname
        print(fullname)
        url = 'https://ultrasignup.com/service/events.svc/history/%s/%s' % (fname, lname)
        athletecsv = open("%s.csv" % fullname, "w")
        writer = csv.writer(athletecsv, delimiter=",")
        writer.writerow(["Event", "Place", "Rank"])
        for i in url:
            results = requests.get(url)
            athlete_json = results.json()
            for k in athlete_json:
                for results in k['Results']:
                    eventname = results.get('eventname')
                    place = results.get('place')
                    rank = results.get('runner_rank')
                    row = eventname, place, rank
                    writer.writerow(row)
        athletecsv.close()
