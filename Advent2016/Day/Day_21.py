Ips = 4294967295

fd = open('day21.txt','r')
s = fd.read()
fd.close()
s = s.split('\n')
S = s


pas = "abcdefgh"
pas = "fbgdceah"

ss = ["swap position 4 with position 0",
     "swap letter d with letter b",
     "reverse positions 0 through 4",
     "rotate left 1 step",
     "move position 1 to position 4",
     "move position 3 to position 0",
     "rotate based on position of letter b",
     "rotate based on position of letter d"]
s.reverse()

#pas = "abcde"
#pas = "decab"
lngth = len(pas)

#part1
'''
for instr in s:
        parts = instr.split()

        if parts[0] == 'move':
                x = int(parts[2])
                y = int(parts[5])
                l = pas[x] 
                t = pas[:x] + pas[x + 1:]
                pas = t[:y] + l + t[y:] 
                #2
                #to
                #5
        elif parts[0] == 'reverse':
                x = int(parts[2])
                y = int(parts[4]) +1 #inclusive
                t = pas[x:y]
                pas = pas[:x] + t[::-1] + pas[y:]

                
                #2
                #trough
                #4
        elif parts[0] == 'swap':
                if parts[1] == 'position':
                        x = int(parts[2])
                        y = int(parts[5])
                        l1 = pas[x]
                        l2 = pas[y]
                        pas = pas.replace(l1, '0')
                        pas = pas.replace(l2, l1)
                        pas = pas.replace('0', l2)
                else:
                        #letter
                        pas = pas.replace(parts[2], '0')
                        pas = pas.replace(parts[5], parts[2])
                        pas = pas.replace('0', parts[5])
        elif parts[0] == 'rotate':
                if parts[1] == 'left':
                        rot = int(parts[2])
                        pas = pas[rot:] + pas[:rot]
                elif parts[1] == 'right':
                        rot = int(parts[2])
                        pas = pas[-rot:] + pas[:-rot]
                else:
                        #magic rotate
                        idx = pas.index(parts[-1])
                        pas = pas[-1:] + pas[:-1]
                        extra = 0
                        if idx >= 4:
                                extra = 1
                        extra-=1

                        idx = pas.index(parts[-1])
                
                        pas = pas[-idx-extra:] + pas[:-idx-extra]
        else:
                print("unknown instruction found!" + instr)

        print(len(pas))
'''        
for instr in s:
        parts = instr.split()

        if parts[0] == 'move':
                y = int(parts[2])
                x = int(parts[5])
                l = pas[x] 
                t = pas[:x] + pas[x + 1:]
                pas = t[:y] + l + t[y:] 
                #2
                #to
                #5
        elif parts[0] == 'reverse':
                x = int(parts[2])
                y = int(parts[4]) +1 #inclusive
                t = pas[x:y]
                pas = pas[:x] + t[::-1] + pas[y:]

                
                #2
                #trough
                #4
        elif parts[0] == 'swap':
                if parts[1] == 'position':
                        x = int(parts[2])
                        y = int(parts[5])
                        l2 = pas[x]
                        l1 = pas[y]
                        pas = pas.replace(l1, '0')
                        pas = pas.replace(l2, l1)
                        pas = pas.replace('0', l2)
                else:
                        l2 = parts[2]
                        l1 = parts[5]
                        #letter
                        pas = pas.replace(l1, '0')
                        pas = pas.replace(l2, l1)
                        pas = pas.replace('0', l2)
        elif parts[0] == 'rotate':
                if parts[1] == 'left':
                        rot = int(parts[2])
                        pas = pas[-rot:] + pas[:-rot]
                elif parts[1] == 'right':
                        rot = int(parts[2])
                        pas = pas[rot:] + pas[:rot]
                else:
                        #magic rotate
                        idx = pas.index(parts[-1])
                        if idx == 0 or idx == 1:
                                pas = pas[1:] + pas[:1]
                        elif idx == 2:
                                pas = pas[-2:] + pas[:-2]
                        elif idx == 3:
                                pas = pas[2:] + pas[:2]
                        elif idx == 4:
                                pas = pas[-1:] + pas[:-1]
                        elif idx == 5:
                                pas = pas[3:] + pas[:3]
                        elif idx == 7:
                                pas = pas[-4:] + pas[:-4]

 #                       pas = pas[1:] + pas[:1]

#                        pas = pas[1:] + pas[:1]
                       # extra = 0
                       # if idx >= 4:
                       #         extra = -1
                       # extra+=1

                        #idx = pas.index(parts[-1])
                
                        #pas = pas[idx+extra:] + pas[:idx+extra]
        else:
                print("unknown instruction found!" + instr)

        print(len(pas))
