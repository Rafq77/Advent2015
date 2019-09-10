#jump instructions
    
fd = open("""Resources/Day_06.txt""", 'r')
registers = list(map(lambda x: int(x), fd.read().split()))

history = list()
checksum = sum(registers) # needs always to be equal
regLen = len(registers)

def redistribute(tab, ix):
    tmp = tab[ix]
    tab[ix] = 0

    while (tmp > 0):
        ix += 1
        if ix == regLen:
            ix = 0

        tmp -= 1
        tab[ix] += 1

    return tab

model = [1, 1, 0, 15, 14, 13, 12, 10, 10, 9, 8, 7, 6, 4, 3, 5]

cnt = 0
while (registers not in history):
    mx = max(registers)
    idx = registers.index(mx)
    history.append(registers.copy())
    registers = redistribute(registers, idx)
    #print(registers)
    cnt +=1 
    if sum(registers) != checksum:
        print ("Error checksum")
        break

print("P1 cnt=" + str(cnt))

cnt = 0
go = True
while (go):
    mx = max(registers)
    idx = registers.index(mx)
    registers = redistribute(registers, idx)
    cnt +=1 
    if sum(registers) != checksum:
        print ("Error checksum")
        break
    if (registers == model):
        print ("Found 2nd! " + str(cnt))
        break
    
    


