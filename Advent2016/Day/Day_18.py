fd = open("""../Resources/Day_18.txt""", 'r')
s = fd.read()
fd.close()
#s = s.split('\n')
S = s

#s = '.^^.^.^^^^'


totalRows = 40
totalRows = 400000


tab = []
tab.append(s)
rows = len(tab)
trap = '^'
safe = '.'
#sum([i=='.' for i in s])

while rows < totalRows:
    template = tab[-1]
    newRow = ''

    #outside borders is 'safe'
    template = '.' + template
    template += '.'

    for i in range(1, len(template)-1):
        l = template[i - 1]
        c = template[i]
        r = template[i + 1]
        if (l == c == trap and r == safe) or\
           (c == r == trap and l == safe) or\
           (l == trap and c == r == safe) or\
           (r == trap and l == c == safe):
            newRow += '^'
        else:
            newRow += '.'

    tab.append(newRow)
    rows += 1

print(sum([sum([ r=='.' for r in i ]) for i in tab]))
