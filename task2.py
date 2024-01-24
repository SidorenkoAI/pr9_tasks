class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        k = arg[0]
        isGreater = True
        for i in arg:
            print(i, k)
            if i <= k and i != arg[0]:
                isGreater = False
                break
            else:
                k = i
        if isGreater:
            return True
        else:
            return False