class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        G = arg[0]
        isGreater = True
        for i in arg:
            print(i, G)
            if i <= G and i != arg[0]:
                isGreater = False
                break
            else:
                G = i
        if isGreater:
            return True
        else:
            return False
k = task2()
print(k.greater([1,3,5,7]))