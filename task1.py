class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        res = list()
        for i in arg:
            if i%2 == 0:
                res.append(i)
                
        return res