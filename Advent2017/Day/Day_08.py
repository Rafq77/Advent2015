fd = open("""../Resources/Day_08.txt""", 'r')
src = fd.read()
fd.close()

lines = src.split('\n')
print("Length: " + str(len(lines)))

import operator
ops = {
    ">": operator.gt,
    "<": operator.lt,
    "<=": operator.le,
    ">=": operator.ge,
    "==": operator.eq,
    "!=": operator.ne,
    "inc" : operator.add,
    "dec" : operator.sub,
    }


regs = dict() #registers

ifSplit = ' if '

ip = 0
koth = 0
for line in lines:
    
    lr = line.split(ifSplit)
    l = lr[0]
    r = lr[1]

    #prepare first, 
    target = l.split()
    
    targetReg = target[0]
    targetOp  = target[1]
    targetVal = int(target[2])
    
    condition = r.split()

    condRegistr = condition[0]
    oper        = condition[1]
    condValue   = int(condition[2])

    #initialize new regs if not avail.
    if condRegistr not in regs:
        regs[condRegistr] = 0

    if targetReg not in regs:
        regs[targetReg] = 0

    # perform logic
    if ops[oper](regs[condRegistr], condValue):
        regs[targetReg] = ops[targetOp](regs[targetReg], targetVal)

    if koth < regs[targetReg]:
        koth = regs[targetReg]
    
    ip +=1
    
max(regs.values())
print(koth)

    
