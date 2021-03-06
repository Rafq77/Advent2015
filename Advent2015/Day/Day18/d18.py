﻿#- Day 18: Like a GIF For Your Yard ---
#After the million lights incident, the fire code has gotten stricter:
#now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

#Never one to let you down,
#Santa again mails you instructions on the ideal lighting configuration.
#With so few lights, he says, you'll have to resort to animation.

#Start by setting your lights to the included initial configuration
#your puzzle input).
#A # means "on", and a . means "off".

#Then, animate your grid in steps,
#where each step decides the next configuration based on the current one.
#Each light's next state (either on or off) depends on its current state
#and the current states of the eight lights adjacent to it (including diagonals).
#Lights on the edge of the grid might have fewer than eight neighbors;
#the missing ones always count as "off".

#For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

#1B5...
#234...
#......
#..123.
#..8A4.
#..765.
#The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

#A light which is on stays on when 2 OR 3 neighbors are on, and turns off otherwise.
#A light which is off turns on if EXACTLY 3 neighbors are on, and stays off otherwise.
#All of the lights update simultaneously; they all consider the same current state before moving to the next.

#Here's a few steps from an example configuration of another 6x6 grid:

#Initial state:
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..

#After 1 step:
# ..##..
# ..##.#
# ...##.
# ......
# .....
# .##..
#
#After 2 steps:
# ..###.
# ......
# ..###.
# ......
# .#....
# .#....
#
#After 3 steps:
# ...#..
# ......
# ...#..
# ..##..
# ......
# ......
#
#After 4 steps:
# ......
# ......
# ..##..
# ..##..
# ......
# ......

#After 4 steps, this example has four lights on.

tst = """.#.#.#
...##.
#....#
..#...
#.#..#
####..""".split('\n')

#how many lights are on after 100 steps?

fd = open("""../../Resources/Day_18.txt""", 'r')
s = fd.read()
fd.close()
raw = s.split('\n')


import copy

def Copy2DList(IN):
    OUT = []
    for i in IN:
        OUT.append(list(i))
    return OUT

def CntNeighbours(_out, x,y):
    
    cnt = 0
    l = True
    r = True
    t = True
    b = True

    if y == 0:
        t = False
        #print('t')
    if y+1 == len(_out):
        b = False
        #print('b')
    if x == 0:
        l = False
        #print('l')
    if x+1 == len(_out):
        r = False
        #print('r')
    
    if t and _out[y-1][x] == '#':
        cnt+=1
    #    print('^')
    if t and l and _out[y-1][x-1] == '#':
        cnt+=1
    #    print('^\\')
    if l and _out[y][x-1] == '#':
        cnt+=1
   #     print('<-')
    if b and l and _out[y+1][x-1] == '#':
        cnt+=1
    #    print('v/')
    if b and _out[y+1][x] == '#':
        cnt+=1
     #   print('v')
    if b and r and _out[y+1][x+1] == '#':
        cnt+=1
     #   print('\\v')
    if r and _out[y][x+1] == '#':
        cnt+=1
     #   print('->')
    if t and r and _out[y-1][x+1] == '#':
        cnt+=1
       # print('/^')

    return cnt

size = [6,6]
size = [100,100]


#raw = tst
#Prepare
out = []
outNew = []
for i in raw:
    out.append(list(i))
outNew = Copy2DList(out)

for i in range(100):
#for i in range(6):
    for y in range(size[0]):
        for x in range(size[1]):
            
            nb = CntNeighbours(out, x,y)
            s = ''

            if nb == 3 and out[y][x] == '.':
                outNew[y][x] = '#'      #switch on
                s = "on"
            elif out[y][x] == '#' and (nb == 3 or nb == 2):
                outNew[y][x] = '#'         #no need to be effective
                s = "remain"
            else:
                outNew[y][x] = '.'         #switch off
                s = "off"

            #p 2
            outNew[0][0] = '#'
            outNew[0][99] = '#'
            outNew[99][0] = '#'
            outNew[99][99] = '#'
            
            #print("x= " + str(x) + " y=" + str(y) + " nb=" + str(nb) + " " + s)
        
        #print("".join(out[y]))
    out = Copy2DList(outNew)
    #print("")

print (sum([i.count('#') for i in out]))

#first run 1061
#secon run 1006
