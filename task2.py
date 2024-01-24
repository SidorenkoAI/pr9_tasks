class task2:
    def __init__(self):
        pass

    def greater(self, arg: list):
        arg2 = arg.copy()
        arg3 = list(set(arg.copy()))
        arg2.sort()

        return arg == arg2 == arg3