fd = open("""Resources/Day_11.txt""", 'r')
src = fd.read().replace('\n','')
steps = src.split(',')

x = 0
y = 0
koth = 0

for step in steps:
    if step == 'sw':
        x -= 1
        y -= 1
    elif step == 'nw':
        x -= 1
        y += 1
    elif step == 'se':
        x += 1
        y -= 1
    elif step == 'ne':
        x += 1
        y += 1
    elif step == 'n':
        y += 2
    elif step == 's':
        y -= 2

    t = y - x #diag
    t = t / 2 #vertical drop

    if koth < t+x:
        koth = t+x

print("x " + str(x))
print("y " + str(y))

t = y - x #diag
t = t / 2 #vertical drop
print("steps: " + str(t+x))
print("koth: " + str(koth))
