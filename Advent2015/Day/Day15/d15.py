"""--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe.
All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients.
You make a list of the remaining ingredients you could use
to finish the recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)
You can only measure ingredients in whole-teaspoon amounts accurately,
and you have to be accurate so you can reproduce your results in the future.
The total score of a cookie can be found by adding up each of the properties
(negative totals become 0) and then multiplying together everything except
calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon
(because the amounts of each ingredient must add up to 100)
would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76
Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now)
results in a total score of 62842880,
which happens to be the best score possible given these ingredients.
If any properties had produced a negative total,
it would have instead become zero,
causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties,
what is the total score of the highest-scoring cookie you can make?"""

raw= """Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8""".split('\n')

#S: c 2, d  0, f -2, t  0, c 3
#B: c 0, d  5, f -3, t  0, c 3
#C: c 0, d  0, f  5, t -1, c 8
#A: c 0, d -1, f  0, t  5, c 8""".split('\n')
tab = [ [2, 0, -2, 0, 3],
        [0, 5, -3, 0, 3],
        [0, 0,  5,-1, 8],
        [0,-1,  0, 5, 8] ]



tot = 101
maxScore = 0
max500 = 0
for i in range(tot):
    print(i)
    for j in range(tot - i):
        for k in range(tot - i - j):
            l = 100 - i - j - k
            cap = i*tab[0][0] + j*tab[1][0] + k*tab[2][0] + l*tab[3][0]
            dur = i*tab[0][1] + j*tab[1][1] + k*tab[2][1] + l*tab[3][1]
            fla = i*tab[0][2] + j*tab[1][2] + k*tab[2][2] + l*tab[3][2]
            tex = i*tab[0][3] + j*tab[1][3] + k*tab[2][3] + l*tab[3][3]

            cal = i*tab[0][4] + j*tab[1][4] + k*tab[2][4] + l*tab[3][4]

            if cap < 0 or dur < 0 or fla < 0 or tex < 0 :
                continue

            score = cap * dur * fla * tex
            if score > maxScore:
                print(str(i) + " " + str(j) + " " + str(k) + " " + str(l))
                maxScore = score
            if cal == 500:
                if score > max500:
                    max500 = score

print(maxScore)
print(max500)


""" --- Part Two ---
Your cookie recipe becomes wildly popular!
Someone asks if you can make another recipe that has exactly 500 calories per cookie
(so they can use it as a meal replacement).
Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above,
if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon
(which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500.
The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring
cookie you can make with a calorie total of 500?

Although it hasn't changed, you can still get your puzzle input."""
class Ingredient:
    def __init__(self, capacity, durability, flavor, texture, calories):
        self.cap = capacity
        self.dur = durability
        self.fla = flavor
        self.tex = texture
        self.cal = calories
    
