def MoveStrings(s, d):
    for i in s:
        d.append(i)
    for i in range(len(s)):
        s.pop(0)