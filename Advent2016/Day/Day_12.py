fd = open("""../Resources/Day_12.txt""", 'r')
s = fd.read()
fd.close()
S = s

def execute():
    while (pc < programSize):
        instr = instructions[pc].split(' ')
        if instr[0] == "cpy":
            exec("%s = %s" % (instr[2], instr[1]))
        if instr[0] == "jnz":
            tmp = 0
            exec("%s = %s" % ('tmp', instr[1]))
            if (tmp != 0):
                  pc += int(instr[2])
                  continue
        if instr[0] == "inc":
            exec("%s = %s + 1" % (instr[1], instr[1]))
        if instr[0] == "dec":
            exec("%s = %s - 1" % (instr[1], instr[1]))
        pc+=1


a = 0
b = 0
c = 0
d = 0
pc = 0
instructions = s.split('\n')
programSize = len(instructions)

execute()


a = 0
b = 0
c = 1
d = 0
pc = 0
execute()

