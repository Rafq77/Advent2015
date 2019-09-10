import math
import itertools
import networkx as nx
import matplotlib.pyplot as plt
import operator
from collections import deque
import re

program = open("Resources/Day_21.txt").read().split('\n')

regWidth = 6
reg = [0 for i in range(6)]
opScores = [0 for i in range(16)]


_program = """#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5""".split('\n')

ip = int(program[0].split()[1])
program = program[1:]


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



operations = { "addr" :addr
,"addi" : addi
,"mulr" : mulr
,"muli" : muli
,"banr" : banr
,"bani" : bani
,"borr" : borr
,"bori" : bori
,"setr" : setr
,"seti" : seti
,"gtir" : gtir
,"gtri" : gtri
,"gtrr" : gtrr
,"eqir" : eqir
,"eqri" : eqri
,"eqrr" : eqrr
}


prog = []
for instr in program:
    opcode, a, b, c = instr.split()
    ops = list(map(int, [a,b,c]))
    prog.append([operations[opcode]] + ops)
    

# method copied from internets (was lazy to write) get the sum of divisiors of the last register value (which is being generated at the beginning)
# p1 --> sum of divisiors of 955 is 1152
# p2 --> sum of divisiors of 10551356 is 12690000
def getDivisors(n):
 if n == 1:
  return [1]

 max = n
 num = 2
 result = [1, n]

 while num < max:
  if not n % num:
   if num != n/num:
    result.extend([num, n//num])
   else:
    result.append(num)
   max = n//num
  num += 1
 return sorted(result)



#part 2
#reg[0] = 1
lenP = len(prog)
reg[0] = 0
print("Using instruction pointer registry No.", ip)
sleep=0
sleepB = 0
while reg[ip] < len(prog):
    print(prog[reg[ip]], reg)
    reg[prog[reg[ip]][3]] = prog[reg[ip]][0](prog[reg[ip]][1],prog[reg[ip]][2])
    
    #    print(reg,"HACKING")
    reg[ip] += 1


#part 1 - 1152
#reg[1] = 0
#print("Using instruction pointer registry No.", ip)
#while reg[ip] < len(program):
    #print(program[reg[ip]], reg)
#   opcode, a, b, c = program[reg[ip]].split()
#    a,b,c = map(int, [a,b,c])
#    reg[c] = operations[opcode](a,b)
#    reg[ip] += 1
    

print(reg[0]) #part 2 - 481
