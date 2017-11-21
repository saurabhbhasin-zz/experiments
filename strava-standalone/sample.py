from __future__ import print_function
# import json
import requests
from stravalib.client import Client
#import sqlite3 as sqlite

client = Client()
authorize_url = client.authorization_url(client_id=15271, redirect_uri='http://localhost')
#mytoken = '203ab78f308e6fafc51df06116efa86774acc7ea'

# Extract the code from your webapp response
code = requests.get(authorize_url)
access_token = client.exchange_code_for_token(client_id=15271, client_secret='c15e1e0820435940d2042a7b11954cdc1c53ed76', code='c95487903f9c2cac4f59f75ed9470a98ed497f23')

# Now store that access token somewhere (a database?)
client.access_token = access_token
athlete = client.get_athlete()
# print("For {id}, I now have an access token {token}".format(id=athlete.id, token=access_token))

# for club in athlete.clubs:
#     print("{name} in {city}, Club Type: {ctype}".format(name=club.name, city=club.city, ctype=club.sport_type))

# f_act = client.get_friend_activities()
# for i in f_act:
#     print(i)

# print("All time total runs: {total_runs}".format(total_runs=athlete.stats.all_run_totals.count))
segment_id = 3991086
segment = client.get_segment(segment_id)
# print("Segment Name: {name} ".format(name=segment.name))
# print(segment.distance)
# print("Average Grade: {grade}%".format(grade=segment.average_grade))
# print("Segment in {city}, {state}".format(city=segment.city, state=segment.state))
# effort = []
# for i in segment.leaderboard.entries:
#     row = i.effort_id
#     effort.append(row)
# print(effort)


# db_filename = 'followers.db'
# conn = sqlite.connect(db_filename)
# cursor = conn.cursor()

# save follower names to database
# for a in my_followers:
    # uncomment the line below to print follower names
    # print(a.firstname,a.lastname)
    # cursor.execute("INSERT INTO `my_followers` (`firstname`,`lastname`) VALUES (?, ?)", (a.firstname, a.lastname))
# conn.commit()
# conn.close()
