# Exer 12

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL:')
# url = 'http://py4e-data.dr-chuck.net/known_by_Sidra.html'
pos = int(input('Enter position:'))
scount = int(input('Enter count:'))

for i in range(scount):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    fst = soup('a')
    count = 0
    for lx in fst:
        count += 1
        if count > pos:
            break
        url = lx.get('href', None)
    print('Retrieving:',url)