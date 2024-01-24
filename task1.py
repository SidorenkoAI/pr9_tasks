class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        L = []
        for i in arg:
            if i % 2 == 0:
                L.append(i)
        return L
K = task1()
print(K.giveEvenNumbers([1,46,2,5,7,2,24]))

