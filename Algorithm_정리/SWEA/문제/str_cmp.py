def strcmp(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        i = 0 #초기값(초기식)
        while i < len(s1) and i < len(s2): #조건식
            if s1[i] != s2[i]:
                return False
            i += 1 #증감식
    return True

a = 'abc'
b = 'abc'
print(strcmp(a,b)) #True, False 받을예정