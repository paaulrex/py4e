# Exer 13

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    pid = js['results'][0]['place_id']
    print('Place id', pid)

    # print(json.dumps(js, indent=4))

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, "Constructed")

    def party(self):
        self.x += 1
        print(self.name, 'party count', self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points += 6
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal('Sally')
j = FootballFan('Jim')

s.party()
j.party()
j.touchdown()