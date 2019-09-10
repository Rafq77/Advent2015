import itertools
import re
from enum import Enum
from collections import deque
# intro = open("Resources/Day_24.txt").read().split('\n')
intro = open("Resources/Day_24test.txt").read().split('\n')

class Damage(Enum):
	Slash = 0 #bludgeon ? 
	Fire = 1
	Radiation = 2

class Weakness:
	def __init__(self):
		self.rad = False # not weak to radiation
		self.fire = False # not weak fire
		self.blud = False # ...

class Cells:
	def __init__(self, txt):
		self.txt = txt
		parts = txt.split()

		self.count = int(parts[0])
		self.hp = int(parts[4])
		self.atkArt = Damage.Slash
		self.atkDmg = int(parts[parts.index('damage')-2])
		self.initiative = int(parts[-1])

	def __repr__(self):
		return "%s\nNo: %d, hp: %d, atk: %d, init: %d" % (self.txt, self.count, self.hp, self.atkDmg, self.initiative)



class ImmuneSystem(Cells):
	def __init__(self, txt):
		Cells.__init__(self, txt)

class Infection(Cells):
	def __init__(self, txt):
		Cells.__init__(self, txt)

defence = [] # immune system
attack = [] # infection

immuneTurn = True;
for each in intro:
	print(each)

	if (re.match("^[0-9]+", each)):
		if immuneTurn:
			defence.append(ImmuneSystem(each))
		else:
			attack.append(Infection(each))
	elif (re.match("Infection", each)):
		immuneTurn = False


for e in defence:
	print(e)
