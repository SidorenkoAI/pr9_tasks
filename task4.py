def PalindromeFilter(arg, minLength):
    lst = []
    for i in arg:
        if i==i[::-1] and len(i)>=minLength:
            lst.append(i)
    return lst