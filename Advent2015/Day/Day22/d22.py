import copy

class Spell:
    def __init__ (self, Name, Cost = 0, TTL = 0, Dmg = 0, Heal = 0 , Armor = 0, Mana = 0):
        self.name = Name
        self.cost = Cost
        self.ttl = TTL
        self.dmg = Dmg
        self.heal = Heal
        self.armor = Armor
        self.mana = Mana

    def work(self, player, enemy):
        player.mana += self.mana
        player.armor += self.armor
        self.armor = 0
        player.hp += self.heal
        enemy.hp -= self.dmg
        self.ttl -= 1
        print("The Spell " + self.name + " works!; ttl is " + str(self.ttl))
        if self.ttl == 0:
            print("The Spell " + self.name + " WORNS OFF!")
            if self.name == 'Shield':
                player.armor = 0
        

class Ppl:
    def __init__(self, Name, Hp, Dmg, Mana):
        self.name = Name
        self.hp = Hp
        self.dmg = Dmg
        self.mana = Mana
        self.armor = 0

    def attack(self, ppl):

        dmg = self.dmg 
        ppl.takeDamage(dmg)

    def takeDamage(self, totalDmg):
        dmg = totalDmg - self.armor
        if dmg < 0:
            dmg = 0
        self.hp -= dmg
        if self.hp <= 0:
            print(self.name + " dies!")

    def status(self):
        print(self.name + " has " + str(self.hp) + "hp " + str(self.armor) + " armor and " + str(self.mana) + " mana")

spells = {}
spell = Spell("Magic Missile", 53, 0, 4)
spells[spell.name] = spell

spell = Spell("Drain", 73, 0, 2, 2)
spells[spell.name] = spell

spell = Spell("Shield", 113, 6, 0, 0, 7)
spells[spell.name] = spell

spell = Spell("Poison", 173, 6, 3)
spells[spell.name] = spell

spell = Spell("Recharge", 229, 5, 0,0,0, 101)
spells[spell.name] = spell

activeEffects = []

#Hit Points: 51 Damage: 9
enemy = Ppl("Boss", 51, 9, 0)
player = Ppl("Player", 50, 0, 500)

PlayerTurn = True
manaCost = 0
# #2
hardMode = False

while enemy.hp > 0 and player.hp > 0:
    for effect in activeEffects:
        effect.work(player, enemy)

    activeEffects = list(filter(lambda x: x.ttl > 0, activeEffects))
        
        #if effect.ttl <= 0:
         #   print("The Spell " + effect.name + " WORNS OFF!")
          #  if effect.name == 'Shield':
           #     player.armor = 0
            #activeEffects.remove(effect)

    enemy.status()
    player.status()
    
    if PlayerTurn:
        print("--Player turn--")
        if hardMode:
            player.hp -=1
            print("Hard Mode: Loose 1hp, player has now: " + str(player.hp))
            if player.hp <= 0:
                continue
        ActionIsNotLegit = True
        while ActionIsNotLegit:
            action = input("choose action: (Magic Missile, Drain, Shield, Poison, Recharge)\n")
            
            if action == '0':
                action = "Magic Missile"
            elif action == '1':
                action = "Drain"
            elif action == '2':
                action = "Shield"
            elif action == '3':
                action = "Poison"
            elif action == '4':
                action = "Recharge"
                
            if len(list(filter(lambda x: x.name == action, activeEffects))) == 0:

                if action not in spells:
                    print("Spell not recognized!")
                    continue
                
                spell = copy.deepcopy(spells[action])
                if player.mana - spell.cost < 0:
                    print("cannot cast spell, not enough mana!")
                    continue

                ActionIsNotLegit = False
                player.mana -= spell.cost
                manaCost += spell.cost
                print("Casting spell " + spell.name + " ttl=" + str(spell.ttl))
                if spell.ttl != 0:
                    activeEffects.append(spell)
                else:
                    #one timer
                    player.hp += spell.heal
                    enemy.hp -= spell.dmg
            else:
                print("Cannot cast this spell again")
                ActionIsNotLegit = True
                    
    else:
        print("--Boss turn--")
        enemy.attack(player)
    PlayerTurn ^= True
    print("\n")

print("GAME OVER")
#0
#0
#0
#0
#3
#2
#4
#3
#900 ;)

#0
#0
#0
#0
#2
#1
#3
#2
#4 #algo result

#0
#0
#0
#2 
#4 
#0 
#3
#2
#4
#3 1242 too high


# 0000 22  33  44
# 212 226 346 458

# 0 M 53
# 1 D 73
# 2 S 113
# 3 P 173
# 4 R 229

#0
#3
#4
#2
#3
#4
#1
#3 1216 correct result (Poison is the key)

# 314 324 3 0



