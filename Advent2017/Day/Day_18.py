import itertools
fd = open("""Resources/Day_18.txt""", 'r')
src = fd.read()
steps = src.split('\n')



def run(ID, rxQ, txQ):
    
    playSoundFreqConstCnt = 0
    _id = ID
    txCnt = 0
    regs = dict()
    regs['a'] = 0
    regs['i'] = 0
    regs['p'] = ID
    regs['b'] = 0
    regs['f'] = 0

    ip = 0
    pLen = len(steps)
    while 0 <= ip < pLen:

        parts = steps[ip].split(' ')
        instr = parts[0]

        if instr == 'snd':
            if txQ:
                txQ.put(regs[parts[1]])
                txCnt += 1
                print("id" + str(_id) + " snt: " + str(txCnt))
            else:
                playSoundFreq = regs[parts[1]]
            
        elif instr == 'set':
            if parts[2] > '9': #its a reg as 2nd param!
                regs[parts[1]] = regs[parts[2]]
            else:
                regs[parts[1]] = int(parts[2])
        elif instr == 'add':
            if parts[2] > '9': #its a reg as 2nd param!
                regs[parts[1]] += regs[parts[2]]
            else:
                regs[parts[1]] += int(parts[2])
        elif instr == 'mul':
            regs[parts[1]] *= int(parts[2])
        elif instr == 'mod':
            if parts[2] > '9': #its a reg as 2nd param!
                regs[parts[1]] = regs[parts[1]] %  regs[parts[2]]
            else:
                regs[parts[1]] = regs[parts[1]] %  int(parts[2])
        elif instr == 'rcv':
            if rxQ:
                regs[parts[1]] = rxQ.get()
                playSoundFreq = regs[parts[1]]
                
            elif regs[parts[1]] > 0:
                playSoundFreqConstCnt += 1
            #print(playSoundFreq)
        elif instr == 'jgz':
            # fuck this!
            if parts[2] > '9' and regs[parts[2]] > 0:
                ip += regs[parts[2]]
                ip -=1 #compensation of iterator
            elif parts[1] == '1' or regs[parts[1]] > 0: # "=='1'" because there is an instruction jgz 1 3, ie. always jump +3
                ip += int(parts[2])
                ip -=1 #compensation of iterator
        ip+=1
        if playSoundFreqConstCnt > 100:
            break
        #print(ip)
        
    return playSoundFreq


import collections
import multiprocessing.pool

print("part1: ", run(0, None,None))
pool = multiprocessing.pool.ThreadPool(processes=2)

q1 = multiprocessing.Queue()
q2 = multiprocessing.Queue()

res1 = pool.apply_async(run, (0, q1, q2))
res2 = pool.apply_async(run, (1, q2, q1))
