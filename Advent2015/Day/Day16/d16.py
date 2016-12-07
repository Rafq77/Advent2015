fd = open("""../../Resources/Day_16.txt""", 'r')
s = fd.read()
fd.close()
raw = s.split('\n')

search = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split('\n')

Search = { 'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1 } 

tmp = """(children: (?<chi>\d+))|
(cats: (?<cat>\d))|
(samoyeds: (?<sam>\d))|
(pomeranians: (?<cat>\d))|
(akitas: (?<cat>\d))|
(vizslas: (?<cat>\d))|
(goldfish: (?<cat>\d))|
(trees: (?<cat>\d))|
(cars: (?<cat>\d))|
(perfumes: (?<cat>\d))|"""


sues = []

class Sue:
    def __init__(self, children = 0, cats = 0, goldfish = 0, trees = 0, cars = 0, perfumes = 0):
        self.chi = children
        self.cat = cats
        self.gol = goldfish
        self.tre = trees
        self.car = cars
        self.per = perfumes
i = 1
for s in raw:
    idx = s.find(':')
    content = s[idx+2:]
    parts = content.split(',')
    sue = {}
    for p in parts:
        subParts = p.split(':')
        sue[subParts[0].lstrip(' ')] = int(subParts[1])
    sues.append(sue)

    trust = True
    for e in sue:
        # second solution
        if e == 'trees' or e == 'cats':
            if Search[e] >= sue[e]:
                trust = False
                break
        elif e == 'pomeranians' or e == 'goldfish':
            if Search[e] <= sue[e]:
                trust = False
                break
        elif Search[e] != sue[e]:
            trust = False
            break

    
        # this single if is enough for first solution
        #if Search[e] != sue[e]:
        #   trust = False
        #   break

    if trust == True:
        print("Match?")
        print(sue)
        print(i)

    i += 1


#s you're about to send the thank you note,
#something in the MFCSAM's instructions catches your eye.
#Apparently, it has an outdated retroencabulator,
#and so the output from the machine isn't exact values
#some of them indicate ranges.

#In particular, the #cats# and #trees# readings indicates that
#there are @greater@ than that many
#(due to the unpredictable nuclear decay of cat dander and tree pollen)
#while the #pomeranians# and #goldfish# readings indicate that there are @fewer@
#than that many (due to the modial interaction of magnetoreluctance).

#What is the number of the real Aunt Sue?

    
    
