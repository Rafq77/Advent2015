fd = open("""Resources/Day_23.txt""", 'r')
s = fd.read()
fd.close()
S = s

def execute(a, instructions):
    #a = 7
    b = 0
    c = 0
    d = 0
    pc = 0
    programSize = len(instructions)
    while (pc < programSize):
        instr = instructions[pc].split(' ')
        if instr[0] == "cpy":
            exec("%s = %s" % (instr[2], instr[1]))
        if instr[0] == "jnz":
            tmp = 0
            exec("%s = %s" % ('tmp', instr[1]))
            if (tmp != 0):
                  exec("%s = %s" % ('tmp', instr[2]))
                  pc += int(tmp)
                  continue
        if instr[0] == "inc":
            exec("%s = %s + 1" % (instr[1], instr[1]))
        if instr[0] == "dec":
            exec("%s = %s - 1" % (instr[1], instr[1]))
        if instr[0] == "tgl":
            val = 0
            exec("val = %s" % (instr[1]))
            if (pc+val) < len(instructions):
                line2Replace = instructions[pc+val]
                newInstr = replaceInstr(line2Replace)
                instructions[pc+val] = newInstr
        pc+=1
    print(a) 

def replaceInstr(line):
    asm = line[:3]
    if asm == 'inc':
        nAsm = 'dec'
    elif asm == 'dec':
        nAsm = 'inc'
    elif asm == 'jnz':
        nAsm = 'cpy'
    elif asm == 'tgl':
        nAsm = 'inc'
    else:
        nAsm = 'jnz'

    line = nAsm + line[3:]
    return line

_instructions = s.split('\n')
backup = list(_instructions)
'''_instructions = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a""".split('\n')'''
execute(7, _instructions)
#first task: a = 7 --> 11500
#second task with reverse eng. a = 12 --> 479008060
