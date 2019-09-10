lines = open("Day_10.txt").read().split('\n')

lines = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=< -1,  0>
position=< 3, -2> velocity=< -1,  1>
position=< 6, 10> velocity=< -2, -1>
position=< 2, -4> velocity=< 2,  2>
position=< -6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=< -3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=< -1, -1>
position=< -2,  3> velocity=< 1,  0>
position=< -4,  3> velocity=< 2,  0>
position=< 10, -3> velocity=< -1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=< 15,  0> velocity=< -2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=< -1,  1>
position=< 0,  5> velocity=< 0, -1>
position=< -2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=< -2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=< -1, -1>
position=< 5,  0> velocity=< 1,  0>
position=< -6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=< 14,  7> velocity=< -2,  0>
position=< -3,  6> velocity=< 2, -1>""".split('\n')

class Elf:
    def __init__(self, pos,vel):
        self.pos = pos
        self.vel = vel

    def print(self):
        print(str(self.pos) + " - " + str(self.vel))

def move(pts):
    for point in pts:
        p = point.pos
        v = point.vel
        point.pos = (p[0] + v[0], p[1] + v[1])

def show(pts):
    
    minX = min(pts, key=lambda x: x.pos[0]).pos[0]
    maxX = max(pts, key=lambda x: x.pos[0]).pos[0] +1 
    minY = min(pts, key=lambda x: x.pos[1]).pos[1]
    maxY = max(pts, key=lambda x: x.pos[1]).pos[1] +1

    canvas = [['.' for i in range(minX, maxX) ] for j in range(minY, maxY)]

    offX = abs(minX)
    offY = abs(minY)

    #print(minX,maxX,minY,maxY,offX,offY, len(canvas), len(canvas[0]))
    
    for p in pts:
        pos = p.pos
        oy = pos[0]+offX
        ox = pos[1]+offY
        #print(ox,oy)
        canvas[ox][oy] = '#'

    for line in canvas:
        print(''.join(line))
              

    #for p in pts:
        #p = map(lambda x: x.pos = (x.pos[0] + 
    
    #[['.' for i in range(5)] for j in range(5)]

    

elves = []
for each in lines:
    parts = each.split()
    x = int(parts[1].strip(','))
    y = int(parts[2][:-1])
    vx = int(parts[4].strip(','))
    vy = int(parts[5][:-1])

    elves.append(Elf((x,y),(vx,vy)))


for i in range(5):
    move(elves)
    show(elves)
    input()
    
    
