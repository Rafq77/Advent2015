import itertools
from collections import deque
coords = open("Resources/Day_25.txt").read().split('\n')

tst = """0,0,0,0
3,0,0,0
0,3,0,0
0,0,3,0
0,0,0,3
0,0,0,6
9,0,0,0
12,0,0,0""".split('\n') # 2

tst="""-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0""".split('\n') # 4

tst="""1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2""".split('\n') # 3

tst="""1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2""".split('\n') #  8

tst = coords # 386

class pt:
    def __init__(self, _1,_2,_3,_4):
        self.x = _1
        self.y = _2
        self.z = _3
        self.q = _4

    def __init__(self, ar):
        self.x = ar[0]
        self.y = ar[1]
        self.z = ar[2]
        self.q = ar[3]

    def isNear(self, other):
    	# TODO manhattan distance here?
        if (abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z) + abs(self.q - other.q)) <= 3:
            return True
        return False

    def __repr__(self):
        return "%s %s %s %s" % (self.x, self.y,self.z, self.q)
    
pts = deque()
groups = []
for each in tst:
    pts.append(pt(list(map(int, each.split(',')))))

#create first group
groups.append(set())
p = pts.popleft()
groups[0].add(p)

# for each pt in set (init set)


while (len(pts) > 0):
	added = False
	mergeGroups = []

	point = pts.popleft()

	for group in groups:
		toAdd = False
		for groupPt in group:
			# compare if point is within range to group
			# if yes, add to group, continue checking 
			if point.isNear(groupPt):
				# print(point, "is Near", groupPt) # DBG
				toAdd = True
				break
				# ok, break out from loop and set flag to add

		if toAdd:
			group.add(point)
			added = True
			mergeGroups.append(group)

	# additionally, if added already once, then merge with current group
	if len(mergeGroups) > 1:
		# cleanup in groups
		for group in mergeGroups:
			groups.remove(group)
		groups.append(set.union(*mergeGroups))

	# if no, create new group
	if added == False:
		s = set()
		s.add(point)
		groups.append(s)

print(len(groups))
