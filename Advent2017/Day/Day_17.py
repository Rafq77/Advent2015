src = 366
ut = 3

#unit test
#src = ut

spinlock = list()
it = 0
spinlock.append(it)

while(it != 2017):

    idx = spinlock.index(it) # position of last number
    it+=1 
    ix = (idx+src)%len(spinlock)+1 # this line is the essence for part2.
    spinlock.insert(ix,it) 

    if it%100000 == 0:
        print(it)

idx = spinlock.index(2017)
print(spinlock[idx-5:idx+5])

# part 2
idx = 0
for i in range(1,50000001): 
    idx = (idx+src)%i + 1  #remember last added on pos 1.
    if idx==1:
        koth = i
print(koth)
