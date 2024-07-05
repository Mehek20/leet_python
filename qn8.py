def myAtoi(s):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    i = 0
    n = len(s)

    while i < n and (s[i] == ' '):
        i += 1
    
    sign = 1
    if i<n and (s[i] == '-' or s[i] == '+'):
        if(s[i] == '-'):
            sign = -1
        i += 1

    num = 0
    while i < n and s[i].isdigit():
        num = num * 10 + (ord(s[i])-ord('0'))
        i += 1
    num *= sign

    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num




    