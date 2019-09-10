Ips = 4294967295

fd = open("""Resources/Day_22.txt""", 'r')
s = fd.read()
fd.close()
s = s.split('\n')[2:]
S = s


class Node:
    Size = 0 #TB
    Used = 0 #TB
    Avail = 0 #TB
    Use = 0 #percent

lenX = 30
lenY = 35
x = lenX
y = lenY
#[x][y]
grid =[[Node() for i in range(y)] for j in range(x)]

for i in s:
    parts = i.split()
    coords = parts[0].split('-')

    x = int(coords[1][1:])
    y = int(coords[2][1:])

    grid[x][y].Size = int(parts[1][:-1])
    grid[x][y].Used = int(parts[2][:-1])
    grid[x][y].Avail = int(parts[3][:-1])
    grid[x][y].Use = int(parts[4][:-1])

#manual
legitPairs = []
for x in range(lenX):
    for y in range(lenY):
        n1 = grid[x][y]
        # - Node A is not empty (its Used is not zero).
        if n1.Used == 0:
            continue
        for iX in range(lenX):
            for iY in range(lenY):
                # - Nodes A and B are not the same node.
                if x == iX and y == iY:
                    continue

                # - The data on node A (its Used) would fit on node B (its Avail).
                n2 = grid[iX][iY]

                #check pairs
                if n1.Used <= n2.Avail:
                    #tuple of 2 tuples
                    pair = ( (x, y), (iX, iY) )

                    legitPairs.append(pair)
    

print(len(legitPairs))

for row in grid:
    string = ''
    for node in row:
        string += str(node.Used) +'/' + str(node.Size) +  ' '
    print(string)

#visualized the data and did manual calculations from x = 28; y = 34 (only empty disk)
#and moved it around like an empty tile. The goal data was located at x = 29; y= 0.
# The read acces point is at x = 0; y = 0;
# i neede to move the empty tile (with skipping the wall of big data disks) to the goal data.
# this costs 45 moves
# and then "looping" the move of my goal data to access point by making 5 step iterations, in total 28
# 45 + 28*5 gives 185 which was the goal
