import itertools
class user():
    userID = itertools.count()

    def __init__(self):
        self.balance = 0
        self.id = next(user.userID)

    def __str__(self):
        return f"user{self.id}: {self.balance}rub"

    def __repr__(self):
        return self.__str__()

    def __gt__(self, other):
        return self.balance > other.balance

    def addMoney(self, cash):
        self.balance += cash