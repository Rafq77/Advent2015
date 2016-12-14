import md5
import re
from itertools import compress

five = r"(0)\1{4}"
three = r"([a-z0-9])\1{2}"

string = "ngcjuoqr"
i = 0
cnt = 0
limit = 75 # little brute force
threes = []
lettersToRemove = ''
matchedIdx = []

task2 = True

while (cnt < limit):

    hsh = md5.new(string+str(i)).hexdigest()

    if task2:
        for s in xrange(2016):
          hsh = md5.new(hsh).hexdigest()

    #find fives
    for it in threes:              
        m = re.search(it[2], hsh)
        if m and matchedIdx.count(it[1]) == 0:
            matchedIdx.append(it[1])
            cnt += 1
            lettersToRemove += it[0]
            lastIdx = it[1]
            print(str(lastIdx) + "\t" + str(i))

    # remove matches of three older than 1000 iterations, not optimal
    threes = [it for it in threes  if it[1] + 1000 > i]

    #find threes
    match = re.search(three, hsh)
    if match:
        key = match.groups()[0]
        tple = (key, i, five.replace('0', key))
        threes.append( tple )
        
    i+=1

matchedIdx.sort()
print(matchedIdx[63])
    
