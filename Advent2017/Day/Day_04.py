import os
import string
import re
import itertools

pBrckts = """\[[a-z]+\]"""
from collections import Counter

    
fd = open("""Resources/Day_04.txt""", 'r')
s = fd.read()
lines = s.split('\n')
cnt = 0
topKek = 0
advancedKek = 0

for line in lines:
    cnt += 1
    words = line.split()
    if [i for i in itertools.combinations(words, 2) if i[0] == i[1]]:
        topKek +=1

    # not efficient but check all permutations.
    # "the other guy", did it by sorting all the words and comparing set lengths.
    # set cannot carry duplicate, therefore if sorted it will filter automatically the dups.
    valid = True;
    for pair in [i for i in itertools.combinations(words, 2) if len(i[0]) == len(i[1])]:
        if valid == False:
            break;
        for word in itertools.permutations(pair[0]):
            if "".join(word) == pair[1]:
                advancedKek += 1
                valid = False;
                break;
 
print(cnt)
print("Lines with duplicate words " + str(topKek))
print("Task 1 valid lines " + str(cnt-topKek))
print("Task 2 valid lines " + str(cnt-advancedKek))
    




    

    
