#House 1 got 10 presents.
#House 2 got 30 presents.
#House 3 got 40 presents.
#House 4 got 70 presents.
#House 5 got 60 presents.
#House 6 got 120 presents.
#House 7 got 80 presents.
#House 8 got 150 presents.
#House 9 got 130 presents

target = 36000000
limit = 10
limit = 1500000


cnt = 1
#cnt = 1000000
reusable = {}

for i in range(limit):
    reusable[i] = 0
#1
#while cnt < limit and cont:
 #   for i in range(cnt,limit,cnt):
  #      reusable[i] += cnt*10
   #  
    #    if reusable[cnt] > target:
     #       print("GOT")
      #      cont = False
       #     break
    #cnt += 1


cont = True
while cnt < limit and cont:
    for i in range(cnt,min(cnt*50+1,limit),cnt):
        reusable[i] += cnt*11
     
        if reusable[cnt] > target:
            print("GOT")
            cont = False
            break
    cnt += 1



