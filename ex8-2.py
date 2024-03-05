# Exer 8.2

fname = input('Enter file name: ')
fh = open(fname)
count = 0
for line in fh:
    lx = line.split()
    if len(lx) == 0 : continue
    if lx[0] != 'From' : continue
    count += 1
    print(lx[1])
print('There were', count, 'lines in the file with From as the first word')