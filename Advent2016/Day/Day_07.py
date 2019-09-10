import os
import string
import re

pBrckts = """\[[a-z]+\]"""
from collections import Counter

def Abba(x):
    for i in range(len(x)-3):
        if (x[i] == x[i+3] and x[i+1] == x[i+2] and x[i] != x[i+1]):
            return True
    return False

def Kek(kek, eke):
    for i in range(len(kek)-2):
        if (kek[i] == kek[i+2] and kek[i] != kek[i+1]):
            for j in range(len(eke)-2):
                if (kek[i] == eke[j+1] and \
                    kek[i+1] == eke[j] and \
                    eke[j] == eke[j+2] and \
                    eke[j] != eke[j+1]):
                    return True
    return False
    
fd = open("""Resources/Day_07.txt""", 'r')
s = fd.read()
words = s.split('\n')
cnt = 0
topKek = 0

for word in words:
    fnds = re.findall(pBrckts, word)
    add = True
    if (list(filter(lambda x: Abba(x), fnds))):
       add = False

    for match in fnds:
        word = word.replace(match, '|')

    if (Kek(word, "".join(fnds))):
        topKek += 1
    if (Abba(word) and add):
        cnt+=1

print(cnt)
print("Top kek " + str(topKek))
    




    

    
