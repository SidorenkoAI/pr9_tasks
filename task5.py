def MoveStrings(s, d):
    for i in s:
        for j in d:
            j+=i
    s.clear()
    return s, d

