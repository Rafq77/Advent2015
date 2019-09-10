fd = open("""../Resources/Day_22.txt""", 'r')
lines = fd.read().split('\n')

from collections import deque
import numpy as np
import math


#def strToArray(s):
#    return np.array([[int(c) for c in i] for i in s.replace('.','0').replace('#','1').split('/')])
        
direction = deque('urdl')
it = 10000

#UNIT TESTS
ut = ["..#", "#..", "..."]


#TODO DISABLE UT
#lines = ut
#it = 70 #infectionCount 41
#it = 10000 #5587 ifectionsCount

virusMap = set()
y = int(len(lines)/2)
x = int(len(lines[y])/2)

for yi in range(len(lines)):
    for xi in range(len(lines[yi])):
        if lines[yi][xi] == '#':
            virusMap.add((xi,yi))

infectionCount = 0
for i in range(it):
    # inf/clean
    if (x,y) in virusMap:
        virusMap.remove((x,y))
        direction.rotate(-1) #rotate right
    else:
        virusMap.add((x,y))
        infectionCount += 1
        direction.rotate(1) #rotate left

    if direction[0] == 'u':
        y -= 1
    elif direction[0] == 'r':
        x += 1
    elif direction[0] == 'd':
        y += 1
    elif direction[0] == 'l':
        x -= 1
    
print("infectionCount " + str(infectionCount))
print("infectedFieldsCount " + str(len(virusMap)))

#reinit for part2:
direction = deque('urdl')
weakMap = set()
infectedMap = set()
flaggedMap = set()
#UNIT TEST LINE BELOW
#lines = ut
it = 10000000
infectionCount = 0
y = int(len(lines)/2)
x = int(len(lines[y])/2)
for yi in range(len(lines)):
    for xi in range(len(lines[yi])):
        if lines[yi][xi] == '#':
            infectedMap.add((xi,yi))


for i in range(it):

    if i%1000000==0:
        print(i)
    if (x,y) in infectedMap: # inf --> flagged
        infectedMap.remove((x,y))
        flaggedMap.add((x,y))
        direction.rotate(-1) #rotate right
    elif (x,y) in weakMap: #weak --> infected
        weakMap.remove((x,y))
        infectionCount += 1
        infectedMap.add((x,y))
        #no turn
    elif (x,y) in flaggedMap: #flg --> clean
        flaggedMap.remove((x,y))
        direction.rotate(2) #rotate back
    else: #clean --> weak
        weakMap.add((x,y))
        direction.rotate(1) #rotate left

    if direction[0] == 'u':
        y -= 1
    elif direction[0] == 'r':
        x += 1
    elif direction[0] == 'd':
        y += 1
    elif direction[0] == 'l':
        x -= 1

print("infectionCount " + str(infectionCount))
#print("infectedFieldsCount " + str(len(infectedMap) + len(flaggedMap)))
        
