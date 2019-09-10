fd = open("""Resources/Day_13.txt""", 'r')
lines = fd.read().split('\n')

ut = """0: 3
1: 2
4: 4
6: 4"""

#lines = ut.split('\n')

class Layer:
    def __init__(self, rnge, depth):
        self.range = [0 for z in range(rnge)]
        self.Sidx = 0
        self.goingDown = True
        self.depth = depth

    def move(self):
        if self.goingDown:
            self.Sidx += 1
            if (self.Sidx == len(self.range)-1):
                self.goingDown = False
        else:
            self.Sidx -= 1
            if (self.Sidx == 0):
                self.goingDown = True

    def print(self):
        tmp = self.range.copy()
        tmp[self.Sidx] = 'S'

        strOut = [ str(o) for o in tmp]
        print(strOut)

class Packet:
    def __init__(self, idx):
        self.offset = idx #name/id
        self.idx = 0
        self.isThrough = False
        self.isCaught = False
                
dpr = list(map(lambda x: (int(x.split(': ')[0]), int(x.split(': ')[1])), lines))

#depth:range
depth = None
maxDepth = max(dpr)[0]
rng = None
maxRange = max(dpr, key=lambda x:x[1])[1]

#prepare
firewall = list()
for i in range(maxDepth+1):
    cfg = [x for x in dpr if x[0] == i]
    if cfg:
        cfg = cfg[0]
        firewall.append(Layer(cfg[1], i))
        
    else:
        firewall.append(None)


delay = 1
idx = 0
caught = True
lenFirewall = len(firewall)
packets = list()

while (caught == True):

    if delay % 1000 == 0:
        print(delay)
        
    delay -=1
    idx = delay  

    # fire new packet on current delay.
    packets.append(Packet(idx))

    for packet in packets:
       
        if(packet.idx >= 0 and packet.idx < lenFirewall):
            #packet in transit
            if (firewall[packet.idx] and firewall[packet.idx].Sidx == 0):
                #packet busted
                packet.isCaught = True
                continue

        if packet.idx >= lenFirewall:
            #packet is Through!
            caught = False
            packet.isThrough = True

        packet.idx+=1 #move

    # remove busted packets
    packets = list(filter(lambda x: x.isCaught == False, packets))

    # move scanners
    [e.move() for e in firewall if e != None]

print( next(filter(lambda x:x.isThrough== True, packets)).offset)
 
# part 1 oneliner
s = list(filter(lambda x: ((x[0])%(x[1]*2-2))==0, dpr))
out = sum(map(lambda x: x[0]*x[1],s))


