import itertools
from collections import Counter
from copy import deepcopy
lines = open('Resources/Day_18.txt').read().split('\n')


tst = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.""".split('\n')

#lines = tst

maxX= len(lines[0])
maxY= len(lines)

def adjacent(x,y):
    return [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y+1), (x+1,y+1), (x+1,y), (x+1,y-1), (x,y-1)]

def pnt(karte):
    for i in karte:
        print(''.join(i))

def alg(karte, x,y):

    nbors = [karte[p[1]][p[0]] for p in adjacent(x,y)]
    p = karte[y][x]

    if p == '.':
        if nbors.count('|') >= 3:
            return '|'
        else:
            return '.'

    if p == '|':
        if nbors.count('#') >= 3:
            return '#'
        else: 
            return '|'
    
    elif p == '#' and nbors.count('|') >= 1 and nbors.count('#') >= 1:
        return '#'
    else:
        return '.'
    
    
# . open
# | tree
# # lumber

# . --> | if 3+ |
# | --> # if 3+ #
# # --> # if > 1 #  > 1 | 


borderH = [' ' for i in range(maxX+2)]
karte = []
karte.append(borderH.copy())

for line in lines:
    karte.append([' '] + list(line) + [' '])
karte.append(borderH.copy())


origin = (1,1)

#karte = [['.' for x in range(maxX)] for y in range(maxY)]

def save(karte):
    out = open("D:\\work\\tmp\\advent2018\\day18.txt",mode='w')
    for line in karte:
        out.write(''.join(line))
        out.write('\n')

def iteration(karte):
    newLife = deepcopy(karte)
    for y in range(1,maxY+1):
        for x in range(1,maxX+1):
            newLife[y][x] = alg(karte, x,y)

    return newLife

pnt(karte)

#part 1 - 456225
#for i in range(10):
#    karte = iteration(karte)
    #pnt(karte)

#
reps = ''
repsDb = []
it = 1000000000
for i in range(it):
    karte = iteration(karte)
    

    #if i % 1000:
    #print(i)
    #pnt(karte)
    #a = sum([row.count('|') for row in karte])
    #b = sum([row.count('#') for row in karte])
    #if a*b not in repsDb:
    #    repsDb.append(a*b)
    #    reps = ' '
    #else:
    #    reps = '+'
        
    #print(i,a,b,a*b,reps)


# there is a pattern:
# 1000 every 1k --> 192676, 198968, 207060, 212850, 199532, 191151, 224436,
# upon inspection the pattern repeats every 28 iterations long
#1000 000 000 % 28 = 20th... at 20th position of the frequency we got our number
# found an iteration that modulo 28 gives 20 (actually 19 because of indexing? - i was off by one) --> 190164
a = sum([row.count('|') for row in karte])
b = sum([row.count('#') for row in karte])
print(a,b,a*b)


















