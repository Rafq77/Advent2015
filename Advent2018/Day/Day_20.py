import math
import itertools
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import re

sentence = open("Resources/Day_20.txt").read()
paths = []
stack = []

tst0="""^ENWWW(NEEE|SSE(EE|N))$"""
tst1="""^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"""
tst2="""^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"""
tst3="""^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"""

tst = tst1
tst = sentence
string = tst[1:-1]
deepness = 0


# a parenthesis is alawys a branch with 2

def prints(s):
    for i in s:
        print(''.join(i))

def nxt(p , c):
    if c == 'N':
        return (p[0], p[1]+1)
    elif c == 'W':
        return (p[0]-1, p[1])
    elif c == 'S':
        return (p[0], p[1]-1)
    elif c == 'E':
        return (p[0]+1, p[1])

class Node:
    def __init__(self, label, left=None, right=None, parent=None):
        self.lbl = label
        self.l = left
        self.r = right
        self.p = parent

    def __repr__(self):
        return self.repr()

    def p(self):        
        print(self.l, ' <-- ', self.lbl, ' --> ', self.r, ' p:', self.p)
        
    def repr(self):
        return self.lbl

    def repr2(self):
        l = ''
        r = ''
        p = ''
        if self.l is not None:
            l = self.l.lbl
        if self.r is not None:
            r = self.r.lbl
        if self.p is not None:
            p = self.p.lbl
        return str(l) + ' <-- ' + self.lbl + ' --> ' + str(r) + ' p:' + str(p)
    
def go(string):

    path = []
    nodes = []
    root = None
    curNode = None
    special = False #used to ignore fake pops
    ignoreOnce = False
    space = ''
    G = nx.DiGraph()
    
    for i in range(len(string)):
        if string[i] == '(':
            #check if this is a "special case" to just include
            nxtSep = string.find('|', i)
            if string[nxtSep+1] == ')' and nxtSep < string.find('(',i+1):
                special = True
                continue
            space += ' '
            p = ''.join(path)

            n = Node(p)
            if not root:
                root = n
                G.add_node(n)
                gR = n
                curNode = n
            else:
                n.p = curNode 
                parentNode = curNode
                
                #curNode = n
                if parentNode.l == None:
                    parentNode.l = n
                    G.add_edge(parentNode, n)
                elif parentNode.r == None:
                    parentNode.r = n
                    G.add_edge(parentNode, n)
                else:
                    print("you shouldn't get here!", i)
                curNode = n
            path = []
            
        elif string[i] == ')':
            if special:
                special = False
            else:
                if len(path) > 0:
                    curNode.r = Node(''.join(path), parent=curNode)
                    G.add_edge(curNode, curNode.r)
                
                curNode = curNode.p #pop
                path = []
        elif string[i] == '|':
            if special:
                continue
            if len(path) > 0:
                curNode.l = Node(''.join(path), parent=curNode)
                G.add_edge(curNode, curNode.l)
            path = []
        else:
            path.append(string[i])
    print(''.join(path))
    return root, G
    
    
r, g  = go(string)
#nx.draw(g, with_labels=True)
#plt.show()

nx.algorithms.shortest_path_length(g,r)
for node in g:
    if g.out_degree(node)==0: #it's a leaf
        paths.append(nx.shortest_path(g, r, node))

start = (0,0)
G = nx.Graph()
print(len(paths))
for p in paths:
    path = ''.join([i.lbl for i in p])

    coords = start
    for d in path:
        nCoords = nxt(coords , d)
        G.add_edge(coords, nCoords)
        coords = nCoords

shortestPaths = nx.algorithms.shortest_path_length(G,start).values()
#part1  - 3560
print("part1:", max(shortestPaths))

#part2 - 8688
print("part2:", sum(1 for length in shortestPaths if length >= 1000))


