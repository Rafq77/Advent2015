fd = open("""../Resources/Day_23.txt""", 'r')
src = fd.read()
fd.close()

lines = src.split('\n')
print("Length: " + str(len(lines)))

pc = 0
cnt = 0 
reg = dict()
a = 'a'
for i in range(8):
    reg[a] = 0
    a  = chr(ord(a)+1)

#reg['a'] = 1
while pc < len(lines):
        
    ins = lines[pc].split()
    op = ins[0]
    pA = ins[1]
    pB = ins[2]

    #is second param a letter?
    secondIsReg = False
    if  pB in reg:
        secondIsReg = True
        
    if op == 'set':
        if secondIsReg:
            reg[pA] = reg[pB]
        else:
            reg[pA] = int(pB)
        
    elif op == 'sub':
        if secondIsReg:
            reg[pA] -= reg[pB]
        else:
            reg[pA] -= int(pB)
        
    elif op == 'mul':
        cnt += 1 
        if secondIsReg:
            reg[pA] *= reg[pB]
        else:
            reg[pA] *= int(pB)
        
    elif op == 'jnz':
        if pA not in reg and pA != '0':
            #constexpr
            pc += int(pB)
        elif reg[pA] != 0:
            if secondIsReg:
                pc += reg[pB]
            else:
                pc += int(pB)
            pc -=1 # because aftermath increment will move off instruction

    pc += 1

print(cnt)

#part 2 prime cheat search
def isprime2(n):
    '''
    check if integer n is a prime, return True or False
    '''
    # 2 is the only even prime
    if n == 2:
        return True
    # integers less than 2 and even numbers other than 2 are not prime
    elif n < 2 or not n & 1:
        return False
    # loop looks at odd numbers 3, 5, 7, ... to sqrt(n)
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


h = 0
b = 108100
c = 125100

for b in range(108100, c + 1, 17):
    #if not prime(b):
    if not isprime2(b):
        h += 1
        
print(h)
    
