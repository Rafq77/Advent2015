fd = open("""../Resources/Day_16.txt""", 'r')
src = fd.read()
fd.close()

"""
Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
Exchange, written xA/B, makes the programs at positions A and B swap places.
Partner, written pA/B, makes the programs named A and B swap places.
For example, with only five programs standing in a line (abcde), they could do the following dance:

s1, a spin of size 1: eabcd.
x3/4, swapping the last two programs: eabdc.
pe/b, swapping programs e and b: baedc.

"""

#Utility
from collections import deque
#d = deque(list)
#d.rotate

ut = ['a','b','c','d','e']
instrUt = [ "s1", "x3/4", "pe/b"]

def move(cmd, lst):
    e = cmd[0]
    if e == 's': # spin
        #rotate(dancefloor, int(each[1:]))
        lst.rotate(int(cmd[1:]))
    elif e == 'x': # exchange indexes
        p2 = cmd[1:]
        l = int(p2.split(sep)[0])
        r = int(p2.split(sep)[1])

        tmp = lst[r]
        lst[r] = lst[l]
        lst[l] = tmp
        
    elif e == 'p' : # exchange letters
        p2 = cmd[1:]
        l = p2.split(sep)[0]
        r = p2.split(sep)[1]
        li = lst.index(l)
        ri = lst.index(r)

        tmp = lst[ri]
        lst[ri] = lst[li]
        lst[li] = tmp

instr = src.replace('\n','').split(',')
sep = '/'

a = ord('a')
dancefloor = list()

for i in range(16):
    dancefloor.append(chr(a+i))

#unit tests
#dancefloor = ut
#instr = instrUt

dancefloor = deque(dancefloor)

seen = list()
seen.append(''.join(dancefloor)) # important for p2. base arrangement also counts!
for each in instr:
    move(each,dancefloor)
    
#part1
print("".join(dancefloor))
spinRoundRound = len(instr)

#key
k = "gjmiofcnaehpdlbk"
bio = 1000000000
print("dance!")
#lets dance!
for i in range(bio): # 1 billion

    h = ''.join(tuple(dancefloor.copy()))
    if h in seen: # find repetition
        print("FOUND IT!")
        break
    seen.append(h)

    for each in instr:
        move(each,dancefloor)
      
#part2
print(''.join(seen[bio % len(seen)]))
