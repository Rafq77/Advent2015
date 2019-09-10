#task 1. spiral count of my pos.
# goal is: 368078
# task what is distance to middle
#next sqrt
i = 3
goal = 368078
while (i*i < goal):
    i+=2

dist =  i*i - goal
x = int(i/2) - (i - dist)
y = int(i/2) 
print(x+y + 1 )

def addSum(tab,x,y):
    total = 0;
    total += tab[x+1][y+0]
    total += tab[x+1][y+1]
    total += tab[x+0][y+1]
    total += tab[x-1][y+1]
    total += tab[x-1][y+0]
    total += tab[x-1][y-1]
    total += tab[x-0][y-1]
    total += tab[x+1][y-1]
    return total


direction = 'u'
def moveOne(ox,oy):
    global direction
    
    #move one extra right
    if (direction == 'r' and oy < 0 and (-ox == oy)):
        ox += 1 # change to next column
        direction = 'u'
        oy -= 1 #because it will be added in if below
    elif (direction == 'u' and ox == oy):
        direction = 'l'
    elif direction == 'l' and ox*-1 == oy:
        direction = 'd'
    elif direction == 'd' and oy == ox:
        direction = 'r'
        

    if (direction == 'r'):
        ox += 1
    elif (direction == 'u'):
        oy += 1
    elif (direction == 'l'):
        ox -= 1
    elif (direction == 'd'):
        oy -= 1

    return ox, oy
   
#prep big tab.
x = i
y = i
t = [ i[:] for i in [[0] * y] *x]

x = int(i/2)+1
y = int(i/2)+1
ox = 1 #offset from origin
oy = 0 #offset from origin

#init
t[x][y] = 1

#first step
t[x + ox][y + oy] = addSum(t, x+ox, y+oy)

candidate = 0
while (candidate < goal):
    
    ox, oy = moveOne(ox,oy)
    t[x + ox][y + oy] = addSum(t, x+ox, y+oy)

    candidate = t[x + ox][y + oy]
    print(candidate)


#fd = open("""../Resources/Day_06.txt""", 'r')
#s = fd.read()
#fd.close()

#import string
#from collections import Counter
#words = s.split('\n')


# last years solution leave for later :D
#mostCommon = ""
#leastCommon = ""
#for i in range(len(words[0])):
#    ss = "".join(list(map(lambda x: x[i], words)))
#    data = Counter(ss)
#    mostCommon += data.most_common()[0][0] #first
#    leastCommon += data.most_common()[-1][0] #last
#print(mostCommon)
#print(leastCommon)

    

    
