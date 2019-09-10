f = lambda x,y: x*x+3*x+2*x*y+y+y*y
key = 1352
demoKey = 10

isOdd = (bin(f(0,0) + 10)[2:]).count('1')%2

#zero is empty
#one is wall

#creates 2d array [x][y]
size = 50
a = [[(bin(f(x,y) + key)[2:]).count('1')%2 for y in range(size)]for x in range(size)]

for y in a:
	s = ''
	xC = 0
	for x in y:
		if (xC == 31 and yC == 39):
			s+= 'X'
			yC +=1
			xC +=1
			continue
		if (x == 1):
			s+='#'
		else:
			s+='.'
		xC+=1
	yC +=1
	print(s)


