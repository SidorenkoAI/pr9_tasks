class task1:
    def __init__(self):
        pass
    def giveEvenNumbers(self, arg):
        return list(filter(lambda x: x % 2 ==0, arg))
        '''
        :param arg: список целых чисел
        :return: список четных чисел
        '''
