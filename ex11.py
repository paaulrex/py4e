# Exer 11

import re

su = list()
fn = input('Enter filename:')
fh = open(fn).read()
x = re.findall('[0-9]+',fh)
for i in x:
    su += [int(i)]
ttl = sum(su)
print(ttl)