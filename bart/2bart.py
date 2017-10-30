import json
from urllib import request

event = "t"


def lambda_handler(event, context):
    key = 'MW9S-E7SL-26DU-VV8V'
    t_count = 'http://api.bart.gov/api/bsa.aspx?cmd=count&key=%s&json=y' % key
    get_count = request.urlopen(t_count).read()
    response = json.loads(get_count.decode('utf-8'))
    trains = response['root']['traincount']
    now = response['root']['time']
    # print("Received event: " + json.dumps(event, indent=2))
    # return(trains)
    return(trains + ' active BART trains at ' + now)
