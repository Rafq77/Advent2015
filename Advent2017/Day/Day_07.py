#jump instructions

#python 3.4.2
import numpy

r = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj cntj xhth
qoyq (66)
padx (45) -> pbga havc qoyq
tknk (41) -> ugml padx fwft
jptl (61)
ugml (68) -> gyxo ebii jptl
gyxo (61)
cntj (57)"""

fd = open("""Resources/Day_07.txt""", 'r')

nodes = fd.read().replace(',','').split()

unique = numpy.unique(r.split(), return_counts=True)
pairs = zip(unique[0].tolist(), unique[1].tolist())
[i for i in pairs if i[1]==1]

unique = numpy.unique(nodes, return_counts=True)
pairs = zip(unique[0].tolist(), unique[1].tolist())

# take last from zipped list, its the unique word that appears only once (root of the tree)
[i for i in zip(unique[0].tolist(), unique[1].tolist()) if i[1]==1][-1]


    
    


