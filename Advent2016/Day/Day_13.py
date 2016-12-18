f = lambda x,y: x*x+3*x+2*x*y+y+y*y
key = 1352
pos = (1,1)
maxX = 50
maxY = 50
#out = (31,39)
out = (31,39) #y/x notation
path = [] # array of tuples (coords)
maxLen = 500
foundExit = False
results = []

empty = '.'
wall = '#'
#zero is empty
#one is wall

#def checkPath(lPos, path):
def checkPath(lPos, lPath):
    global foundExit, results, a, S, empty, out
    #print(len(lPath))
    #print(lPos)
    if lPos[0] < 0 or lPos[0] >= maxX-1 or\
       lPos[1] < 0 or lPos[1] >= maxY-1 or\
       S[lPos[0]][lPos[1]] == wall or\
       len(lPath) > maxLen:
        return False #invalidPos == outsideField.
    
    if lPos == out:
        foundExit = True
        print("foundSmth")
        print(lPath)
        results.append(lPath)
        return #True

    # y/x notation!!
    l = S[lPos[0]][lPos[1]-1] 
    r = S[lPos[0]][lPos[1]+1] 
    u = S[lPos[0]-1][lPos[1]] 
    d = S[lPos[0]+1][lPos[1]] 

    newPath = lPath
    newPath.append(lPos)
    
    if u == empty:
        futurePos = (lPos[0]-1, lPos[1])
        if futurePos != lPath[-1]: #don't go back
                if lPath.count(futurePos) == 0:
                        done = checkPath(futurePos, newPath)

    if d == empty:
        futurePos = (lPos[0]+1, lPos[1])
        if futurePos != lPath[-1]: #don't go back
                if lPath.count(futurePos) == 0:
                        done = checkPath(futurePos, newPath)
                        
    if l == empty:
        futurePos = (lPos[0], lPos[1]-1)
        if futurePos != lPath[-1]: #don't go back
                if lPath.count(futurePos) == 0:
                        done = checkPath(futurePos, newPath)
                        
    if r == empty:
        futurePos = (lPos[0], lPos[1]+1)
        if futurePos != lPath[-1]: #don't go back
                if lPath.count(futurePos) == 0:
                        done = checkPath(futurePos, newPath)
    return
        
size = 50
#creates 2d array [x][y]
a = [[(bin(f(x,y) + key)[2:]).count('1')%2 for y in range(size)]for x in range(size)]
yC = 0

S = []
for y in a:
	s = ''
	xC = 0
	for x in y:
		#if (xC == 39 and yC == 31):
			#s+= 'X'
			#yC +=1
			#xC +=1
			#continue
		if (x == 1):
			s+='#'
		else:
			s+='.'
		xC+=1
	yC +=1
	S.append(s)

#path.append(pos)
checkPath(pos, path)
