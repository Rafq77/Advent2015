fd = open("""../Resources/Day_25.txt""",'r')
s = fd.read()
fd.close()
S = s


def execute(a, instructions):
    #a = 7
    b = 0
    c = 0
    d = 0
    pc = 0
    expected = 0
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
        if instr[0] == "out":
            val = 0
            exec("val = %s" % (instr[1]))
            if val == expected:
                expected = val ^ 1
            else:
                break;
            print(val)
        pc+=1

_instructions = s.split('\n')
backup = list(_instructions)

A = 0
while(True):
    print("A:" + str(A))
    execute(A, _instructions)
    A +=1
#first task: a = 196
#second task with reverse eng. a = 12 --> 479008060
