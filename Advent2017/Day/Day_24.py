fd = open("""../Resources/Day_24.txt""", 'r')
src = fd.read()
fd.close()

lines = src.split('\n')
print("Length: " + str(len(lines)))

components = list()
for each in lines:
    p1, p2 = each.split('/')
    components.append((int(p1), int(p2)))

import itertools
import collections
components.sort()

#for c in components:
#    print(c)


def rec(tupList):
    #print(tupList)
    last = tupList[-1]
    candidates = list(filter(lambda x: x[0] == last[1] or x[1] == last[1], components))

    for c in candidates:
        if c not in tupList and c[::-1] not in tupList:
        #if c not in tupList:
            
            tmp = tupList.copy()
            if c[1] == tmp[-1][1]: #rotate                
                tmp.append(c[::-1])
            else:
                tmp.append(c)
            yield tmp
            yield from rec(tmp)
            
    return tupList

koth = 0
kothLen = 0
kothLenS = 0
for e in components:
    if e[0] == 0:
        l = list()
        l.append(e)
        
        for each in rec(l):
            #print(each)
            s = sum([sum(t) for t in each])
            if s > koth:
                koth = s
            l = len(each)
            if l > kothLen:
                kothLen = l
                kothLenS = s
