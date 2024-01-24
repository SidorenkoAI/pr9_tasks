import math
class Drob:
    '''
    7. Реализовать перегрузку опреаторов +, -, *, /, чтобы можно было работать с дробями
    естественным образом:
    a = Drob(1,2)
    b = Drob(5,6)
    c = Drob()
    c = a + b
    8. Со списком дробей должны работать стандартный метод сортировки, функция max():
    lst = [Drob(1,3), Drob(4,1), Drob(6,4)]
    lst.sort()
    print(max(lst))
    '''
    def nod(self,n,d):
        return math.gcd(n,d)

    def __init__(self,n=0,d=1):
        if d == 0:
            raise TypeError ("Знаменатель не может быть равен 0!")
        self.n = int(n / self.nod(n,d))
        self.d = int(d / self.nod(n, d))
        if self.d<0:
            self.d = int(d / self.nod(n, d))*-1
        elif self.n==0:
            self.n=0
            self.d=1
    def __add__(self, other):
        p = self.n * other.d + self.d * other.n
        q = self.d * other.d
        return Drob(p, q)

    def __str__(self):
        return f'{self.n}/{self.d}'
    def __repr__(self):
        return str(self)
print(Drob(1,3)+Drob(1,3))
