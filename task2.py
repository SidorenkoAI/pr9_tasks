class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        G = arg[0]
        isGreater = False
        for i in arg:
            if i < G:
                isGreater = True
        if isGreater:
            return('Yes')
        else:
            return('No')
Item = task2()

