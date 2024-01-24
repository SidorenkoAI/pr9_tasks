def PalindromeFilter(arg, minLength):
    res=[]
    for i in arg:
        if len(i)>=minLength and i.lower()==str(''.join(reversed(i))).lower():
            res.append(i)

    return res

