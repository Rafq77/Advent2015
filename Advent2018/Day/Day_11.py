#NOTE, RUN IT IN COMMAND LINE, IDLE DOESN'T LIKE MULTIPROCESS LIB
# the key was, partial sums.
# @x,y= val + x-1,y + x,y-1 - x-1,y-1

import math
import itertools

inp = 8199
#inp 18 - 3d maxVal=113, coords= 90,269,16
#inp 42 - 3d maxVal=119, coords= 232,251,12
size = 303

def prod(x,y,ser):
    rack =x + 10
    pl = (rack)*y
    plS = pl + ser
    tmp = plS*rack
    tmp/=100
    t = math.trunc(tmp)# %10
    hun = int(str(t)[-1])
    prod = hun-5
    
    return prod

holo = [[prod(x,y,inp) for x in range(size)] for y in range(size)]
powers = [[0 for x in range(size)] for y in range(size)]
p3d = [[[0 for p in range(size-max(x,y))] for x in range(size)] for y in range(size)]

def square(x,y):
    #x and y are swapped
    return sum([sum(holo[y][x:x+3]) for y in range(y,y+3)])

def square3d(x,y,size):
    #x and y are swapped
    return sum([sum(holo[y][x:x+size]) for y in range(y,y+size)])

def square3d_wrapper(args):
	return square3d(*args)

#print(prod(3,5,8))
#print(prod(122,79,57))
#print(prod(217,196,39))
#print(prod(101,153,71))

if __name__ == "__main__":
    import multiprocessing as mp
    import functools
    import operator

    for i in range(size-3):
        for j in range(size-3):
            powers[i][j] = square(i,j)

    #p3d = [[[0 for p in range(size)] for x in range(size)] for y in range(size)]

    #for i in range(1, size-3):
    #    print(i)
    #    for j in range(1, size-3):
    #        for s in range(1, size-3-max(i,j)):
    #            p3d[i][j][s] = powers[i][j] - powers[i-s][j] - powers[i][j-s] + powers[i-s][j-s]

    #part 1 - 235,87
    maxVal = max(itertools.chain.from_iterable(powers))
    #todo cleanup finding max val in 2d list
    result = [(y, x.index(maxVal)) for y, x in enumerate(powers) if maxVal in x]
    print(result)

    pool = mp.Pool()

    for i in range(size-3):
        print(i)
        for j in range(size-3):
            #p3d[i][j] = list(pool.map(square3d_wrapper, [(i,j,s)for s in range(size-3 - max(i,j))]))
            p3d[i][j] = list(pool.map(square3d_wrapper, [(i,j,s) for s in range( min(size-3 - max(i,j),21) )]))

    maxVal = max(itertools.chain.from_iterable(functools.reduce(operator.concat, p3d)))
    coords = max([[(p3d.index(x), x.index(y), (y.index(maxVal))) for y in x if maxVal in y] for x in p3d])[0]

    #part2  - 234,272,18 max Val = 119
    print("maxVal is: " + str(maxVal) + " "  + str(coords))







