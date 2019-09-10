import itertools
fd = open("""Resources/Day_20.txt""", 'r')
src = fd.read()
lines = src.split('\n')

ID = 0
class Particle:
    class Pos:
        def __init__(self,x,y,z):
            self.x = x
            self.y = y
            self.z = z

        def __repr__(self):
            return "Pos(%s, %s, %s)" % (self.x, self.y, self.z)
            
        def __eq__(self, other):
            if isinstance(other, Particle.Pos):
                return ((self.x == other.x) and (self.y == other.y) and (self.z == other.z))
            else:
                return False
            
        def __ne__(self, other):
            return (not self.__eq__(other))

        def __hash__(self):
            return hash(self.__repr__())

    class Velocity:
        def __init__(self,x,y,z):
            self.x = x
            self.y = y
            self.z = z

    class Acc:
        def __init__(self,x,y,z):
            self.x = x
            self.y = y
            self.z = z

    def __init__(self, pos, vel, acc):
        global ID
        self.ID = ID
        self.destroyed = False
        ID += 1
        self.pos = pos
        self.vel = vel #velocity
        self.acc = acc

    def updateVelocity(self):
        self.vel.x += self.acc.x
        self.vel.y += self.acc.y
        self.vel.z += self.acc.z

    def updatePosition(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.pos.z += self.vel.z

    def move(self):
        self.updateVelocity()
        self.updatePosition()

    def dist(self):
        return self.pos.x**2 + self.pos.y**2 + self.pos.z**2
    
    def distM(self):
        return abs(self.pos.x) + abs(self.pos.y) + abs(self.pos.z)

    def print(self):
        print("position: %s %s %s" % (self.pos.x, self.pos.y, self.pos.z))
        print("velocity: %s %s %s" % (self.vel.x, self.vel.y, self.vel.z))
        print("acceleration: %s %s %s" % (self.acc.x, self.acc.y, self.acc.z))
    
particles = list()
for line in lines:
    pva = line.split(', ')
    p = pva[0][3:-1].split(',')
    v = pva[1][3:-1].split(',')
    a = pva[2][3:-1].split(',')

    x,y,z = [int(i) for i in p]
    pos = Particle.Pos(x,y,z)

    x,y,z = [int(i) for i in v]
    vel = Particle.Velocity(x,y,z)
    
    x,y,z = [int(i) for i in a]
    acc = Particle.Acc(x,y,z)

    particles.append(Particle(pos,vel,acc))

someTime = 500 #after 400 it is also ok
#run for some time
for i in range(someTime):

    #part2
    seen = set()
    for e in particles:
        if e.destroyed == True:
            continue
        elif e.pos not in seen:
            seen.add(e.pos)
        else:
            #print("collisions")
            e.destroyed = True
            
            #find remaining with same pos
            for each in [p for p in particles if p.pos == e.pos and p.destroyed == False]:
                each.destroyed = True
            
    for each in particles:
        #if each.destroyed == False:
        each.move()

#find minimum dist
#part1 answer
m = min(particles, key=lambda x: x.distM())
print(m.ID)

#part2 answer
print(len(list(filter(lambda x: x.destroyed==False, particles))))


