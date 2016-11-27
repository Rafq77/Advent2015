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
    
gatesString = """lf AND lq -> ls
iu RSHIFT 1 -> jn
bo OR bu -> bv
gj RSHIFT 1 -> hc
et RSHIFT 2 -> eu
bv AND bx -> by
is OR it -> iu
b OR n -> o
gf OR ge -> gg
NOT kt -> ku
ea AND eb -> ed
kl OR kr -> ks
hi AND hk -> hl
au AND av -> ax
lf RSHIFT 2 -> lg
dd RSHIFT 3 -> df
eu AND fa -> fc
df AND dg -> di
ip LSHIFT 15 -> it
NOT el -> em
et OR fe -> ff
fj LSHIFT 15 -> fn
t OR s -> u
ly OR lz -> ma
ko AND kq -> kr
NOT fx -> fy
et RSHIFT 1 -> fm
eu OR fa -> fb
dd RSHIFT 2 -> de
NOT go -> gp
kb AND kd -> ke
hg OR hh -> hi
jm LSHIFT 1 -> kg
NOT cn -> co
jp RSHIFT 2 -> jq
jp RSHIFT 5 -> js
1 AND io -> ip
eo LSHIFT 15 -> es
1 AND jj -> jk
g AND i -> j
ci RSHIFT 3 -> ck
gn AND gp -> gq
fs AND fu -> fv
lj AND ll -> lm
jk LSHIFT 15 -> jo
iu RSHIFT 3 -> iw
NOT ii -> ij
1 AND cc -> cd
bn RSHIFT 3 -> bp
NOT gw -> gx
NOT ft -> fu
jn OR jo -> jp
iv OR jb -> jc
hv OR hu -> hw
16076 -> b
gj RSHIFT 5 -> gm
hq AND hs -> ht
dy RSHIFT 1 -> er
ao OR an -> ap
ld OR le -> lf
bk LSHIFT 1 -> ce
bz AND cb -> cc
bi LSHIFT 15 -> bm
il AND in -> io
af AND ah -> ai
as RSHIFT 1 -> bl
lf RSHIFT 3 -> lh
er OR es -> et
NOT ax -> ay
ci RSHIFT 1 -> db
et AND fe -> fg
lg OR lm -> ln
k AND m -> n
hz RSHIFT 2 -> ia
kh LSHIFT 1 -> lb
NOT ey -> ez
NOT di -> dj
dz OR ef -> eg
lx -> a
NOT iz -> ja
gz LSHIFT 15 -> hd
ce OR cd -> cf
fq AND fr -> ft
at AND az -> bb
ha OR gz -> hb
fp AND fv -> fx
NOT gb -> gc
ia AND ig -> ii
gl OR gm -> gn
0 -> c
NOT ca -> cb
bn RSHIFT 1 -> cg
c LSHIFT 1 -> t
iw OR ix -> iy
kg OR kf -> kh
dy OR ej -> ek
km AND kn -> kp
NOT fc -> fd
hz RSHIFT 3 -> ib
NOT dq -> dr
NOT fg -> fh
dy RSHIFT 2 -> dz
kk RSHIFT 2 -> kl
1 AND fi -> fj
NOT hr -> hs
jp RSHIFT 1 -> ki
bl OR bm -> bn
1 AND gy -> gz
gr AND gt -> gu
db OR dc -> dd
de OR dk -> dl
as RSHIFT 5 -> av
lf RSHIFT 5 -> li
hm AND ho -> hp
cg OR ch -> ci
gj AND gu -> gw
ge LSHIFT 15 -> gi
e OR f -> g
fp OR fv -> fw
fb AND fd -> fe
cd LSHIFT 15 -> ch
b RSHIFT 1 -> v
at OR az -> ba
bn RSHIFT 2 -> bo
lh AND li -> lk
dl AND dn -> do
eg AND ei -> ej
ex AND ez -> fa
NOT kp -> kq
NOT lk -> ll
x AND ai -> ak
jp OR ka -> kb
NOT jd -> je
iy AND ja -> jb
jp RSHIFT 3 -> jr
fo OR fz -> ga
df OR dg -> dh
gj RSHIFT 2 -> gk
gj OR gu -> gv
NOT jh -> ji
ap LSHIFT 1 -> bj
NOT ls -> lt
ir LSHIFT 1 -> jl
bn AND by -> ca
lv LSHIFT 15 -> lz
ba AND bc -> bd
cy LSHIFT 15 -> dc
ln AND lp -> lq
x RSHIFT 1 -> aq
gk OR gq -> gr
NOT kx -> ky
jg AND ji -> jj
bn OR by -> bz
fl LSHIFT 1 -> gf
bp OR bq -> br
he OR hp -> hq
et RSHIFT 5 -> ew
iu RSHIFT 2 -> iv
gl AND gm -> go
x OR ai -> aj
hc OR hd -> he
lg AND lm -> lo
lh OR li -> lj
da LSHIFT 1 -> du
fo RSHIFT 2 -> fp
gk AND gq -> gs
bj OR bi -> bk
lf OR lq -> lr
cj AND cp -> cr
hu LSHIFT 15 -> hy
1 AND bh -> bi
fo RSHIFT 3 -> fq
NOT lo -> lp
hw LSHIFT 1 -> iq
dd RSHIFT 1 -> dw
dt LSHIFT 15 -> dx
dy AND ej -> el
an LSHIFT 15 -> ar
aq OR ar -> as
1 AND r -> s
fw AND fy -> fz
NOT im -> in
et RSHIFT 3 -> ev
1 AND ds -> dt
ec AND ee -> ef
NOT ak -> al
jl OR jk -> jm
1 AND en -> eo
lb OR la -> lc
iu AND jf -> jh
iu RSHIFT 5 -> ix
bo AND bu -> bw
cz OR cy -> da
iv AND jb -> jd
iw AND ix -> iz
lf RSHIFT 1 -> ly
iu OR jf -> jg
NOT dm -> dn
lw OR lv -> lx
gg LSHIFT 1 -> ha
lr AND lt -> lu
fm OR fn -> fo
he RSHIFT 3 -> hg
aj AND al -> am
1 AND kz -> la
dy RSHIFT 5 -> eb
jc AND je -> jf
cm AND co -> cp
gv AND gx -> gy
ev OR ew -> ex
jp AND ka -> kc
fk OR fj -> fl
dy RSHIFT 3 -> ea
NOT bs -> bt
NOT ag -> ah
dz AND ef -> eh
cf LSHIFT 1 -> cz
NOT cv -> cw
1 AND cx -> cy
de AND dk -> dm
ck AND cl -> cn
x RSHIFT 5 -> aa
dv LSHIFT 1 -> ep
he RSHIFT 2 -> hf
NOT bw -> bx
ck OR cl -> cm
bp AND bq -> bs
as OR bd -> be
he AND hp -> hr
ev AND ew -> ey
1 AND lu -> lv
kk RSHIFT 3 -> km
b AND n -> p
NOT kc -> kd
lc LSHIFT 1 -> lw
km OR kn -> ko
id AND if -> ig
ih AND ij -> ik
jr AND js -> ju
ci RSHIFT 5 -> cl
hz RSHIFT 1 -> is
1 AND ke -> kf
NOT gs -> gt
aw AND ay -> az
x RSHIFT 2 -> y
ab AND ad -> ae
ff AND fh -> fi
ci AND ct -> cv
eq LSHIFT 1 -> fk
gj RSHIFT 3 -> gl
u LSHIFT 1 -> ao
NOT bb -> bc
NOT hj -> hk
kw AND ky -> kz
as AND bd -> bf
dw OR dx -> dy
br AND bt -> bu
kk AND kv -> kx
ep OR eo -> eq
he RSHIFT 1 -> hx
ki OR kj -> kk
NOT ju -> jv
ek AND em -> en
kk RSHIFT 5 -> kn
NOT eh -> ei
hx OR hy -> hz
ea OR eb -> ec
s LSHIFT 15 -> w
fo RSHIFT 1 -> gh
kk OR kv -> kw
bn RSHIFT 5 -> bq
NOT ed -> ee
1 AND ht -> hu
cu AND cw -> cx
b RSHIFT 5 -> f
kl AND kr -> kt
iq OR ip -> ir
ci RSHIFT 2 -> cj
cj OR cp -> cq
o AND q -> r
dd RSHIFT 5 -> dg
b RSHIFT 2 -> d
ks AND ku -> kv
b RSHIFT 3 -> e
d OR j -> k
NOT p -> q
NOT cr -> cs
du OR dt -> dv
kf LSHIFT 15 -> kj
NOT ac -> ad
fo RSHIFT 5 -> fr
hz OR ik -> il
jx AND jz -> ka
gh OR gi -> gj
kk RSHIFT 1 -> ld
hz RSHIFT 5 -> ic
as RSHIFT 2 -> at
NOT jy -> jz
1 AND am -> an
ci OR ct -> cu
hg AND hh -> hj
jq OR jw -> jx
v OR w -> x
la LSHIFT 15 -> le
dh AND dj -> dk
dp AND dr -> ds
jq AND jw -> jy
au OR av -> aw
NOT bf -> bg
z OR aa -> ab
ga AND gc -> gd
hz AND ik -> im
jt AND jv -> jw
z AND aa -> ac
jr OR js -> jt
hb LSHIFT 1 -> hv
hf OR hl -> hm
ib OR ic -> id
fq OR fr -> fs
cq AND cs -> ct
ia OR ig -> ih
dd OR do -> dp
d AND j -> l
ib AND ic -> ie
as RSHIFT 3 -> au
be AND bg -> bh
dd AND do -> dq
NOT l -> m
1 AND gd -> ge
y AND ae -> ag
fo AND fz -> gb
NOT ie -> if
e AND f -> h
x RSHIFT 3 -> z
y OR ae -> af
hf AND hl -> hn
NOT h -> i
NOT hn -> ho
he RSHIFT 5 -> hh""".split('\n')

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


