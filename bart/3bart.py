import json
from urllib import request

key = 'MW9S-E7SL-26DU-VV8V'


def traincount():
    t_count = 'http://api.bart.gov/api/bsa.aspx?cmd=count&key=%s&json=y' % key
    get_count = request.urlopen(t_count).read()
    response = json.loads(get_count.decode('utf-8'))
    trains = response['root']['traincount']
    now = response['root']['time']
    return(trains)


def advisories():
    sa = 'http://api.bart.gov/api/bsa.aspx?cmd=bsa&key=%s&json=y' % key
    get_sa = request.urlopen(sa).read()
    response2 = json.loads(get_sa.decode('utf-8'))
    advisory = response2['root']['bsa'][0]['description']['#cdata-section']
    return(advisory)


def lambda_handler(event, context):
    # return(trains + ' active BART trains at ' + now + '. ' + advisory)
    # return(advisory)
    # print("Received event: " + json.dumps(event, indent=2))
    return(advisories())
