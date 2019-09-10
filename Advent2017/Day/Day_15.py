a = """Generator A starts with 679"""
b = """Generator B starts with 771"""

ta = 679
tb = 771

tst1a = 16807
tst1b = 48271

tst2a = 65
tst2b = 8921

fa = 16807
fb = 48271
mod = 2147483647

mask = 0xFFFF
match = int("1110001101001010", 2)

#unit test
#ta = tst2a
#tb = tst2b

la = list()
lb = list()
cnt = 0

itLimit = 5000000 # 5 mio

#part1
for i in range(40000000):
    ta = (ta * fa)%mod
    tb = (tb * fb)%mod

    if (ta & mask) == (tb & mask):
        cnt += 1

    if (ta%4 ==0) and len(la) < itLimit :
        la.append(ta)

    if (tb%8 ==0) and len(lb) < itLimit:
        lb.append(tb)

    #progress feedback
    #if len(la) % 500000 == 0 and len(la) < itLimit:
    #    print('ta ' + str(len(la)))

    #if len(lb) % 500000 == 0 and len(lb) < itLimit:
    #    print('tb ' + str(len(lb)))

    #if i%1000000==0:
    #    print(i)
    
print('p1')
print(cnt)

missing = itLimit-len(lb)
lb = lb + [0 for i in range(missing)]

cnt = 0
for x in zip(la,lb):
    if (x[0] & mask) == (x[1] & mask):
        cnt += 1
print('p2')
print(cnt)
    
