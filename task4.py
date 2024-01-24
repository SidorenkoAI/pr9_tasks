def PalindromeFilter(arg, minLength):
    return arg == arg[::-1] and len(arg) >= minLength