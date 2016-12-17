s = "01000100010010111"
#part 1
length = 272

#part 2
length = 35651584

def xor(inp):
    return "".join(list(map(lambda x: x[0] != '1' and '1' or '0', inp)))

b = s
while len(b) < length:
    a = b
    b = b[::-1]

    b = a + '0' + xor(b)
    print(len(b))

print("done")
s = b[:length]

while (len(s)%2 == 0):
    newS = ''
    for pair in [s[i:i+2] for i in range(0, len(s), 2)]:
        newS += (pair[0] == pair[1] and '1' or '0')

    s = newS
    print(len(s))
            
        
    
