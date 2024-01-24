class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        G = arg[0]
        isGreater = True
        for i in arg:
            if i < G:
                isGreater = False
                break
            else:
                G = i
        if isGreater:
            return True
        else:
            return False
