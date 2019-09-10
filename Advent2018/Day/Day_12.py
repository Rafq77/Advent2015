from collections import deque
from collections import defaultdict
import itertools as it
initSt = """..#..###...#####.#.#...####.#..####..###.##.#.#.##.#....#....#.####...#....###.###..##.#....#######"""
rules = """..### => .
.##.# => #
#..#. => .
#.#.# => #
###.. => #
.#..# => .
##..# => #
.###. => #
..#.. => .
..... => .
##### => .
.#... => #
...#. => #
#...# => #
####. => .
.#### => .
##.## => #
...## => .
..##. => .
#.##. => .
#.... => .
.#.#. => .
..#.# => #
#.#.. => #
##... => #
##.#. => .
#..## => .
.##.. => .
#.### => .
....# => .
.#.## => #
###.# => #""".split('\n')

ut = False
if ut:
    initSt = """#..#.#..##......###...###"""
    rules = """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #""".split('\n')

def sumIndices(pots, offset):
    return sum([i-offset for i in range(len(pots)) if pots[i] == '#'])

offset = int(len(initSt)/5)
offset = 5
pots =  [ '.' for i in range(offset) ]
pots = ''.join(pots) + initSt + ''.join(pots)

r = defaultdict()
for e in [''.join(i) for i in it.product(['.','#'], repeat=5)]:
    r[e] = '.'

for rule in rules:
    p = rule.split(' => ')
    r[p[0]] = p[1]
rules = r

#out = open("D:\\work\\tmp\\advent2018\\day12.txt",mode='w')
def grow(generations, rules, pots):
    nSum = 0
    for i in range(generations): #generations
        #if i % 100 == 0:
        #    print(sum([1 for i in pots if i == '#']))
        #print(pots)
        #out.write(pots)
        #out.write('\n')
            #print(i)
        newPots = deque(['.','.'])
        for j in range(2,len(pots)-3):
            sub = pots[j-2:j+3]
            newPots.append(rules[sub])
            
        [newPots.append('.') for i in range(4)]
        pots = ''.join(newPots)

        lSum = nSum 
        nSum = sumIndices(pots, offset)
        #print(nSum - lSum) #53 later on
    #out.close()
    return pots, nSum-lSum

potsSmall, diff = grow(20, rules, pots)
print("part1: " + str(sumIndices(potsSmall,offset)))

#ooof!!!
#50000000000
oof = 50000000000
its = 400

pots, diff = grow(its, rules, pots) #53 '#' is the diff.
#sum is 22562 after 400.
togo = oof - its
print("part2: " + str(sumIndices(pots,offset)+diff*togo))



        
    


    
