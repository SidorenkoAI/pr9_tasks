class task2:
    def __init__(self):
        pass

    def greater(self, arg):
        a = arg[0]
        good = True
        for i in arg:
            print(i, a)
            if i <= a and i != arg[0]:
                good = False
                break
            else:
                a = i
        if good:
            return True
        else:
            return False