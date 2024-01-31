import itertools, random
'''
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее
уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У
солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа
"герой". У героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты.
Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран.
У героя, принадлежащего команде с более длинным списком, увеличивается уровень.
'''

class Hero:
    HeroID = itertools.count()
    def __init__(self, TeamNumber = "0"):
        self.id = next(Hero.HeroID)
        self.team = TeamNumber
        self.level = 0
    def __str__(self):
        return f"{self.id} {self.team}"
    def __repr__(self):
        return f"{self.id} {self.team}"
    def LevelChange(self):
        self.level += 1

class Solder:
    SolderID = itertools.count()

    def __init__(self, TeamNumber="0"):
        self.id = next(Solder.SolderID)
        self.team = TeamNumber
    def __str__(self):
        return f"Солдат ID {self.id} из команды {self.team}"
    def __repr__(self):
        return self.__str__()
    def follow_to_hero(self, hero = Hero()):
        pass

# a = [Hero('12'), Hero('13'), Hero('14')]
# print(a)
team = int(input())
team_lst = {}
while team:
    hero = Hero(str(team))
    team_lst[hero] = Solder(str(random.randint(2, 10)))
    team -= 1
print(list(team_lst.values()))
