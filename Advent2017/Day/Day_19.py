import itertools
fd = open("""Resources/Day_19.txt""", 'r')
src = fd.read()
tab = src.split('\n')

x = 1
y = 0
d = 'd' # direction, u,d,l,r

word = ''

finished = False
it = 0
while(finished == False):
    it+=1
    if d == 'd':
        y += 1
    elif d == 'u':
        y -= 1
    elif d == 'r':
        x += 1
    elif d == 'l':
        x -= 1

    if tab[y][x] == '|' or tab[y][x] == '-':
        #continue
        continue
    elif tab[y][x] == '+':
        #change dir except the one that i came from....
        if d == 'u' or d == 'd':
            #check left right
            if tab[y][x+1] != ' ':
                d = 'r'
            elif tab[y][x-1] != ' ':
                d = 'l'
        else:
            #it is going to be up down
            if tab[y+1][x] != ' ':
                d = 'd'
            elif tab[y-1][x] != ' ':
                d = 'u'
        
    elif tab[y][x] == ' ':
        #error
        print("I'm outside")
        finished = True
    else:
        #must be a letter
        word += tab[y][x]


    
        
print(word)
print(it)
