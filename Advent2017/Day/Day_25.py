"""HARDCODE

Begin in state A.
Perform a diagnostic checksum after 12399302 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state C.

In state B:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state D.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state D.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state D.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state F.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state B.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.
    

"""
#https://www.reddit.com/r/adventofcode/comments/7lzo3l/2017_day_25_solutions/drqas2o/
#because i wanted to do it with such a recipe book as in "tm"
steps = 12399302

a, b, c, d, e, f = range(6) #states enum
left, right = 0, 1 #move direction

tm = {
    (a, 0): (1, right, b),
    (a, 1): (0, right, c),

    (b, 0): (0, left, a),
    (b, 1): (0, right, d),

    (c, 0): (1, right, d),
    (c, 1): (1, right, a),

    (d, 0): (1, left, e),
    (d, 1): (0, left, d),

    (e, 0): (1, right, f),
    (e, 1): (1, left, b),

    (f, 0): (1, right, a),
    (f, 1): (1, right, e),
}

tape = {}
head, state = 0, a

for i in range(steps):
    val = tape.get(head, 0) #returns 0 if nothing at requested pos.
    wval, move, nextstate = tm.get((state, val))

    tape[head] = wval
    head = head+1 if move == right else head-1
    state = nextstate

print(sum(tape.values()))
