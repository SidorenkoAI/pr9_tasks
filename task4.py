def PalindromeFilter(arg, minLength):
    Palindroms = []
    for i in arg:
        if len(i) >= minLength:
            if i == i[::-1]:
                Palindroms.append(i)
    return Palindroms