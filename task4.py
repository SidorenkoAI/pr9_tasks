def PalindromeFilter(arg, minLength):
    ans=[]
    for i in arg:
        if i==i[::-1] and len(i)>=minLength:
            ans.append(i)
    return ans