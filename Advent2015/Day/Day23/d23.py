desc = """
--- Day 23: Opening the Turing Lock ---

Little Jane Marie just got her very first computer for Christmas from some unknown benefactor.
It comes with instructions and an example program, but the computer itself seems to be malfunctioning.
She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions
(truly, it goes on to remind the reader, a state-of-the-art technology).
The registers are named a and b, can hold any non-negative integer, and begin with a value of 0.

The instructions are as follows:

hlf r sets register r to half its current value, then continues with the next instruction.
tpl r sets register r to triple its current value, then continues with the next instruction.
inc r increments register r, adding 1 to it, then continues with the next instruction.
jmp offset is a jump; it continues with the instruction offset away relative to itself.
jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

All three jump instructions work with an offset relative to that instruction.
The offset is always written with a prefix + or - to indicate the direction of the jump
(forward or backward, respectively).
For example, jmp +1 would simply continue with the next instruction,
while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

inc a
jio a, +2
tpl a
inc a
What is the value in register b when the program in your puzzle input is finished executing?

==================
--- Part Two ---

The unknown benefactor is very thankful for releasi-- er,
helping little Jane Marie with her computer.
Definitely not to distract you,
what is the value in register b after the program is finished executing if register a starts as 1 instead?

You can also [Share] this puzzle."""


instructions = """jio a, +18
inc a
tpl a
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +22
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7""".split("\n")


PC = 0
IP = 0

#reg = {'a' : 0, 'b' : 0 }
reg = {'a' : 1, 'b' : 0 }
jmp = False
while IP < len(instructions):
    instr = instructions[IP][:3]

    if instr == 'jio': # Jump if one (1)
        Rx = instructions[IP][4]
        if reg[Rx] == 1:
            jmp = True
            IP += int(instructions[IP][6:])
    elif instr == "jie": # Jump if equal (even)
        Rx = instructions[IP][4]
        if reg[Rx]%2 == 0:
            jmp = True
            IP += int(instructions[IP][6:])
    elif instr == 'jmp': # Jump
        IP += int(instructions[IP][3:])
        jmp = True
    elif instr == 'tpl': # Triple val (*3)
        Rx = instructions[IP][4]
        reg[Rx] *= 3
    elif instr == 'inc': # increment (+1)
        Rx = instructions[IP][4]
        reg[Rx] += 1
    elif instr == 'hlf': # half (divide 2, or RSHIFT 1)
        Rx = instructions[IP][4]
        reg[Rx] >>= 1

    if jmp:
        jmp = False
    else:
        IP += 1