log = """Replace in out o - b OR n
Replace in out v - b RSHIFT 1
Replace in out p - b AND n
Replace in out f - b RSHIFT 5
Replace in out d - b RSHIFT 2
Replace in out e - b RSHIFT 3
Replace in out t - c LSHIFT 1
Done! t c LSHIFT 1
Done! v b RSHIFT 1
Done! f b RSHIFT 5
Done! d b RSHIFT 2
Done! e b RSHIFT 3
Replace in out u - t OR s
Replace in out x - v OR w
Replace in out k - d OR j
Replace in out l - d AND j
Replace in out g - e OR f
Replace in out h - e AND f
Done! g e OR f
Done! h e AND f
Replace in out j - g AND i
Replace in out i - NOT h
Done! i NOT h
Done! j g AND i
Done! k d OR j
Done! l d AND j
Replace in out n - k AND m
Replace in out m - NOT l
Done! m NOT l
Done! n k AND m
Done! o b OR n
Done! p b AND n
Replace in out r - o AND q
Replace in out q - NOT p
Done! q NOT p
Done! r o AND q
Done! s 1 AND r
Replace in out w - s LSHIFT 15
Done! u t OR s
Done! w s LSHIFT 15
Replace in out ao - u LSHIFT 1
Done! ao u LSHIFT 1
Done! x v OR w
Replace in out ap - ao OR an
Replace in out ak - x AND ai
Replace in out aq - x RSHIFT 1
Replace in out aj - x OR ai
Replace in out aa - x RSHIFT 5
Replace in out y - x RSHIFT 2
Replace in out z - x RSHIFT 3
Done! aq x RSHIFT 1
Done! aa x RSHIFT 5
Done! y x RSHIFT 2
Done! z x RSHIFT 3
Replace in out as - aq OR ar
Replace in out ag - y AND ae
Replace in out af - y OR ae
Replace in out ab - z OR aa
Replace in out ac - z AND aa
Done! ab z OR aa
Done! ac z AND aa
Replace in out ae - ab AND ad
Replace in out ad - NOT ac
Done! ad NOT ac
Done! ae ab AND ad
Done! ag y AND ae
Done! af y OR ae
Replace in out ah - NOT ag
Replace in out ai - af AND ah
Done! ah NOT ag
Done! ai af AND ah
Done! ak x AND ai
Done! aj x OR ai
Replace in out al - NOT ak
Replace in out am - aj AND al
Done! al NOT ak
Done! am aj AND al
Done! an 1 AND am
Replace in out ar - an LSHIFT 15
Done! ap ao OR an
Done! ar an LSHIFT 15
Replace in out bj - ap LSHIFT 1
Done! bj ap LSHIFT 1
Done! as aq OR ar
Replace in out bk - bj OR bi
Replace in out bl - as RSHIFT 1
Replace in out av - as RSHIFT 5
Replace in out be - as OR bd
Replace in out bf - as AND bd
Replace in out at - as RSHIFT 2
Replace in out au - as RSHIFT 3
Done! bl as RSHIFT 1
Done! av as RSHIFT 5
Done! at as RSHIFT 2
Done! au as RSHIFT 3
Replace in out bn - bl OR bm
Replace in out bb - at AND az
Replace in out ba - at OR az
Replace in out ax - au AND av
Replace in out aw - au OR av
Done! ax au AND av
Done! aw au OR av
Replace in out ay - NOT ax
Replace in out az - aw AND ay
Done! ay NOT ax
Done! az aw AND ay
Done! bb at AND az
Done! ba at OR az
Replace in out bc - NOT bb
Replace in out bd - ba AND bc
Done! bc NOT bb
Done! bd ba AND bc
Done! be as OR bd
Done! bf as AND bd
Replace in out bh - be AND bg
Replace in out bg - NOT bf
Done! bg NOT bf
Done! bh be AND bg
Done! bi 1 AND bh
Replace in out bm - bi LSHIFT 15
Done! bm bi LSHIFT 15
Done! bk bj OR bi
Replace in out ce - bk LSHIFT 1
Done! ce bk LSHIFT 1
Done! bn bl OR bm
Replace in out cf - ce OR cd
Replace in out bp - bn RSHIFT 3
Replace in out cg - bn RSHIFT 1
Replace in out bo - bn RSHIFT 2
Replace in out ca - bn AND by
Replace in out bz - bn OR by
Replace in out bq - bn RSHIFT 5
Done! bp bn RSHIFT 3
Done! cg bn RSHIFT 1
Done! bo bn RSHIFT 2
Done! bq bn RSHIFT 5
Replace in out br - bp OR bq
Replace in out bs - bp AND bq
Replace in out ci - cg OR ch
Replace in out bv - bo OR bu
Replace in out bw - bo AND bu
Done! br bp OR bq
Done! bs bp AND bq
Replace in out bu - br AND bt
Replace in out bt - NOT bs
Done! bt NOT bs
Done! bu br AND bt
Done! bv bo OR bu
Done! bw bo AND bu
Replace in out by - bv AND bx
Replace in out bx - NOT bw
Done! bx NOT bw
Done! by bv AND bx
Done! ca bn AND by
Done! bz bn OR by
Replace in out cb - NOT ca
Replace in out cc - bz AND cb
Done! cb NOT ca
Done! cc bz AND cb
Done! cd 1 AND cc
Replace in out ch - cd LSHIFT 15
Done! cf ce OR cd
Done! ch cd LSHIFT 15
Replace in out cz - cf LSHIFT 1
Done! ci cg OR ch
Done! cz cf LSHIFT 1
Replace in out ck - ci RSHIFT 3
Replace in out db - ci RSHIFT 1
Replace in out cl - ci RSHIFT 5
Replace in out cv - ci AND ct
Replace in out cj - ci RSHIFT 2
Replace in out cu - ci OR ct
Replace in out da - cz OR cy
Done! ck ci RSHIFT 3
Done! db ci RSHIFT 1
Done! cl ci RSHIFT 5
Done! cj ci RSHIFT 2
Replace in out cn - ck AND cl
Replace in out cm - ck OR cl
Replace in out dd - db OR dc
Replace in out cr - cj AND cp
Replace in out cq - cj OR cp
Done! cn ck AND cl
Done! cm ck OR cl
Replace in out co - NOT cn
Replace in out cp - cm AND co
Done! co NOT cn
Done! cp cm AND co
Done! cr cj AND cp
Done! cq cj OR cp
Replace in out cs - NOT cr
Replace in out ct - cq AND cs
Done! cs NOT cr
Done! ct cq AND cs
Done! cv ci AND ct
Done! cu ci OR ct
Replace in out cw - NOT cv
Replace in out cx - cu AND cw
Done! cw NOT cv
Done! cx cu AND cw
Done! cy 1 AND cx
Replace in out dc - cy LSHIFT 15
Done! dc cy LSHIFT 15
Done! da cz OR cy
Replace in out du - da LSHIFT 1
Done! dd db OR dc
Done! du da LSHIFT 1
Replace in out df - dd RSHIFT 3
Replace in out de - dd RSHIFT 2
Replace in out dw - dd RSHIFT 1
Replace in out dg - dd RSHIFT 5
Replace in out dp - dd OR do
Replace in out dq - dd AND do
Replace in out dv - du OR dt
Done! df dd RSHIFT 3
Done! de dd RSHIFT 2
Done! dw dd RSHIFT 1
Done! dg dd RSHIFT 5
Replace in out di - df AND dg
Replace in out dh - df OR dg
Replace in out dl - de OR dk
Replace in out dm - de AND dk
Replace in out dy - dw OR dx
Done! di df AND dg
Done! dh df OR dg
Replace in out dj - NOT di
Replace in out dk - dh AND dj
Done! dj NOT di
Done! dk dh AND dj
Done! dl de OR dk
Done! dm de AND dk
Replace in out do - dl AND dn
Replace in out dn - NOT dm
Done! dn NOT dm
Done! do dl AND dn
Done! dp dd OR do
Done! dq dd AND do
Replace in out ds - dp AND dr
Replace in out dr - NOT dq
Done! dr NOT dq
Done! ds dp AND dr
Done! dt 1 AND ds
Replace in out dx - dt LSHIFT 15
Done! dx dt LSHIFT 15
Done! dv du OR dt
Replace in out ep - dv LSHIFT 1
Done! ep dv LSHIFT 1
Done! dy dw OR dx
Replace in out eq - ep OR eo
Replace in out er - dy RSHIFT 1
Replace in out ek - dy OR ej
Replace in out dz - dy RSHIFT 2
Replace in out el - dy AND ej
Replace in out eb - dy RSHIFT 5
Replace in out ea - dy RSHIFT 3
Done! er dy RSHIFT 1
Done! dz dy RSHIFT 2
Done! eb dy RSHIFT 5
Done! ea dy RSHIFT 3
Replace in out et - er OR es
Replace in out eg - dz OR ef
Replace in out eh - dz AND ef
Replace in out ed - ea AND eb
Replace in out ec - ea OR eb
Done! ed ea AND eb
Done! ec ea OR eb
Replace in out ee - NOT ed
Replace in out ef - ec AND ee
Done! ee NOT ed
Done! ef ec AND ee
Done! eg dz OR ef
Done! eh dz AND ef
Replace in out ej - eg AND ei
Replace in out ei - NOT eh
Done! ei NOT eh
Done! ej eg AND ei
Done! ek dy OR ej
Done! el dy AND ej
Replace in out en - ek AND em
Replace in out em - NOT el
Done! em NOT el
Done! en ek AND em
Done! eo 1 AND en
Replace in out es - eo LSHIFT 15
Done! es eo LSHIFT 15
Done! eq ep OR eo
Replace in out fk - eq LSHIFT 1
Done! et er OR es
Done! fk eq LSHIFT 1
Replace in out eu - et RSHIFT 2
Replace in out ff - et OR fe
Replace in out fm - et RSHIFT 1
Replace in out fg - et AND fe
Replace in out ew - et RSHIFT 5
Replace in out ev - et RSHIFT 3
Replace in out fl - fk OR fj
Done! eu et RSHIFT 2
Done! fm et RSHIFT 1
Done! ew et RSHIFT 5
Done! ev et RSHIFT 3
Replace in out fc - eu AND fa
Replace in out fb - eu OR fa
Replace in out fo - fm OR fn
Replace in out ex - ev OR ew
Replace in out ey - ev AND ew
Done! ex ev OR ew
Done! ey ev AND ew
Replace in out fa - ex AND ez
Replace in out ez - NOT ey
Done! ez NOT ey
Done! fa ex AND ez
Done! fc eu AND fa
Done! fb eu OR fa
Replace in out fd - NOT fc
Replace in out fe - fb AND fd
Done! fd NOT fc
Done! fe fb AND fd
Done! ff et OR fe
Done! fg et AND fe
Replace in out fi - ff AND fh
Replace in out fh - NOT fg
Done! fh NOT fg
Done! fi ff AND fh
Done! fj 1 AND fi
Replace in out fn - fj LSHIFT 15
Done! fn fj LSHIFT 15
Done! fl fk OR fj
Replace in out gf - fl LSHIFT 1
Done! gf fl LSHIFT 1
Done! fo fm OR fn
Replace in out gg - gf OR ge
Replace in out ga - fo OR fz
Replace in out fp - fo RSHIFT 2
Replace in out fq - fo RSHIFT 3
Replace in out gh - fo RSHIFT 1
Replace in out fr - fo RSHIFT 5
Replace in out gb - fo AND fz
Done! fp fo RSHIFT 2
Done! fq fo RSHIFT 3
Done! gh fo RSHIFT 1
Done! fr fo RSHIFT 5
Replace in out fx - fp AND fv
Replace in out fw - fp OR fv
Replace in out ft - fq AND fr
Replace in out fs - fq OR fr
Replace in out gj - gh OR gi
Done! ft fq AND fr
Done! fs fq OR fr
Replace in out fu - NOT ft
Replace in out fv - fs AND fu
Done! fu NOT ft
Done! fv fs AND fu
Done! fx fp AND fv
Done! fw fp OR fv
Replace in out fy - NOT fx
Replace in out fz - fw AND fy
Done! fy NOT fx
Done! fz fw AND fy
Done! ga fo OR fz
Done! gb fo AND fz
Replace in out gd - ga AND gc
Replace in out gc - NOT gb
Done! gc NOT gb
Done! gd ga AND gc
Done! ge 1 AND gd
Replace in out gi - ge LSHIFT 15
Done! gg gf OR ge
Done! gi ge LSHIFT 15
Replace in out ha - gg LSHIFT 1
Done! ha gg LSHIFT 1
Done! gj gh OR gi
Replace in out hb - ha OR gz
Replace in out hc - gj RSHIFT 1
Replace in out gm - gj RSHIFT 5
Replace in out gw - gj AND gu
Replace in out gk - gj RSHIFT 2
Replace in out gv - gj OR gu
Replace in out gl - gj RSHIFT 3
Done! hc gj RSHIFT 1
Done! gm gj RSHIFT 5
Done! gk gj RSHIFT 2
Done! gl gj RSHIFT 3
Replace in out he - hc OR hd
Replace in out gr - gk OR gq
Replace in out gs - gk AND gq
Replace in out gn - gl OR gm
Replace in out go - gl AND gm
Done! gn gl OR gm
Done! go gl AND gm
Replace in out gq - gn AND gp
Replace in out gp - NOT go
Done! gp NOT go
Done! gq gn AND gp
Done! gr gk OR gq
Done! gs gk AND gq
Replace in out gu - gr AND gt
Replace in out gt - NOT gs
Done! gt NOT gs
Done! gu gr AND gt
Done! gw gj AND gu
Done! gv gj OR gu
Replace in out gx - NOT gw
Replace in out gy - gv AND gx
Done! gx NOT gw
Done! gy gv AND gx
Done! gz 1 AND gy
Replace in out hd - gz LSHIFT 15
Done! hd gz LSHIFT 15
Done! hb ha OR gz
Replace in out hv - hb LSHIFT 1
Done! he hc OR hd
Done! hv hb LSHIFT 1
Replace in out hq - he OR hp
Replace in out hg - he RSHIFT 3
Replace in out hf - he RSHIFT 2
Replace in out hr - he AND hp
Replace in out hx - he RSHIFT 1
Replace in out hh - he RSHIFT 5
Replace in out hw - hv OR hu
Done! hg he RSHIFT 3
Done! hf he RSHIFT 2
Done! hx he RSHIFT 1
Done! hh he RSHIFT 5
Replace in out hi - hg OR hh
Replace in out hj - hg AND hh
Replace in out hm - hf OR hl
Replace in out hn - hf AND hl
Replace in out hz - hx OR hy
Done! hi hg OR hh
Done! hj hg AND hh
Replace in out hl - hi AND hk
Replace in out hk - NOT hj
Done! hk NOT hj
Done! hl hi AND hk
Done! hm hf OR hl
Done! hn hf AND hl
Replace in out hp - hm AND ho
Replace in out ho - NOT hn
Done! ho NOT hn
Done! hp hm AND ho
Done! hq he OR hp
Done! hr he AND hp
Replace in out ht - hq AND hs
Replace in out hs - NOT hr
Done! hs NOT hr
Done! ht hq AND hs
Done! hu 1 AND ht
Replace in out hy - hu LSHIFT 15
Done! hw hv OR hu
Done! hy hu LSHIFT 15
Replace in out iq - hw LSHIFT 1
Done! iq hw LSHIFT 1
Done! hz hx OR hy
Replace in out ir - iq OR ip
Replace in out ia - hz RSHIFT 2
Replace in out ib - hz RSHIFT 3
Replace in out is - hz RSHIFT 1
Replace in out il - hz OR ik
Replace in out ic - hz RSHIFT 5
Replace in out im - hz AND ik
Done! ia hz RSHIFT 2
Done! ib hz RSHIFT 3
Done! is hz RSHIFT 1
Done! ic hz RSHIFT 5
Replace in out ii - ia AND ig
Replace in out ih - ia OR ig
Replace in out id - ib OR ic
Replace in out ie - ib AND ic
Replace in out iu - is OR it
Done! id ib OR ic
Done! ie ib AND ic
Replace in out ig - id AND if
Replace in out if - NOT ie
Done! if NOT ie
Done! ig id AND if
Done! ii ia AND ig
Done! ih ia OR ig
Replace in out ij - NOT ii
Replace in out ik - ih AND ij
Done! ij NOT ii
Done! ik ih AND ij
Done! il hz OR ik
Done! im hz AND ik
Replace in out io - il AND in
Replace in out in - NOT im
Done! in NOT im
Done! io il AND in
Done! ip 1 AND io
Replace in out it - ip LSHIFT 15
Done! it ip LSHIFT 15
Done! ir iq OR ip
Replace in out jl - ir LSHIFT 1
Done! iu is OR it
Done! jl ir LSHIFT 1
Replace in out jn - iu RSHIFT 1
Replace in out iw - iu RSHIFT 3
Replace in out iv - iu RSHIFT 2
Replace in out jh - iu AND jf
Replace in out ix - iu RSHIFT 5
Replace in out jg - iu OR jf
Replace in out jm - jl OR jk
Done! jn iu RSHIFT 1
Done! iw iu RSHIFT 3
Done! iv iu RSHIFT 2
Done! ix iu RSHIFT 5
Replace in out jp - jn OR jo
Replace in out iy - iw OR ix
Replace in out iz - iw AND ix
Replace in out jc - iv OR jb
Replace in out jd - iv AND jb
Done! iy iw OR ix
Done! iz iw AND ix
Replace in out jb - iy AND ja
Replace in out ja - NOT iz
Done! ja NOT iz
Done! jb iy AND ja
Done! jc iv OR jb
Done! jd iv AND jb
Replace in out jf - jc AND je
Replace in out je - NOT jd
Done! je NOT jd
Done! jf jc AND je
Done! jh iu AND jf
Done! jg iu OR jf
Replace in out ji - NOT jh
Replace in out jj - jg AND ji
Done! ji NOT jh
Done! jj jg AND ji
Done! jk 1 AND jj
Replace in out jo - jk LSHIFT 15
Done! jo jk LSHIFT 15
Done! jm jl OR jk
Replace in out kg - jm LSHIFT 1
Done! kg jm LSHIFT 1
Done! jp jn OR jo
Replace in out kh - kg OR kf
Replace in out jq - jp RSHIFT 2
Replace in out js - jp RSHIFT 5
Replace in out ki - jp RSHIFT 1
Replace in out kb - jp OR ka
Replace in out jr - jp RSHIFT 3
Replace in out kc - jp AND ka
Done! jq jp RSHIFT 2
Done! js jp RSHIFT 5
Done! ki jp RSHIFT 1
Done! jr jp RSHIFT 3
Replace in out jx - jq OR jw
Replace in out jy - jq AND jw
Replace in out kk - ki OR kj
Replace in out ju - jr AND js
Replace in out jt - jr OR js
Done! ju jr AND js
Done! jt jr OR js
Replace in out jv - NOT ju
Replace in out jw - jt AND jv
Done! jv NOT ju
Done! jw jt AND jv
Done! jx jq OR jw
Done! jy jq AND jw
Replace in out ka - jx AND jz
Replace in out jz - NOT jy
Done! jz NOT jy
Done! ka jx AND jz
Done! kb jp OR ka
Done! kc jp AND ka
Replace in out ke - kb AND kd
Replace in out kd - NOT kc
Done! kd NOT kc
Done! ke kb AND kd
Done! kf 1 AND ke
Replace in out kj - kf LSHIFT 15
Done! kh kg OR kf
Done! kj kf LSHIFT 15
Replace in out lb - kh LSHIFT 1
Done! lb kh LSHIFT 1
Done! kk ki OR kj
Replace in out lc - lb OR la
Replace in out kl - kk RSHIFT 2
Replace in out km - kk RSHIFT 3
Replace in out kx - kk AND kv
Replace in out kn - kk RSHIFT 5
Replace in out kw - kk OR kv
Replace in out ld - kk RSHIFT 1
Done! kl kk RSHIFT 2
Done! km kk RSHIFT 3
Done! kn kk RSHIFT 5
Done! ld kk RSHIFT 1
Replace in out ks - kl OR kr
Replace in out kt - kl AND kr
Replace in out kp - km AND kn
Replace in out ko - km OR kn
Replace in out lf - ld OR le
Done! kp km AND kn
Done! ko km OR kn
Replace in out kq - NOT kp
Replace in out kr - ko AND kq
Done! kq NOT kp
Done! kr ko AND kq
Done! ks kl OR kr
Done! kt kl AND kr
Replace in out kv - ks AND ku
Replace in out ku - NOT kt
Done! ku NOT kt
Done! kv ks AND ku
Done! kx kk AND kv
Done! kw kk OR kv
Replace in out ky - NOT kx
Replace in out kz - kw AND ky
Done! ky NOT kx
Done! kz kw AND ky
Done! la 1 AND kz
Replace in out le - la LSHIFT 15
Done! lc lb OR la
Done! le la LSHIFT 15
Replace in out lw - lc LSHIFT 1
Done! lf ld OR le
Done! lw lc LSHIFT 1
Replace in out ls - lf AND lq
Replace in out lg - lf RSHIFT 2
Replace in out lh - lf RSHIFT 3
Replace in out li - lf RSHIFT 5
Replace in out lr - lf OR lq
Replace in out ly - lf RSHIFT 1
Replace in out lx - lw OR lv
Done! lg lf RSHIFT 2
Done! lh lf RSHIFT 3
Done! li lf RSHIFT 5
Done! ly lf RSHIFT 1
Replace in out ln - lg OR lm
Replace in out lo - lg AND lm
Replace in out lk - lh AND li
Replace in out lj - lh OR li
Replace in out ma - ly OR lz
Done! lk lh AND li
Done! lj lh OR li
Replace in out ll - NOT lk
Replace in out lm - lj AND ll
Done! ll NOT lk
Done! lm lj AND ll
Done! ln lg OR lm
Done! lo lg AND lm
Replace in out lq - ln AND lp
Replace in out lp - NOT lo
Done! lp NOT lo
Done! lq ln AND lp
Done! ls lf AND lq
Done! lr lf OR lq
Replace in out lt - NOT ls
Replace in out lu - lr AND lt
Done! lt NOT ls
Done! lu lr AND lt
Done! lv 1 AND lu
Replace in out lz - lv LSHIFT 15
Done! lz lv LSHIFT 15
Done! lx lw OR lv
Replace in out a - lx
Done! ma ly OR lz
Done! a lx"""
