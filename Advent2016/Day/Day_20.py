Ips = 4294967295

fd = open("""Resources/Day_20.txt""", 'r')
s = fd.read()
fd.close()
s = s.split('\n')
S = s

blist = []
for i in s:
        t = i.split('-')
        blist.append((int(t[0]), int(t[1]))) #beg, end

blist = sorted(blist, key=lambda it: it[0])

#tst
#blist = [ (0,2), (4,7), (5,8) ]

done=True
act = blist[0]
ae = act[1] + 1
total = 0
while done:
        
        el = filter(lambda x: x[0]<=ae and ae <= x[1], blist)
        

        if len(el) == 1:
                act = filter(lambda x: x[0]<=ae and ae <= x[1], blist)[0]
                ae = act[1]+1
        elif len(el) > 1:
                act = filter(lambda x: x[0]<=ae and ae <= x[1], blist)[1]
                ae = act[1]+1
                print(len(el))
        else:
                # 0
                # task one, break on first encounter here
                print(ae)
                total+=1
                ae+=1
                if (ae >= 4294967295):
                        done = False
print(total)
