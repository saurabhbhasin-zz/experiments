import logging
import requests
logging.basicConfig(filename='strava.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
headers = {"Authorization": "Bearer 203ab78f308e6fafc51df06116efa86774acc7ea"}
current_athlete = 'https://www.strava.com/api/v3/athlete'
r = requests.get(current_athlete, headers=headers)
athlete = r.json()
# print(athlete)
athlete_id = athlete["id"]
logging.info(athlete_id)
segment_id = 3991086


def getAthlete(athlete_id):
    athlete_url = 'https://www.strava.com/api/v3/athletes/%s' % athlete_id
    response = requests.get(athlete_url, headers=headers)
    athlete = response.json()
    # print(json.dumps(athlete, indent=4))
    # print(athlete["firstname"] + " " + athlete["lastname"] + " has " + str(athlete["follower_count"]) + " followers.")
    # print(athlete["firstname"] + " " + athlete["lastname"])
    # c = []
    # for i in athlete["clubs"]:
    #     c.append(i["id"])
    # return c
    return athlete


def allEfforts(segment_id):
    url = https://www.strava.com/api/v3/segments/%s/all_efforts % (segment_id)
    r = requests.get(url, headers=headers)
    response = r.json()
    print(response)


def getStats(athlete_id):
    stats_url = 'https://www.strava.com/api/v3/athletes/%s/stats' % (athlete_id)
    response = requests.get(stats_url, headers=headers)
    stats = response.json()
    return stats


def getClubs(club_id):
    for i in club_id:
        clubs_url = 'https://www.strava.com/api/v3/clubs/%s' % (i)
        response = requests.get(clubs_url, headers=headers)
        clubs = response.json()
        # print(clubs["name"])
        return clubs


def getSegmentLeaderboard(segment_id):
    leaderboard_url = 'https://www.strava.com/api/v3/segments/%s/leaderboard' % (segment_id)
    response = requests.get(leaderboard_url, headers=headers)
    leaderboard = response.json()
    entries = leaderboard['entries']
    for i in entries:
        print(i['athlete_name'])


def getActivities(athlete_id):
    activities_url = 'https://www.strava.com/api/v3/activities'
    response = requests.get(activities_url, headers=headers)
    activities = response.json()
    # for i in activities:
    #     print(i["id"], i["name"], i["type"], i["kudos_count"])
    return activities


def getFollowers(athlete_id):
    logging.info("running getFollowers")
    # athlete_url = 'https://www.strava.com/api/v3/athletes/%s' % athlete_id
    # ath_response = requests.get(athlete_url, headers=headers)
    # athlete = ath_response.json()
    # num_followers = str(athlete["follower_count"])
    # logging.info(num_followers)
    page = 1
    followers_url = 'https://www.strava.com/api/v3/athletes/%s/followers' % (athlete_id)
    length_of_data = 1
    while length_of_data > 0:
        logging.info(page)
        r2 = requests.get(followers_url, headers=headers, params={'page': page, 'per_page': 200})
        f2 = r2.json()
        length_of_data = len(f2)
        logging.info(len(f2))
        page = page + 1
        # followerids = []
        for f in f2:
            print(f["id"], f["firstname"], f["lastname"], f["city"], f["state"])
            # followerids.append(f['id'])
        # print(len(followerids))
        # return followerids


# club_id = getAthlete(athlete_id)
# getAthlete(athlete_id)
# getStats(athlete_id)
# getClubs(club_id)
# getActivities(athlete_id)
# getFollowers(athlete_id)
# getSegmentLeaderboard(3991086)
allEfforts(segment_id)
