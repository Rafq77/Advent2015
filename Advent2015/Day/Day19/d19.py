mol = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

dic = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg""".split('\n')

output = set()
output.add('HF')
output.add('NAl')
output.add('OMg')

cnt = 1

#for el in dic:
 #   tmp = el.split(' => ')
  #  key = tmp[0]
   # val = tmp[1]

#    replacements = mol.count(key)
 #   idx = -1
  #  dist = len(key)
   # for i in range(replacements):
    #    idx = mol.index(key, idx + 1)
     #   out = mol[:idx] + val + mol[idx+dist:]
      #  output.add(out)


from random import shuffle

# dug out from internet, this is not my solution

reps = []
for el in dic:
    tmp = el.split(' => ')
    key = tmp[0]
    val = tmp[1]
    reps.append((key, val))
    

#reps = [('Al', 'ThF), ...]
#mol = "CRnCaCa..."

target = mol
part2 = 0

while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = mol
        part2 = 0
        shuffle(reps)

print(part2)
    
