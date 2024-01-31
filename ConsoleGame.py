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
        return f"Герой ID {self.id} из команды {self.team}"
    def __repr__(self):
        return self.__str__()
    def LevelChange(self, num):
        self.level += num
        return self.level

class Solder:
    SolderID = itertools.count()

    def __init__(self, TeamNumber="0"):
        self.id = next(Solder.SolderID)
        self.team = TeamNumber
    def __str__(self):
        return f"Солдат ID {self.id} из команды {self.team}"
    def __repr__(self):
        return self.__str__()
    def follow_to_hero(self, hero: Hero):
        pass

def create_teams():
    team = int(input())
    team_data = {}
    Level_Lst = []
    while team:
        hero = Hero(str(team))
        solders = []
        for i in range(random.randint(2, 10)):
            solders.append(Solder(hero.team))
        team_data[hero] = solders
        Level_Lst.append(hero.LevelChange(len(solders)))
        team -= 1
    return team_data, Level_Lst

def menu():
    print("1: start game")
    print("0: exit")

def game_support():
    print("/OutputMaxLevelTeam")
    print("/StartGame")
    print("/FollowToHero --NumHero")

while True:
    try:
        menu()
        userInput = int(input())
        if userInput == 0:
            ValueError()
        elif userInput == 1:
            game_support()
            Action = input()
            if Action == "/OutputMaxLevelTeam":
                print("Максимальный уровень Героя: ", max(create_teams()[1]))
    except ValueError():
        break