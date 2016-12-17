from hashlib import md5

pos = (0,0)
maxX = 3
maxY = 3
out = (3,3)

#both inclusive
accBeg = ord('b')
accEnd = ord('f')
maxLen = 9999
 
begin = "awrkjxxr" #??
#begin = "ihgpwlah" #DDRRRD
#begin = "kglvqrro" #DDUDRLRRUDRD
#begin = "ulqzkmiv" #DRURDRUDDLLDLUURRDULRLDUUDDDRR

#m = md5(begin.encode()).hexdigest()
foundExit = False
results = []
def checkDig(lPos, mdPath):
    global foundExit, results
    
    if lPos[0] < 0 or lPos[0] > maxX or lPos[1] < 0 or lPos[1] > maxY or len(mdPath) > maxLen:
        #print("invalid --> end")
        return False #invalidPos == outsideField.
    
    if lPos == out:
        foundExit = True
        results.append(mdPath)
        return #True

    tmpMd5 = md5(mdPath.encode()).hexdigest()

    u = tmpMd5[0] #up
    d = tmpMd5[1] #down
    l = tmpMd5[2] #left
    r = tmpMd5[3] #right
    #print(u+d+l+r)

    if ord(u) >= accBeg and ord(u) <= accEnd:
        done = checkDig((lPos[0], lPos[1] - 1 ), mdPath + 'U')
        #if done:
            #return True

    if ord(d) >= accBeg and ord(d) <= accEnd:
        done = checkDig((lPos[0], lPos[1] + 1 ), mdPath + 'D')
        #if done:
           # return True
        
    if ord(l) >= accBeg and ord(l) <= accEnd:
        done = checkDig((lPos[0] - 1, lPos[1]), mdPath + 'L')
      #  if done:
          #  return True
        
    if ord(r) >= accBeg and ord(r) <= accEnd:
        done = checkDig((lPos[0] + 1, lPos[1]), mdPath + 'R')
        #if done:
           # return True
        
    return
        
    

checkDig(pos, begin)
results.sort(key=len)
#part 1
print(results[0])
print(len(results[-1])-len(begin))
