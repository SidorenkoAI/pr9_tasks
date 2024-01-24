def MoveStrings(s, d):
    for i in s:
        for j in d:
            j+=i
            s.pop(0)
    return s, d

