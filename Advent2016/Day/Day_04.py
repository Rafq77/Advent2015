from collections import Counter

#[('o', 3), ('r', 2), ('a', 2), ('e', 1), ('m', 1), ('l', 1), ('t', 1), ('n', 1)]
def most_common(lst):
    data = Counter(lst)
    return data.most_common()

inp = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""

fd = open("""../Resources/Day_04.txt""", 'r')
inp = fd.read()
fd.close()

#task 1
sectors = 0

#task 2
import string
abc = string.ascii_lowercase

rooms = inp.split('\n')
for i in rooms:
  doorname = i.split('[')
  word = doorname[0] 
  letters = word.split('-')[:-1]
  sectorId = int(word.split('-')[-1])
  checksum = doorname[1].rstrip(']')
  letters = ''.join(letters)

  x = sorted(most_common(letters), key=lambda t: (-t[1], t[0]))
  calculatedChecksum = ''.join(map(lambda t: t[0], x[:5]))
  
  if (checksum == calculatedChecksum):
    sectors = sectors + sectorId
    
  # task 2
  mod = sectorId%26
  letters = letters.replace('-','')
  
  val = ''.join(map(lambda x: abc[(ord(x)-97+mod)%26], letters))
  if val == "northpoleobjectstorage":
    print("storage id:" + str(sectorId))

print("not decoys: " + str(sectors))