fd = open("""../Resources/Day_09.txt""", 'r')
src = fd.read()
fd.close()

#lines = src.split('\n')
#print("Length: " + str(len(lines)))

#ut

#src = "{{{},{},{{}}}}" # 6 groups
#src = "{<{},{},{{}}>}" # 1 group
#src = "{<a>,<a>,<a>,<a>}" # 1 group
#src = "{{<a>},{<a>},{<a>},{<a>}}" # 5 groups
#src = "{{<!>},{<!>},{<!>},{<a>}}" # 2 groups
#src = "{{{}}}" # 6 score
#src = "{{{},{},{{}}}}" # 16 score
#src = "{{<ab>},{<ab>},{<ab>},{<ab>}}" # 9 score
#src = "{{<!!>},{<!!>},{<!!>},{<!!>}}" # 9 score
#src = "{{<a!>},{<a!>},{<a!>},{<ab>}}" # 3 score
#src = "<{o\"i!a,<{i<a>" #10 char


groupCount = 0
c = src
deep = 0
garbage = False
score = 0
trash = 0

i = 0
while i < len(src):

    if c[i] == '{' and garbage == False:
        deep += 1
    elif c[i] == '}' and garbage == False:
        groupCount += 1
        score += deep
        deep -= 1
    elif c[i] == '<' and garbage == False:
        garbage = True
    elif c[i] == '>':
        garbage = False
    elif c[i] == '!':
        #ignore next Char
        i+=1
    elif garbage == True:
        trash += 1
        
    i+=1
    
print(groupCount)
print("score: " + str(score))
print("trash: " + str(trash))
