import re
from itertools import compress

fd = open("""../Resources/Day_15.txt""", 'r')
s = fd.read()
fd.close()
s = s.split('\n')
S = s

class Disc():
    actPos = 0
    positions = 0
    id = 0

discs = []

for i in s:
    parts = i[:-1].split(' ')

    disc = Disc()
    disc.actPos = int(parts[11])
    disc.id = int(parts[1][1:])
    disc.positions = int(parts[3])
    discs.append(disc)

for disc in discs:
    print("D[" + str(disc.id) + "] pos:" + str(disc.actPos) + "/" + str(disc.positions))


def DoMagic(discs):

    t = 0
    done = False
    while(not done):
        done = True
        for disc in discs:
            time = disc.id+t
            if ((time+disc.actPos)%disc.positions):
                done = False
                break #breaks only one loop
        t += 1

    return t-1

out = DoMagic(discs)
print(out)


extraDisc = Disc()
extraDisc.id = len(discs)+1
extraDisc.actPos = 0
extraDisc.positions = 11
discs.append(extraDisc)

out = DoMagic(discs)
print(out)



