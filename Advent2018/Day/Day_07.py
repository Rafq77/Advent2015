import itertools
lines = open('Resources/Day_07.txt').read().split('\n')

abc = [chr(i) for i in range(65,65+26)]
d = dict()
for c in abc:
    d[c] = ord(c) - 64
wrk = [ {}  for i in range(5) ] 

llines = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".split('\n')

tab = []
graph = {}
for each in lines:
    parts = each.split()
    con = (parts[1], parts[7])

    if parts[1] in graph:
        #print("A++ing " + parts[1] + " -> " + parts[7])
        graph[parts[1]].append(parts[7])
    else:
        #print("Adding " + parts[1] + " -> " + parts[7])
        graph[parts[1]] = list(parts[7])

#find start
inp = list(graph.keys())
from itertools import chain
vals = [i for i in chain.from_iterable(graph.values())]
stopNode = [c for c in set(vals) if c not in inp][0]
startNodes = [c for c in set(inp) if c not in set(vals)]


#attempt with networkx
import networkx as nx
import matplotlib.pyplot as plt

DG=nx.DiGraph()
[DG.add_node(n) for n in set(inp)]

for k,v in graph.items():
    [DG.add_edge(k,c) for c in v]


DGrev = DG.reverse()
#nx.draw(DG, with_labels=True)
#plt.show()

fN = [] #finished Nodes
aN = startNodes.copy() #availableNodes


while(len(aN) > 0):
    aN.sort()
    fN.append(aN.pop(0))
    for each in DG[fN[-1]]:
        # if all reverse graph inputs have been already added before to finished nodes, i.e. if they are done
        if all([True if revNode in fN else False for revNode in DGrev[each]]):
            if each not in aN:
                aN.append(each)
                
#part 1 = BCEFLDMQTXHZGKIASVJYORPUWN
print(''.join(fN))

#reset 4 part 2
fN = [] 
aN = startNodes.copy()
it = 0
while(len(aN) > 0 or any([i != {} for i in wrk])):
    aN.sort()

    # emulate time business
    # decrement if there are any digits not == 0
    if any([list(i.values())[0] > 0 for i in wrk if len(i) > 0]):
        while not any([list(i.values())[0] == 0 for i in wrk if len(i) > 0]):
            it += 1
            for each in wrk:
                for k,v in each.items():
                    each[k] -= 1
                    
            
    #finish jobs of workers
    for i in range(len(wrk)):
        if 0 in wrk[i].values():
            fN.append(list(wrk[i].keys())[0])
            wrk[i] = {}

            
            #cleanup, add letters from digits 0 to fN.append()
    if (len(fN) != 0):
        for each in DG[fN[-1]]:
            if all([True if revNode in fN else False for revNode in DGrev[each]]):
                if each not in aN:
                    aN.append(each)
    
    #find empty workers and give them job
    for each in wrk:
        if any([ True if len(i) == 0 else False for i in wrk ]):
            slot = wrk.index({})
            if (len(aN) > 0):
                l = aN.pop(0)
                wrk[slot] = {l: d[l] + 60 } # + 60

print(''.join(fN))
print(it)
