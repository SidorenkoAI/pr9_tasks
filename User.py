import itertools
class User:
    userId = itertools.count()
    def __init__(self):
        self.id = next(User.userId)
        self.balance = 0
    def __str__(self):
        return f'User ID: {self.id}. Balance: {self.balance} rub.'
    def __gt__(self, other):
        return self.balance>other.balance
    def addMoney(self, nom, count):
        self.balance+=(nom*count)
# class Admin: