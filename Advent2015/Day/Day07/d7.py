class Gate:
    idx = ""
    fn  =""
    cnt = 0
    output = 0

    def __init__(self, _id, _fn):
        self.idx = _id
        self.fn = _fn
        self.output = 0
        self.input = []
        self.done = False
        self.rdy = False

        self.cnt = self.fn.count(' ')

        if (self.cnt == 0): # input
            self.rdy = False
            self.done = True
            try: 
                self.output = int(self.fn.split(' ')[0])
            except ValueError:
                self.done = False
                self.input = [self.fn.split(' ')[0]]
            self.cnt = 0
            self.keyword = "BIND"
        elif (self.cnt == 1): # NOT
            self.cnt = 1
            self.keyword = self.fn.split(' ')[0]
            self.input = [self.fn.split(' ')[1]]
        elif (self.cnt == 2): # OR AND (two operands) // LSHIFT RSHIFT (only 1 input)
            self.cnt = 2
            self.keyword = self.fn.split(' ')[1]
            if (self.keyword[1:] == "SHIFT"):
                self.input = [self.fn.split(' ')[0], int(self.fn.split(' ')[2])]    
            else:
                a = self.fn.split(' ')[0]
                b = self.fn.split(' ')[2]
                try:
                    a = int(a)
                except ValueError:
                    []
                    # nuttin
                try:
                    b = int(b)
                except ValueError:
                    []
                    # nothig
                self.input = [a, b]
        else:
            self.cnt = 3
            raise("ERROR!!!!")
        
        #literalsNeeded

    def Update(self):
            if (len(self.input) == 2):
                if (type(self.input[0]) == type(self.input[1]) == type(0)):
                    self.rdy = True
            elif (len(self.input) == 1):
                if (type(self.input[0]) == type(0)):
                    self.rdy = True
    

    def Simulate(self):
        if ((self.rdy == True) & (self.done == False)):
            #print("Done! " + self.idx + " " + self.fn)
            self.rdy = False
            self.done = True
            if (self.keyword == "AND"):
                self.output = self.input[0] & self.input[1]
                print(self.fn)
                print(str(self.input[0]) + " & " + str(self.input[1]) + " -> " + str(self.output))
            elif (self.keyword == "OR"):
                self.output = self.input[0] | self.input[1]
                print(str(self.input[0]) + " | " + str(self.input[1]) + " -> " + str(self.output))
            elif (self.keyword == "LSHIFT"):
                self.output = self.input[0] << self.input[1]
                print(str(self.input[0]) + " << " + str(self.input[1]) + " -> " + str(self.output))
            elif (self.keyword == "RSHIFT"):
                self.output = self.input[0] >> self.input[1]
                print(str(self.input[0]) + " >> " + str(self.input[1]) + " -> " + str(self.output))
            elif (self.keyword == "NOT"):
                self.output = ~self.input[0]
                print("~" + str(self.input[0]) + " -> " + str(self.output))
            elif (self.keyword == "BIND"):
                self.output =  self.input
                print(str(self.input[0]) + " -> " + str(self.output))
            else:
                print("No operation for" + self.keyword)


                
   # case function do it and or etc. 
    #16076
fd = open("""../../Resources/Day_07.txt""", 'r')
s = fd.read()
fd.close()
gatesString = s.split('\n')

gates = list(map(lambda gate: Gate(gate.split(" -> ")[1], gate.split(" -> ")[0]),gatesString))

#todo = list(filter(lambda gate: gate.done == False, gates))
todo = gates
root = gates
done = []

while (len(todo) > 0):
    #print("\nTODO :" + str(len(todo)))

    done = list(filter(lambda gate: gate.done == True, todo)) + done
    todo = list(filter(lambda gate: gate.done == False, todo))
    
    for i in done:
        key = i.idx
        for j in todo:
            if (j.input[0] == key):
                j.input[0] = i.output
                #print("Replace in out " + j.idx + " - " + j.fn)
            if (len(j.input) > 1):
                if (j.input[1] == key):
                    #print("  ... cotinued")
                    j.input[1] = i.output

    for i in todo:
        i.Update()
        i.Simulate()