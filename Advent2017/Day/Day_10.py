src = "183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88"
org = src
src = list(map(lambda x: int(x), src.split(',')))
lst = list(range(0,256))


ut = [3, 4, 1, 5]
utLst = [0, 1, 2, 3, 4]

#unit test override
#src = ut
#lst = utLst

def knotHash(src, lst):
    p = 0
    s = 0

    for length in src:
        wrap = False
        
        sub = lst[p: p + length] # check overflow
        if len(sub) < length:
            
            # take from beginning
            wrapLeftLength = length - len(sub)
            sub = sub + lst[: wrapLeftLength]
            wrap = True
                    
        sub.reverse()
        if wrap == True:
            lst[p:] = sub[: len(sub) - wrapLeftLength]
            lst[:wrapLeftLength] = sub[-wrapLeftLength:]
        else:
            lst[p:p + length] = sub
        p = (p + length + s)%len(lst)
        s += 1

    print(lst[0]*lst[1])

#this is the copy of above but adjusted for hex and preserves internal pos and skip.
position = 0
skip = 0
def knotHash2(src, lst):
    
    global position
    global skip

    for length in src:
        wrap = False
        
        s = lst[position: position + length] # check overflow
        if len(s) < length:
            # take from beginning
            wrapLeftLength = length - len(s)
            s =  s + lst[: wrapLeftLength]
            
            wrap = True
            
        
        s.reverse()
        if wrap == True:
            lst[position:] = s[: len(s) - wrapLeftLength]
            lst[:wrapLeftLength] = s[-wrapLeftLength:]
        else:
            lst[position:position + length] = s
        position = (position + length + skip)%len(lst)
        skip += 1
    return lst

knotHash(ut, utLst)
knotHash(src, lst)

src = list(map(lambda x : ord(x), org))

#unit tests, work! :D
#src = [49,44,50,44,51] # --> 3efbe78a8d82f29979031a4aa0b16a9d
#src = [49,44,50,44,52] # --> 63960835bcdc130f0b66d7ff4f6a5a8
#src = [] # --> a2582a3a0e66e6e86e3812dcb672a272
#src = [65, 111, 67, 32, 50, 48, 49, 55] # 'AoC 2017' --> 33efeb34ea91902bb2f59c9920caa6cd

# add constant
const = [17, 31, 73, 47, 23]
src = src + const

#initialize length string
lst = list(range(0,256))

for i in range(64):
    lst = knotHash2(src , lst)

from functools import reduce
#tst = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
#reduce(lambda x, y: x^y, tst)

out = list()
for i in range(16):
    sub = lst[i*16:(i+1)*16]
    out.append(reduce(lambda x, y: x^y, sub))

print("".join([hex(x)[2:] for x in out])) #forgets 0
print("".join(["{:02x}".format(x) for x in out]))
