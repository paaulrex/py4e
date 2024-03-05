# Exer 8.1

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
nlst = list()
for lx in fh:
    lx = lx.rstrip()
    lxs = lx.split()
    lst += lxs
for i in lst:
    if i not in nlst:
        nlst.append(i)
nlst.sort()
print(nlst)