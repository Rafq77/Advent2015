src = "nbysizxe"

tst1 = "flqrgnkx" # "##.#.#.." expectd in first row
#src = tst1

#take some knot_hash, courtesy of reddit.com/user/evonfriedland
from functools import reduce
def knot_hash(lengths, numbers):
    pos = 0
    skip = 0

    for length in lengths:
        to_flip = [(pos + i) % len(numbers) for i in range(length)]
        temp = list(numbers)
        for i in range(length):
            numbers[to_flip[i]] = temp[to_flip[-(i+1)]]
        pos += (length + skip)
        skip += 1

    return numbers

def sparse_hash(inpt):
    result = []
    for i in range(0, 256, 16):
        sh = reduce(lambda x, y: x ^ y, inpt[i:i+16])
        result.append(sh)
    return result


def dense_hash(inpt):
    result = []
    for sh in inpt:
        dh = hex(sh)[2:].zfill(2)
        result.append(dh)
    return ''.join(result)

grid = list()

for i in range(128):
    entry_key = src + '-' + str(i)
    lengths = [ord(char) for char in entry_key] + [17, 31, 73, 47, 23]
    lengths = lengths * 64
    numbers = list(range(256))

    knot_hashed = knot_hash(lengths, numbers)
    sparse_hashed = sparse_hash(knot_hashed)
    dense_hashed = dense_hash(sparse_hashed)

    # convert to binary grid
    grid.append(''.join([bin(int(x, 16))[2:].rjust(4,'0') for x in dense_hashed]))

print("part1 ('1' count):" + str(sum([x.count('1') for x in grid])))


visited = set()
cnt = 0

def dfs(x,y):
    #print(str(x) + ' | ' + str(y))
    if (x,y) in visited:
        return
    if grid[x][y] == '0':
        return
    visited.add((x,y))

    if (x > 0):
        dfs(x-1, y)
    if (y > 0):
        dfs(x, y-1)
    if (x < len(grid)-1):
        dfs(x+1, y)
    if (y < len(grid)-1):
        dfs(x, y+1)
    
for y in range(len(grid)):
    for x in range(len(grid)):
        if (x, y) in visited:
            continue #already seen
        elif grid[x][y] == '1':
            cnt +=1
            dfs(x,y) # find and save neighbour position
            
print("part2 (group count): " + str(cnt))
