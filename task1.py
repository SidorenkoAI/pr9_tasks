class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        r=[]
        for i in arg:
            if i%2==0:
                r.append(i)

        return r

a=task1
print(a.giveEvenNumbers(a, list(map(int, input().split()))))
