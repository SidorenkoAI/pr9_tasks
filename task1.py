class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        lst=[]
        for i in arg:
            if i%2==0:
                lst.append(i)
        return lst


