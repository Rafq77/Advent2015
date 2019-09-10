import itertools
from collections import Counter
lines = open('Resources/Day_17.txt').read().split('\n')

maxX= 600
maxY= 1650
quelle = (500,0)
karte = [['.' for x in range(maxX)] for y in range(maxY)]

def save(karte):
    out = open("D:\\work\\tmp\\advent2018\\day17.txt",mode='w')
    for line in karte:
        out.write(''.join(line))
        out.write('\n')


def fillLvl(x,y):
    global karte
    X = x
    Y = y
    newQuelle = []
    # check if my lvl is within container (i.e. exit on any sides?)

    lSideOpen = True
    rSideOpen = True
    
    #go left
    while karte[y][x] != '#' and karte[y+1][x] !='.':
        x-=1

    if karte[y][x] == '#':
        lSideOpen = False

    if karte[y][x] == '.':
        lSideOpen = True
    #new quelle @ [y][x]
        newQuelle.append([x,y])

    #go right
    y = Y
    xL = x
    x = X
    while karte[y][x] != '#' and karte[y+1][x] !='.':
        x+=1
    xR = x

    if karte[y][x] == '#':
        rSideOpen = False

    if karte[y][x] == '.':
        rSideOpen = True
        newQuelle.append([x,y])

    mark = '|' if lSideOpen or rSideOpen else '~'

    for x in range(xL+1, xR):
        karte[y][x] = mark

    return newQuelle


    #should return coords of sides where you can flow further, 

for each in lines:
    p = each.split(', ')
    if p[0][0] == 'x': #vertical wall
        x = int(p[0][2:])
        y = p[1][2:] # range!!!!

        yRange = list(map(int, y.split('..')))

        for y in range(yRange[0],yRange[1]):
            karte[y][x] = '#'
        
    else:               #horizontal wall
        x = p[1][2:]
        y = int(p[0][2:]) # range!!!!

        xRange = list(map(int, x.split('..')))

        for x in range(xRange[0],xRange[1]+1):
            karte[y][x] = '#'

#flowHead
fH = list(quelle) 
todo = []
#flow down

try:
    while(y<maxY):
        x = fH[0]
        y = fH[1]
        sq = karte[y][x]

        if karte[fH[1]+1][fH[0]] == '|' or karte[fH[1]-1][fH[0]] == '|':
            karte[y][x] = '|'
                        
        if karte[fH[1]+1][fH[0]-1] == '|' or karte[fH[1]+1][fH[0]+1] == '|':
            fH = todo.pop()
            continue
        
        if y+2 >= maxY:
            fH = todo.pop()
            continue
        sqDown = karte[y+1][x]
        

        #flow down
        if sqDown == '.':
            karte[y][x] = '|'
            fH[1]+=1
        elif sqDown == '#' or sqDown == '~': #reached some bottom
            newQuelle = fillLvl(x,y)
            if newQuelle == []: #empty
                fH[1]-=1 #fillUp
            else:
                todo.extend(newQuelle)
                fH = todo.pop()
                
        elif sqDown == '|': #joined some other
            fH = todo.pop()
            
            
except IndexError as IE:
    a=3

minY = min([y for y in range(maxY) if '#' in karte[y]])
maxY = max([y for y in range(maxY) if '#' in karte[y]])
a = sum([row.count('~') for row in karte[:maxY+1]])
b = sum([row.count('|') for row in karte[:maxY+1]])
print( a + b - minY)
#part 2 is water with '~'
print(a)

save(karte)
