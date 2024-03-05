# Exer 10.2

fname = input('Enter file:')
fh = open(fname)
di = dict()
lst = list()
for lx in fh:
    lx = lx.rstrip()
    lx = lx.split()
    if len(lx) == 0 or lx[0] != 'From':
        continue
    time = lx[5]
    tx = [time[:2]]
    for hr in tx:
        di[hr] = di.get(hr, 0) + 1
for x,y in di.items():
    lst.append((x,y))
lst = sorted(lst)
for x,y in lst:
    print(x,y)