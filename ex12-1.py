# Exer 12

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

lst = list()
url = 'http://py4e-data.dr-chuck.net/comments_1936560.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

spans = soup('span')
for line in spans:
    # print(line.contents)
    for i in line.contents:
        lst += [int(i)]
slst = sum(lst)
print(slst)