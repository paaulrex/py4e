# Exer 9.4

msnt = dict()
lst = list()
fname = input('Enter file name:')
fh = open(fname)
for line in fh:
    lx = line.split()
    if len(lx) == 0 or lx[0] != 'From': 
        continue
    lst += [lx[1]]
for who in lst:
    msnt[who] = msnt.get(who,0) + 1   
topSender = None
numSends = None
for who,num in msnt.items():
    if numSends is None or num > numSends:
        topSender = who
        numSends = num
print(topSender, numSends)