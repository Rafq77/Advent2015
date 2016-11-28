#ring armor is -1 attack is +1
class Ppl:
    def __init__(self, Name, Hp, Dmg, Def):
        self.name = Name
        self.hp = Hp
        self.dmg = Dmg
        self.defe = Def
        
        self.wpn = 0
        self.rings = [0, 0]
        self.armor = 0

    def attack(self, Ppl):
        
        ringDamage = sum(filter(lambda x: x>0, self.rings))
        totalDmg = self.dmg + self.wpn + ringDamage

        print(self.name + " attacks for " + str(totalDmg))
        Ppl.takeDamage(totalDmg)

    def takeDamage(self, dmg):
        ringDefence = sum(filter(lambda x: x<0, self.rings)) * -1
        totalDef = self.defe + self.armor + ringDefence

        dmgDealt = dmg - totalDef
        if dmgDealt <= 0:
            dmgDealt = 1

        self.hp -= dmgDealt
        string = self.name + " takes damage for " + str(dmgDealt)
        if (self.hp <= 0):
            string += " and dies"
        else:
            string += " and has " + str(self.hp) + "hp remaining"
        print(string)


Enemy = Ppl("Boss", 103, 9, 2)
Player = Ppl("Hero", 100, 0, 0)

#Player.wpn = 7
#Player.armor = 2
#Player.rings.append(2)
#----- Dmg+2 ring is the winner hhere

#Player.wpn=8
#Player.arm = 5
##Player.rings.append(3)
#Player.rings.append(2)
#----

Player.wpn=8
#Player.arm = 5
Player.rings.append(2)
#Player.rings.append(2)
#----

# > 128


while Enemy.hp > 0 and Player.hp > 0:
    Player.attack(Enemy)
    Enemy.attack(Player)
