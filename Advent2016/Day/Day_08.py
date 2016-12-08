fd = open("""../Resources/Day_08.txt""", 'r')
s = fd.read()
fd.close()

words = s.split('\n')

# # - 1 - on 
# . - 0 - off
#50x6
screen = [ [ 0 for i in range(6)] for i in range(50)]

#instructions
#rect - switches on the lights
#rotate col (Y coord)
#rotate row (X coord)

ex = 0
for i in words:
    rot = 0;
    
    if (i.find("row") != -1):
        s = i.split(' ')
        by = int(s[-1])
        y = int(s[2].split('=')[1])
        t = list(map(lambda z: z[y],screen))
        t = t[-by:] + t[:-by]
        for j in range(50):
            screen[j][y] = t[j]
        
        
    if (i.find("column") != -1):
        s = i.split(' ')
        by = int(s[-1])
        x = int(s[2].split('=')[1])
        screen[x] = screen[x][-by:] + screen[x][:-by]

    #XxY
    if (i.find("rect") != -1):
        xy = i.split(' ')[1].split('x')
        x = int(xy[0])
        y = int(xy[1])
        for I in range(x):
            for J in range(y):
                screen[I][J] = 1

#task 1
print(sum([sum(i) for i in screen]))

#task 2
a = ''
for i in range(6):
	for j in range(50):
		a+= screen[j][i] and '#' or ' '
	print(a)
	a = ''

    
