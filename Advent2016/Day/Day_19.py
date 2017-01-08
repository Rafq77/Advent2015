elvesTotal = 3001330
#elvesTotal = 5
table = []

class Elf:
    idx = 0
    prCount = 1
    removed = False
    

for i in range(elvesTotal):
    elf = Elf()
    elf.idx = i+1 #from one
    elf.prCount = 1
    table.append(elf)
    
while len(table) > 1:
    for i in range(len(table)):
        elfNext = (i+1)%len(table)
        if table[i].prCount != 0:
            table[i].prCount = table[i].prCount + table[elfNext].prCount
            table[elfNext].prCount = 0
    print(len(table))
    table = list(filter(lambda elf: elf.prCount != 0, table))

print(table[0].idx)
print(table[0].prCount)
'''
#reinitialize for task 2

table = []
for i in range(elvesTotal):
    elf = Elf()
    elf.idx = i+1 #from one
    elf.prCount = 1
    elf.removed = False
    elf.movedThisRound = False
    table.append(elf)


print("start")
i = 0
removedElves = 0
lenTable = len(table)
while lenTable != removedElves + 1:
    
    oppositeIdx = int(len(table)/2) # conversion to int, floors it anyway
    #removedElves = 0

    for i in range(lenTable):
        
        if table[i].removed == True:
            continue

        elementsBehind = len(filter(lambda x: x.removed==True, table[:i]))
        elementsFor = removedElves - elementsBehind
        
        #elfNext = (i+oppositeIdx)%len(table)
        oppositeIdx = int((lenTable-removedElves)/2) # conversion to int, floors it anyway

        j = i
        validSkips = 0
        while validSkips != oppositeIdx:
            j = (j+1)%lenTable
            if table[j].removed == False:
                validSkips+=1

        #elfNext = (i+oppositeIdx+(removedElves-elementsBehind))%lenTable


        elfNext = j    
        print(str(table[i].idx) + " stealing from " + str(table[elfNext].idx))

        table[i].prCount = table[i].prCount + table[elfNext].prCount
        table[elfNext].removed = True
        removedElves +=1
        #table.remove(table[elfNext])
        #oppositeIdx = int((len(table))/2)
        

    #table = list(filter(lambda elf: elf.removed == False, table))

    print(removedElves)
    #print(len(table))
    
'''
