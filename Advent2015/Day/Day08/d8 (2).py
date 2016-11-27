raw = """Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46""".split('\n')

class System:
    name = ""

    def __init__(self, _name):
        self.name = _name


stations = list(map(lambda x: x.split(' ')[0],raw))
stations = list(set(stations + list(map(lambda x: x.split(' ')[2],raw))))

muster = {}
distances = []
table = {}

for station in stations:
    muster[station] = 0

for station in stations:
    table[station] = muster

for i in raw:
    dist = 0
    split = i.split(' = ')
    station0 = split[0].split(' to ')[0]
    station1 = split[0].split(' to ')[1]
    dist = split[1]

    table[station0][station1] = dist
    table[station1][station0] = dist
