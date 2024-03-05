# Exer 13

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lst = list()

while True:
    url = input('Enter location:')
    if len(url) > 25:
        break
    else:
        print('Please enter a valid url')
print('Retrieving', url)

html = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(html), 'characters')

tree = ET.fromstring(html)
counts = tree.findall('.//comment')
print('Count:', len(counts))

for i in counts:
    count = i.find('count').text
    lst += [int(count)]
slst = sum(lst)
print('Sum:', slst)