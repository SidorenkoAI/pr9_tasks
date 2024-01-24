def PalindromeFilter(arg,minLength):

    a = []

    for i in arg:
        if i==i[::-1] and len(i)>=minLength:
            a.append(i)

    return a