import itertools
from collections import Counter
lines = open('Resources/Day_06.txt').read().split('\n')

liness = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".split('\n')
#part 1 3449

InfinityEmulation = 4
Range = 400
totDist = 10000

ut = False
if ut:
    lines = liness
    Range = 10
    InfinityEmulation = 1
    totDist = 32
    
def manhattan(pos, x, y):
    #print(str(pos[0]) + '-' + 
    return abs(pos[0] - x) + abs(pos[1] - y)

coords = []
for each in lines:
    coords.append(tuple(map(lambda x: int(x), each.replace(',', '').split())))

distMap = [['.' for y in range(Range)] for x in range(Range)]
ddMap = [['.' for y in range(Range)] for x in range(Range)]


#the middle part could be counted once
for y in range(Range):
    for x in range(Range):

        distances = []
        # count the distance to point, for each coordinate
        # dist eq. length to no. of coordinates
        for each in coords:
             distances.append(manhattan(each, x,y))

        if (sum(distances) < totDist):
            ddMap[x][y] = '#'

        # count equal distances to coordinate
        c = Counter(distances)

        # check  if the shortest distance appears at most 1 time
        if c[min(c)] <= 1:
            distMap[x][y] = chr(97 + distances.index(min(c)))
        else:
            distMap[x][y] = '.'


c = Counter()
for i in distMap:
    c = Counter(i) + c

# border values are the closest ones, so they will be expanding to infty, no need to calc more. 
# check top/bottom/left/right
for i in range(len(distMap)):
    try:
        c.pop(distMap[i][0])
    except:
        continue
    
for i in range(len(distMap)):
    try:
        c.pop(distMap[0][i])
    except:
        continue

for i in range(len(distMap)):
    try:
        c.pop(distMap[len(distMap)-1][i])
    except:
        continue
    
for i in range(len(distMap)):
    try:
        c.pop(distMap[i][len(distMap)-1])
    except:
        continue

if ut:
    for i in distMap:
        print(''.join(i))

    print('')
    for i in ddMap:
        print(''.join(i))


#problem: in 300 iterations
#part 1
print(list(c.values())[0])

#problem: in 400 iterations
#part 2
print(sum([i.count('#') for i in ddMap]))
