fd = open("""../Resources/Day_06.txt""", 'r')
s = fd.read()
fd.close()

import string
from collections import Counter
words = s.split('\n')

mostCommon = ""
leastCommon = ""
for i in range(len(words[0])):
    ss = "".join(list(map(lambda x: x[i], words)))
    data = Counter(ss)
    mostCommon += data.most_common()[0][0] #first
    leastCommon += data.most_common()[-1][0] #last
print(mostCommon)
print(leastCommon)

    

    
