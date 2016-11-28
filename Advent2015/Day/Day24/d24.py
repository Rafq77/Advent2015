import itertools

el = [
1
,3
,5
,11
,13
,17
,19
,23
,29
,31
,37
,41
,43
,47
,53
,59
,67
,71
,73
,79
,83
,89
,97
,101
,103
,107
,109
,113]

results = []
keyNum = int(sum(el)/3)
cnt = 0
print("Looking for " + str(keyNum))

m = 9999999999999999999999
for l in itertools.combinations(el,6):
    if sum(l) == keyNum:
        p = 1
        for i in l:
            p *= i
        m = min(m, p)
print(m)

m = 999999999999
keyNum = int(sum(el)/4)
for i in range(1,6):
    for l in itertools.combinations(el,i):
        if sum(l) == keyNum:
            p = 1
            for i in l:
                p *= i
    #        print(p)
            m = min(m, p)
    print(m)
    #print(p)



#for l in itertools.permutations(el):
#for l in itertools.combinations(el, len(el)):
    #cnt+= 1
    #if cnt%100000 == 0:
     #   print(cnt)

#    complete = False
#    missingCompletes = 2
#    subTotal = 0

 #   for i in l:
 #       subTotal += i
 #       if subTotal == keyNum:
#            subTotal = 0
#            missingCompletes -= 1

#        if missingCompletes <= 0:
#            results.append(l)
#            print(len(results))
#            break

print("done")
