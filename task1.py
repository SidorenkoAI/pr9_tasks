class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        spis=[]
        for i in arg:
            if i%2==0:
                spis.append(i)
        return f'Четные числа из списка: {spis}'