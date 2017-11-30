import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://www.ironman.com/triathlon/events/americas/ironman"
RACE_DATE = "20171119"
RACE_LOCATION = "arizona"
BIDID = "2"
DETAIL = "1"


def getdata():
    EVENT_URL = "/cozumel/results.aspx?rd=%s&race=%s&bidid=%s&detail=%s" % (RACE_DATE, RACE_LOCATION, BIDID, DETAIL)
    print(BASE_URL+EVENT_URL)
    r = requests.get(BASE_URL+EVENT_URL).text
    soup = BeautifulSoup(r, 'lxml')
    athlete_name = soup.find("h1").text
    print(athlete_name)
    athlete_details = soup.find("table", {"class": "right"})
    # print(athlete_details)
    df = pd.read_html(str(athlete_details), index_col="Race Summary")
    print(df)
    results = df[0].to_json(orient='index')
    print(results)


getdata()
