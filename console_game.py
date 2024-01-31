from random import randint

class Person:
    def __init__(self):
        self.id = id(self)


class Hero(Person):
    level = 0
    soldiers = list()
    def levelUp(self):
        self.level += 1    


class Soldier(Person):
    hero = None
    def goToHero(self, hero: Hero):
        self.hero = hero
        hero.soldiers.append(self)


hero1, hero2 = Hero(), Hero()
team1, team2 = list(), list()

for i in range(500):
    s = Soldier()
    if bool(randint(0, 1)):
        team1.append(s)
    else:
        team2.append(s)

print('Team 1 len is', len(team1))
print('Team 2 len is', len(team2))

if len(team1) > len(team2):
    hero1.levelUp()
    print('Level Up! (hero1)')
else:
    hero2.levelUp()
    print('Level Up! (hero2)')