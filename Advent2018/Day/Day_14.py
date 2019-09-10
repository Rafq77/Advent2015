from collections import deque
from collections import defaultdict
import itertools as it
inp = 939601
sinp = str(inp)
offset = 10

elf1 = 0
elf2 = 1

board = deque([3, 7])
it = 0
git = 0
while(len(board) < inp + offset): #solves part1
    total = board[elf1] + board[elf2]
    board.extend(list(map(int,str(total))))
    
    elf1 = (1 + board[elf1] + elf1)% len(board)
    elf2 = (1 + board[elf2] + elf2) % len(board)
print(list(board)[inp:inp+offset])

