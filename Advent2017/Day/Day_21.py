fd = open("""../Resources/Day_21.txt""", 'r')
lines = fd.read().split('\n')

from collections import deque
import numpy as np


def strToArray(s):
    return np.array([[int(c) for c in i] for i in s.replace('.','0').replace('#','1').split('/')])

class Rule():
    def __repr__(self):
        return str(self.r)+'\n'
    def __init__(self, rulStr):

        #expects tuple
        output = rulStr[1]
        rulStr = rulStr[0]
        self.stringRep = rulStr

        self.r = strToArray(rulStr)
        self.rl = np.flip(self.r,0)
        self.rr = np.flip(self.r,1)

        self.r90 = np.rot90(self.r)
        self.r90l = np.flip(self.r90,0)
        self.r90r = np.flip(self.r90,1)

        self.r180 = np.rot90(self.r90)
        self.r180l = np.flip(self.r180,0)
        self.r180r = np.flip(self.r180,1)

        self.r270 = np.rot90(self.r180)
        self.r270l = np.flip(self.r270,0)
        self.r270r = np.flip(self.r270,1)

        self.patterns = [self.r, self.r90, self.r90l, self.r90r, self.r180, self.r180l, self.r180r, self.r270, self.r270l, self.r270r, self.rl, self.rr]
        self.out = strToArray(output)
        
sep = ' => '

rules = [Rule(tuple(i.split(sep))) for i in lines]
#part1
#it = 5
#part2 
it = 18
start = ".#./..#/###"
painting = strToArray(start)

#UNIT TESTS
ut = [("../.#" , "##./#../..."), (".#./..#/###", "#..#/..../..../#..#")]

#TODO DISABLE UT
#rules = [Rule(s) for s in ut]
#it = 2

tst= """##.##./#..#../....../##.##./#..#../......"""
outUt = strToArray(tst)

for I in range(it):
    print(I)
    size = len(painting[0])
    if size%2 == 0:
        aStp = 2
    elif size%3 ==0:
        aStp = 3
    else:
        print("unexpected size of array")

    nBlocks = int(size/aStp)
    newSize = int(nBlocks*(aStp+1))
    newPainting = np.zeros((newSize,newSize),dtype=int)

    newPainting -= 1 

    for i in range(int(size/aStp)):
        xl = i*aStp
        xr = (i+1)*aStp
        for j in range(int(size/aStp)):
            yl = j*aStp
            yr = (j+1)*aStp
            
            subA = painting[xl:xr,yl:yr]
            for r in rules:
              if any([np.array_equal(subA, p) for p in r.patterns]):
                  nxl = i*(aStp+1)
                  nxr = (i+1)*(aStp+1)
                  nyl = j*(aStp+1)
                  nyr = (j+1)*(aStp+1)
                  newPainting[nxl:nxr,nyl:nyr] = r.out
                  break
    painting = newPainting
print(np.count_nonzero(painting))
