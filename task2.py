class task2:
    def __init__(self):
        pass
    k=False
    def greater(self, arg):
        for i in range(1,len(arg)):
            if arg[i-1]<arg[i]:
                k=True
            else:
                k=False
        return k