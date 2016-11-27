#Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
#Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
#Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
#For example:

# no i o l
# obligatory aa bb zz ([a-z]).*\1
# abc

#hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
#abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
#abbcegjk fails the third requirement, because it only has one double letter (bb).
#The next password after abcdefgh is abcdffaa.
#The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
#Given Santa's current password (your puzzle input), what should his next password be?

#Your puzzle input is vzbxkghb.
import re

#raw = "ghijklmn " #ghjaabcc
#raw = "ghizzzaa " #ghjaabcc
raw = "vzbxkghb "
#raw = "vzbxxzaa " answer for first one
raw = "vzbzbcde "

wrk = True
pat = re.compile("[iol]+")
dbl = re.compile(r"(([a-z].*)\2.*){2,}")

def Increment(a):
    if ord(a[-1])+1 < 123:
        a = a[:-1] + chr(ord(a[-1]) + 1)
    else:
        a = Increment(a[:-1]) + 'a'
    return a
    

while (wrk):
    #print(raw)
    tab = list(map(lambda c: ord(c), raw))

    #seek 3 in a row
    sucess = 0
    for i in range(len(tab)-1):
        if (tab[i] == tab[i+1]-1):
            sucess += 1
        else:
            sucess = 0

        if (sucess >= 2): # we have 3 in row
            if not(pat.search(raw)): # no i o l
                if (dbl.search(raw)):
                    print("SUCCESS!")
                    print(raw)
                    wrk = False
                    break

    raw = Increment(raw[:-1]) + " "
                
            
            
