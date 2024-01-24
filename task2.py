class task2:
    def __init__(self):
        pass
    def greater(self, arg):
        a=arg[0]
        arg.pop(0)
        for i in arg:
            if i<=a:
                return False
                break
            a=i
        return True

