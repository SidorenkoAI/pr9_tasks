def PalindromeFilter(arg, minLength):
    res = list()
    for i in arg:
        if arg == arg[::-1] and len(arg) >= minLength:
            res.append(i)
    return res
