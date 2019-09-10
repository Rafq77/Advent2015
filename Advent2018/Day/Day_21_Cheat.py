a = 0
s = set()
part1 = False
while True:
    c = a | 0x10000
    a = 6780005
    while True:
        b = c & 0xFF
        a += b
        a &= 0xFFFFFF
        a *= 65899
        a &= 0xFFFFFF
        if (256 > c):
            if part1:
                print(a)
                exit(0)
            else:
                if a not in s:
                    print(a)
                s.add(a)
                break
        # the following code was the optimised part
        c = c // 256
