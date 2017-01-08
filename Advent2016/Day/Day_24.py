import itertools
import collections
fd = open("""../Resources/Day_24.txt""",'r')
s = fd.read()
fd.close()
S = s

tab = s.split('\n')
coords = {}
for row in range(len(tab)):
        #paint
        print(tab[row])
        for i in range(8):
                idx = tab[row].find(str(i))
                if (idx != -1):
                        #print("Found " + str(i) + " at " +  str(row) + ',' + str(idx))
                        coords[i] = (row,idx)

possibleConnections =list(itertools.combinations(coords,2))

wall = '#'
maxLen = 255
results = []

def findExit(end, nodesToVisit):
        # nodesToVisit contains entry point as beginning
        # tab my table
        # wall = '#'
        nodesVisited = set()
        nodesToVisit = collections.deque(nodesToVisit)
        path = ''
        foundExit = False
        while nodesToVisit:
            #print(len(nodesToVisit))

            #BFS
            path = nodesToVisit.popleft()
            #DFS
            #path = nodesToVisit.pop()
            
            node = path[-1] #last elem 
            
            if node == end: 
                print("FOUND SMTH")
                print(len(path))
                foundExit = True
                return path
              
        
            l = (node[0], node[1]-1)
            r = (node[0], node[1]+1)
            u = (node[0]-1, node[1])
            d = (node[0]+1, node[1])
            
            if (tab[l[0]][l[1]]) != wall and\
               l not in nodesVisited:
                nPath = list(path)
                nPath.append(l)
                nodesToVisit.append(nPath)
                
            if (tab[r[0]][r[1]]) != wall and\
               r not in nodesVisited:
                nPath = list(path)
                nPath.append(r)
                nodesToVisit.append(nPath)
                
            if (tab[u[0]][u[1]]) != wall and\
               u not in nodesVisited:
                nPath = list(path)
                nPath.append(u)
                nodesToVisit.append(nPath)
                
            if (tab[d[0]][d[1]]) != wall and\
               d not in nodesVisited:
                nPath = list(path)
                nPath.append(d)
                nodesToVisit.append(nPath)
            
            nodesVisited.add(node)
        
        return nodesVisited
               
                

#visited = findExit(coords[1], [[coords[0]]])
# 430 because bruteforce
# 23 + 65 + 33 + 81 + 21 + 207
# 700 bruteforced too
possibleConnections = [(0, 1), (1,7), (0,7),(1, 3), (2,3), (2, 4), (4, 5), (5, 6), (6, 7)]
for perm in possibleConnections:
        beg = coords[perm[0]]
        end = coords[perm[1]]
        pth = findExit(end, [[beg]])

        print("Path from " + str(perm[0])  + " to " + str(perm[1]) + " takes " + str(len(pth)))

        

        
