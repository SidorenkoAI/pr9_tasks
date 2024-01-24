class drob:
    def __init__(self, n = 0, d = 1):
        if d == 0:
            raise TypeError ("Знаменатель не может быть равен 0!")
        self.nom = int(n / self.nod(n,d))
        self.denom = int(d / self.nod(n,d))

    def __str__(self):
        return f"{self.nom} / {self.denom}"

    def __add__(self, other):
        n = self.nom * other.denom + self.denom * other.nom
        d = self.denom * other.denom
        return drob(n, d)

    def __sub__(self, other):
        if self.denom == other.denom:
            result_numerator = self.nom - other.nom
            result_denominator = self.denom
        else:
            result_numerator = (self.nom * other.denom) - (other.nom * self.denom)
            result_denominator = self.denom * other.denom

        return drob(result_numerator, result_denominator)

    def __mul__(self, other):
        result_numerator = self.nom * other.nom
        result_denominator = self.denom * other.denom
        return drob(result_numerator, result_denominator)

    def __truediv__(self, other):
        result_denominator = self.nom * other.denom
        result_numerator = self.denom * other.nom
        return drob(result_numerator, result_denominator)

    def __lt__(self, other):
        common_denom = self.nod(self.denom, other.denom)
        self_numerator = self.nom * (common_denom // self.denom)
        other_numerator = other.nom * (common_denom // other.denom)
        return self_numerator < other_numerator

    def __repr__(self):
        return str(self)

    def nod(self, a, b):
        if b == 0:
            return a
        else:
             return self.nod(b, a % b)

c = drob(1, 0)
print(c)


