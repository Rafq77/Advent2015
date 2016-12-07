import json
import re
fd = open("""../../Resources/Day_12.txt""", 'r')
jsonStr = fd.read()
fd.close()

j = json.loads(jsonStr)

cnt = 0

#part 1 is ok
pattern = "([-]?\d{1,})"
expression = re.compile(pattern)

for i in expression.findall(jsonStr):
    cnt += (int(i))

print(cnt)

#part 2 official JSON parse
cnt = 0
zer = 0

def Check(a, add=False):
    if (type(a) == type({})):
        CheckDict(a, add)
    elif(type(a) == type([])):
        CheckList(a, add)
    elif(type(a) == type(0)):
         global zer
         zer += a

def CheckDict(d, add=False):
    if list(filter(lambda x: x == 'red', d.values())):
        return
    
    for k, v in d.items():
         Check(v,add)
         Check(k,add)
    
def CheckList(l, add=False):
    for i in l:
         Check(i, add)
         
    
for i in j.keys():
    Check(j[i])
    
