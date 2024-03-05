# Exer 13

import urllib.request, urllib.parse, urllib.error
import json

while True:
    url = input('Enter location:')
    if len(url) > 25:
        break
    else:
        print('Please enter valid location:')

print('Retrieving', url)
nurl = urllib.request.urlopen(url)
data = nurl.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
# print(json.dumps(js, indent=4))

lst = list()
count = 0
for i in js['comments']:
    lst += [int(i['count'])]
    count += 1
print('Count:', count)

slst = sum(lst)
print('Sum:', slst)