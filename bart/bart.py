# Simple script to play with the BART api

import requests

# Key and Developer Info at: http://api.bart.gov/docs/overview/index.aspx

key = 'MW9S-E7SL-26DU-VV8V'
t_count = 'http://api.bart.gov/api/bsa.aspx?cmd=count&key=%s&json=y' % key
get_count = requests.get(t_count)
response1 = get_count.json()
print(response1['root']['traincount'] + ' active BART trains at '
      + response1['root']['time'])

sa = 'http://api.bart.gov/api/bsa.aspx?cmd=bsa&key=%s&json=y' % key
get_sa = requests.get(sa)
response2 = get_sa.json()

print(response2['root']['bsa'][0]['description']['#cdata-section'])
