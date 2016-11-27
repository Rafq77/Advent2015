

raw = "3113322113"
#raw = "1"
output = raw
#expected = "132123222113"


for x in range(50):
    #print(output)
    raw = output
    output = ''
    chain = False
    chainVal = ''
    lastVal = 'x'
    chainCnt = 1
    for i in range(len(raw)):

        try:
            if raw[i+1] == raw[i]:
                #start chain 
                if chain == False:
                    chainCnt = 2
                    chain = True
                else:
                    chainCnt = chainCnt + 1
            else:
                output = output + str(chainCnt) + raw[i]
                chainCnt = 1
        except IndexError:
            output = output + str(chainCnt) + raw[i]
            chainCnt = 1

        
        
        
        lastVal = i

    #output = output + str(chainCnt) + lastVal

#print(output)


    
    #rotated
    #for i in range(int(len(raw)/2)):
     #   part = raw[i*2:i*2+2]
        #p0 = int(part[0])
        #p1 = part[1]
        #output =  output + p0 * p1
        #raw = output

        
#if i == lastVal:
#           chain = True
#           chainCnt = chainCnt + 1
#            
#        elif (chain == True): #close chain
#            if lastVal == 'x':
#                lastVal = i
#            #print(str(chainCnt) + " times for lastVal=" + lastVal)
#            output = output + str(chainCnt) + lastVal
#            chain = False
#            chainCnt = 1
#
#        else:
#            chain = True
#           chainCnt = 1
