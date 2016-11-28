raw = """Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.""".split('.\n')


"""
Seeing how reindeer move in bursts, Santa decides he's not pleased
with the old scoring system.

Instead, at the end of each second,
he awards one point to the reindeer currently in the lead.
(If there are multiple reindeer tied for the lead, they each get one point.)
He keeps the traditional 2503 second time limit,
of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above,
after the first second, Dancer is in the lead and gets one point.
He stays in the lead until several seconds into Comet's second burst:
after the 140th second,
Comet pulls into the lead and gets his first point.
Of course, since Dancer had been in the lead for the 139 seconds before that,
he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points,
while poor Comet, our old champion, only has 312.
So, with the new scoring system,
Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer
(in your puzzle input), after exactly 2503 seconds,
how many points does the winning reindeer have?
"""

#c = Ren("Comet", 14, 10, 127)
#d = Ren("Dancer", 16, 11, 162)

#In this example, after the 1000th second, both reindeer are resting,
#and Comet is in the lead at 1120 km (
#poor Dancer has only gotten 1056 km by that point).


class Ren:
    def __init__(self, name, spd, endurance, rest):
        self.n = name
        self.s = spd
        self.e = endurance # how long can he fly
        self.r = rest

        self.sec = 0

    def Run(self, seconds):
        period = self.e + self.r #seconds
        
        revolution = int(seconds/period) 
        remaining = seconds - (revolution * period)


        distanceTraveled = (self.e * self.s) * revolution

        if remaining > 0:
            if remaining < self.e:
                distanceTraveled += remaining * self.s
            else:
                distanceTraveled += self.e * self.s

        #print(self.n + " traveled " + str(distanceTraveled))
        return(distanceTraveled)

    def AddS(self):
        self.sec += 1
        return self.Run(self.sec)
        
    
tab = []
ren = []
for i in raw:
    p = i.split(' ')
    x = Ren(p[0], int(p[3]), int(p[6]), int(p[-2]))
    ren.append(x)
    tab.append(x.Run(2503))

max(tab)



results = tab
for i in range(len(results)):
    results[i] = 0

for i in range(2503):
    tab = []    
    for r in ren:
        tab.append(r.AddS())

    if tab.count(max(tab)) > 1:
        idx = [eq for eq, x in enumerate(tab) if x == max(tab)]
        for i in idx:
            results[i] += 1
    else:
        results[tab.index(max(tab))] += 1
    
        
