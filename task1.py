class task1:
    def __init__(self, numbers):
        self.numbers = numbers

    def giveEvenNumbers(self):
        even_numbers = []
        for number in self.numbers:
            if number % 2 == 0:
                even_numbers.append(number)
        return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = task1(numbers)
result = even_numbers.giveEvenNumbers()
print(result)


