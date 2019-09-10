import math
import itertools
import networkx as nx
import matplotlib.pyplot as plt
import operator
from collections import deque
import re

raw = open("Day_16.txt").read()

reg = [0 for i in range(4)]
opScores = [0 for i in range(16)]

def addr(a,b):
    global reg
    return reg[a]+reg[b]

def addi(a,b):
    global reg
    return reg[a]+b

def mulr(a,b):
    global reg
    return reg[a]*reg[b]

def muli(a,b):
    global reg
    return reg[a]*b

def banr(a,b):
    global reg
    return reg[a] & reg[b]

def bani(a,b):
    global reg
    return reg[a] & b

def borr(a,b):
    global reg
    return reg[a] | reg[b]

def bori(a,b):
    global reg
    return reg[a] | b

def setr(a,b):
    global reg
    return reg[a]

def seti(a,b):
    global reg
    return a

def gtir(a,b):
    global reg
    return 1 if a > reg[b] else 0
def gtri(a,b):
    global reg
    return 1 if reg[a] > b else 0
def gtrr(a,b):
    global reg
    return 1 if reg[a] > reg[b] else 0

def eqir(a,b):
    global reg
    return 1 if a == reg[b] else 0
def eqri(a,b):
    global reg
    return 1 if reg[a] == b else 0
def eqrr(a,b):
    global reg
    return 1 if reg[a] == reg[b] else 0



operations = [addr
,addi
,mulr
,muli
,banr
,bani
,borr
,bori
,setr
,seti
,gtir
,gtri
,gtrr
,eqir
,eqri
,eqrr
]


candidates = dict().fromkeys(operations)
for k in candidates.keys():
    candidates[k]= [0 for i in range(16)]
    

def testExample(before, after, instr):
    global operations
    global reg
    opcode, a, b, c = instr
    initialState = before
    expected = after 
    idx = 0
    opScores = [i for i in range(16)]

    for op in operations:
        reg = initialState.copy()
        reg[c] = op(a,b)
        #op(reg,a,b,c)

        if expected == reg:
            #opScores[idx] += 1
            idx+=1
            candidates[op][opcode]+=1 
        else:
            candidates[op][opcode]-=1 
            #try:
                #opScores.remove(opcode)
            #except ValueError as Err:
                #s = 1

        


    #part1 3 or more    
    
    #if sum(opScores) > 3:
    if idx >= 3:
        #print(opScores, sum(opScores), '+')
        return True
    else:
        #print(opScores, sum(opScores))
        return False
    
#testExample([3,2,1,1],[3,2,2,1],"9 2 1 2")

tst = raw.split('\n\n')
inst = tst[-1].split('\n')
tst = tst[:-2]
moreThan3 = 0

for t in tst:
    bef, ins, aft = t.split('\n')
    b = list(map(int,bef.split(': [')[1][:-1].split(',')))
    i = list(map(int, ins.split()))
    a = list(map(int,aft.split(':  [')[1][:-1].split(',')))

    if testExample(b, a, i):
        moreThan3 += 1


#part 1 - 642
print(moreThan3)

#part2 this was to manual, how to make it manual - one loop is missing that i did manually. 

#muli -> 6
#addr -> 12
#addi -> 1
#bori -> 8
#borr -> 14
#setr -> 3
#mulr -> 4
#seti -> 5
#banr -> 15
#bani -> 9 ##
#gtir -> 2
#gtrr -> 10
#gtri -> 13
#eqrr -> 11
#eqri -> 7
#eqir -> 0

ops = [ eqir, addi, gtir, setr, mulr, seti, muli, eqri, bori, bani, gtrr, eqrr, addr, gtri, borr, banr ]

candidates = dict().fromkeys(operations)
for k in candidates.keys():
    candidates[k]= [0 for i in range(16)]
    candidates[k][6] = -200
    candidates[k][12] = -200
    candidates[k][1] = -200
    candidates[k][8] = -200
    candidates[k][14] = -200
    candidates[k][3] = -200
    candidates[k][4] = -200
    candidates[k][5] = -200
    candidates[k][15] = -200
    candidates[k][9] = -200##
    candidates[k][2] = -200
    candidates[k][10] = -200
    candidates[k][13] = -200
    candidates[k][11] = -200
    candidates[k][7] = -200
    candidates[k][0] = -200
    
    
for t in tst:
    bef, ins, aft = t.split('\n')
    b = list(map(int,bef.split(': [')[1][:-1].split(',')))
    i = list(map(int, ins.split()))
    a = list(map(int,aft.split(':  [')[1][:-1].split(',')))

    if testExample(b, a, i):
        moreThan3 += 1

for k,v in candidates.items():
    print(k.__name__, v.index(max(v)), [i for i in v if i > 0])

reg = [0,0,0,0]
for i in inst:
    opcode, a, b, c = list(map(int, i.split()))

    reg[c] = ops[opcode](a,b)

print(reg[0]) #part 2 - 481
