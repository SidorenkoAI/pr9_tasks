def MoveStrings(s, d):
    for i in s:
        d.append(i)
    s.clear()
    return s, d

print(MoveStrings(["s", "aa", "a", "1111"], ["d", "bb", "b"]))
