fd = open("""../Resources/Day_02.txt""", 'r')
src = fd.read()
fd.close()

keys = src.split('\n')
print("Length: " + str(len(keys)))

# #1. conv. numbers
tab = list()

for row in keys:
    # add new row
    tab.append(list(map(lambda x: int(x), row.split())))

# task 1: sum of differences between max min in row
total = 0;
for row in tab:
    total += max(row) - min(row)

# task  2: sum of !!divisions!! between max min, but evenly divisible
total2 = 0;
for row in tab:
    s = sorted(row) # :)

    lop = [(p1, p2) for p1 in s for p2 in s if (p1 != p2 and p1 > p2 and p1%p2 == 0)][0]
    
    total2 += lop[0] / lop[1]



print(total)
print(total2)
