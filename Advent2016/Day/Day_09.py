def unwind(s):
    tot = 0
    if s.count('(') == 0:
        return len(s)
    while (s.count('(') > 0):
        if (len(s) == 0):
            todo=False
            #print(tot)
            return 0
        b = s.index('(')  
        if (b != 0):
            tot += b
            s = s[b:]
        e = s.index(')')
        
        sub = s[:e+1]
        
        parts = sub[1:-1] #skip brackets
        parts = parts.split('x') #split in two
        
        elem = int(parts[0])
        cnt = int(parts[1])

        tot += unwind(s[len(sub):elem+len(sub)])*cnt
        s = s[ elem+ len(sub):]

    return tot;
#############


fd = open("""../Resources/Day_09.txt""", 'r')
s = fd.read()
fd.close()
S = s

todo = True
e = 0
tot = 0
tot2 = 0

while(todo):
    if (len(s) == 0):
        todo=False
        print(tot)
        break
    b = s.index('(')
    e = s.index(')')

    if (b != 0):
        tot += b
        tot2 += b
        s = s[b:]
        continue
 
    sub = s[:e+1]
    
    parts = sub[1:-1] #skip brackets
    parts = parts.split('x') #split in two
    
    elem = int(parts[0])
    cnt = int(parts[1])

    tot += elem*cnt
    tot2 += unwind(s[len(sub):elem+len(sub)])*cnt
    s = s[ elem+ len(sub):]

print(tot2)
