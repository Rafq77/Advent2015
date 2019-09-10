from collections import deque
from collections import defaultdict
import itertools as it
lines = open('Resources/Day_13.txt').read().split('\n')

tst ="""/->-\         
|   |  /----\ 
| /-+--+-\  |  
| | |  | v  | 
\-+-/  \-+--/  
  \------/   """.split('\n')


tst2="""/>-<\   
|   |    
| /<+-\  
| | | v  
\>+</ |  
  |   ^  
  \<->/ """.split('\n')

#lines = tst2
#lines[y][x]

direction = ['u','d','l','r']
rotation = deque(['l','s','r'])
cart = ['v','>','^','<']
cartDict = { 'v': '|', '>':'-', '<':'-', '^':'|' }
turns = ['\\','/']
turnDict = { '>\\' : 'v', '>/': '^', 'v/' : '<', '^\\' : '<',  'v\\': '>' , '</':'v', '^/':'>', '<\\' :'^' }
cartMap = [ [' ' for y in x] for x in lines]
cartRotations = []


class Cart:
    def __init__(self, x,y, rotation):
        self.x = x
        self.y = y
        self.rotation = rotation.copy()
        self.rotation.rotate(1)
        self.crashed = False

    def rotate(self):
        self.rotation.rotate(-1)
        return self.rotation[0]

def tic(lines, cm):
    for cartCoords in currentCartCoords(cm):
        cy,cx = cartCoords
        c = cm[cy][cx]
        
        cr = list(filter(lambda c: c.x == cx and c.y == cy and c.crashed==False, cartRotations))
        if len(cr) == 0:
            continue
        else:
            cr = cr[0]

        if c == '>': #right
            ccx = cx+1
            ccy = cy
        elif c == '<': #left
            ccx = cx-1
            ccy = cy
        elif c == 'v': #down
            ccx = cx
            ccy = cy+1
        elif c == '^': #up
            ccx = cx
            ccy = cy-1
        else:
            print("error")

        nxt = lines[ccy][ccx]
        nxtCart = cm[ccy][ccx]

        if nxtCart in cart:
            print("COLLISION")
            print("X:", ccx, "Y:", ccy)

            #remove carts
            cm[ccy][ccx] = ' '
            cm[cy][cx] = ' '
            
            crashed = list(filter(lambda c: c.x == ccx and c.y == ccy, cartRotations))
            for crash in crashed:
                crash.crashed = True
                
            cr.crashed = True
            continue

        # easy moves:
        # >- -< |^v
        # optimized, shape stays the same
            
        #turns:
        # >\v >/^ v/< ^\< v\> </v  ^/> <\^
        if nxt in turns:
            c = turnDict[c+nxt]
            
        #intersections:
        # >+ v+ ^+ +<
        if nxt == '+':
            rot = cr.rotate()
            if rot == 'l':
                if cart.index(c)+1 >= len(cart):
                    c = cart[0]
                else:
                    c = cart[cart.index(c)+1]
            elif rot == 'r':
                c = cart[cart.index(c)-1]

        cm[cy][cx] = ' '
        cm[ccy][ccx] = c
        
        cr.x = ccx
        cr.y = ccy
        
    aliveCarts = list(filter(lambda c: c.crashed ==False, cartRotations))
    if len(aliveCarts) == 1:
        print("X:", aliveCarts[0].x, "Y:", aliveCarts[0].y)
        return False        
    return True
    
def currentCartCoords(cartMap):
    return [(y,x) for x in range(len(cartMap[y])) for y in range(len(cartMap)) if cartMap[y][x] in cart]

for y in range(len(lines)):
    lines[y] = list(lines[y])
    for x in range(len(lines[y])):
        if lines[y][x] in cart:
            mark = lines[y][x]
            cartMap[y][x] = mark
            lines[y][x] = cartDict[mark]

def printCartMap(cm):	
    for i in cm:
        print(''.join(i))

#create carts 
for each in currentCartCoords(cartMap):
    cartRotations.append(Cart(each[1],each[0],rotation))

noCollision = True
while(noCollision):
    noCollision = tic(lines,cartMap)


