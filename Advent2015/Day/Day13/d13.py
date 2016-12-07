fd = open("""../../Resources/Day_13.txt""", 'r')
raw = fd.read()
fd.close()
raw = raw.replace('.','').split('\n')

shelv = [ 'Alice', 'Bob', 'Carol', 'David', 'Eric', 'Frank', 'George', 'Mallory', 'Raf' ]

#prep
d= {}
for i in shelv:
    d[i] = {}

import re
import itertools
perms = list(itertools.permutations(shelv))

firstNamePattern = r"^\w+"
secondNamePattern = r"\w+$"

fnp = re.compile(firstNamePattern)
snp = re.compile(secondNamePattern)
digit = re.compile(r"\d+")

for i in raw:
    n1 = fnp.search(i).group()
    n2 = snp.search(i).group()
    n = digit.search(i).group()

    if i.count("gain") > 0: #positive; add
        d[n1][n2] = int(n)
    else:
        d[n1][n2] = int(n) * -1

#rdy
results = {}
Max = 0
MaxSet = 0
for i in perms:
    total = 0

    for nIdx in range(len(i) - 1):
        total += d[i[nIdx]][i[nIdx+1]]
        total += d[i[nIdx + 1]][i[nIdx]]

    # close the circle
    total += d[i[0]][i[-1]]
    total += d[i[-1]][i[0]]

    results[i] = total
    if Max < total:
        Max = total
        MaxSet = i
        print(Max)


    
