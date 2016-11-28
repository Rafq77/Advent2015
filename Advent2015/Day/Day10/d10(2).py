raw = "3113322113 "
#raw = "1"
output = raw
#expected = "132123222113"


for x in range(50):
    print(x)
    raw = output + ' '
    output = ''
    chainCnt = 1
    length = len(raw)
    for i in range(len(raw) - 1):

        if raw[i+1] == raw[i]:
            chainCnt = chainCnt + 1
        else:
            output += str(chainCnt) + raw[i]
            chainCnt = 1
        lastVal = i
print(len(output))
