fd = open("""Resources/Day_12.txt""", 'r')
lines = fd.read().split('\n')

midSplit = (' <-> ')
rSplit = (', ')

pipes = set()
pipes.add(0)

pool = list()
numbers = list()

ut = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""
#lines = ut.split('\n')

class Node:
    def __init__(self):
        self.name = -1
        self.parent = None
        self.children = set()
        self.childrenNames = set()

        self.Finished = False # children are not ready  

for line in lines:
    lin = line.split(midSplit)

    l = int(lin[0])
    r = list(map(lambda x: int(x), lin[1].split(rSplit)))

    numb = set(r)
    numb.add(l)
    
    numbers.append(numb)

    n = Node()
    n.name = l
    n.childrenNames = set(r)

    pool.append(n)


#take 0
p = pool[0]
out = list()
visited = set()
def recurse(node):

    visited.add(node.name)

    for each in node.childrenNames:
        child = next(filter(lambda x: x.name == each, pool))
        
        child.parent = node
        node.children.add(child)
        out.append(child)
        if child.name not in visited:
            recurse(child)
        
        
    node.Finished = True
    
recurse(p)

names = list()
names = [i.name for i in out]
print(len(set(names)))


#cheat
iset = set([frozenset(s) for s in numbers])  # Convert to a set of sets
result = []
while(iset):                  # While there are sets left to process:
    nset = set(iset.pop())      # Pop a new set
    check = len(iset)           # Does iset contain more sets
    while check:                # Until no more sets to check:
        check = False
        for s in iset.copy():       # For each other set:
            if nset.intersection(s):  # if they intersect:
                check = True            # Must recheck previous sets
                iset.remove(s)          # Remove it from remaining sets
                nset.update(s)          # Add it to the current set
    result.append(tuple(nset))  # Convert back to a list of tuples

print(len(result))


#show graph
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph of programs
graph = nx.Graph()

for line in lines:
    # Parse the line
    node, neighbors = line.split(' <-> ')

    # Add edges defined by this line
    graph.add_edges_from((node, neighbor) for neighbor in neighbors.split(', '))
