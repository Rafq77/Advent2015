#jump instructions
    
fd = open("""Resources/Day_05.txt""", 'r')
lines = list(map(lambda x: int(x), fd.read().split()))
bckp = lines.copy()
cnt = 0
ip = 0 #instruction pointer

progEnd = len(lines)

while ip < progEnd:
    offset = lines[ip]
    lines[ip] += 1
    ip += offset
    cnt +=1

print("Went out of the list in " + str(cnt) + " steps")

#reinitialize
cnt = 0
ip = 0
lines = bckp.copy()


while ip < progEnd:
    offset = lines[ip]
    if offset >= 3:
        lines[ip] -= 1
    else:
        lines[ip] += 1
    ip += offset
    cnt +=1

print("When decrementing after jumps higher than 3, then you are out of the list in " + str(cnt) + " steps")


#round 2
    

    
