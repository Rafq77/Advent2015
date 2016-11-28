raw = [ 11
,30
,47
,31
,32
,36
,3
,1
,5
,3
,32
,36
,15
,11
,46
,26
,28
,1
,19
,3 ]
raw.sort()
#raw.reverse()

goal = 150
cnt = 0
solutions = []
minimum = False
import itertools

#13 because maximum length from smallest portions
for i in range(14):
    for t in itertools.combinations(raw,i):
        if sum(t) == 150:
            cnt += 1
            solutions.append(t)
    #        minimum = True
    #if minimum == True:
    #    break

print("done")

    
    

