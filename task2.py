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
        return f'Монотонное возрастание чисел: {k}'
spis=task2()
spis2=list(map(int,input().split()))
print(spis.greater(spis2))