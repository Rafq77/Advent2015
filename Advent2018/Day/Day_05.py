import itertools
#lines = open('Resources/Day_05.txt').read().split('\n')
lines = open('Resources/Day_05.txt').read()


txt = lines
it = 0

#brute force
a = ord('a')
A = ord('A')
z = ord('z') 
diff = a - A
size = z - a
global tab
tab = []
for c in range(a, z+1):
        tab.append(chr(c) + chr(c-diff))
        tab.append(chr(c-diff) + chr(c))

def compress(txt):
    emptyRun = False
    while(False == emptyRun):

        emptyRun = True
        lenOrig = len(txt)
        for each in tab:
            txt = txt.replace(each, '')

        if len(txt) < lenOrig:
            emptyRun = False
    return txt

output = compress(lines)
print("part 1: " + str(len(output)))

its = dict()
for c in range(a, z+1):
    txt = lines.replace(chr(c),'').replace(chr(c-diff), '')
    output = compress(txt)
    its[chr(c)] = len(output)
    print(chr(c) + ' ' + str(len(output)))
    
print("part 2: " + str(min(its.values())))
