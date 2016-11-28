lookupRow = 3010
lookupCol = 3019

init = 20151125
row = 1
col = 1

p = 252533
m = 33554393


val = init
lastRow = 1

while row != lookupRow or col != lookupCol:
    val = (val*p)%m
    if row == 1:
        lastRow += 1
        row = lastRow
        col = 1
    else:
        row -= 1
        col += 1

    #if row==3000 or :
     #   print(row)
      #  print(col)
    


