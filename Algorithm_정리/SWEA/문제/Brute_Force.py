def brute(t,p):
    i,j = 0,0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i+j
            j += 1
        if j == len(p):
            return i - len(p)
        else:
            return -1 #못찾았다는 뜻

text = 'TTTTAACCA'
pattern = 'TTA'
print(brute(text,pattern))

# find쓰면 한방에 끝남
print(text.find(pattern))

str1 = 'A pattern matching algorithm'
str2 = 'rithm'

def BruteForce(str1,str2):
    A = len(str1)
    B = len(str2)

    for i in range(A-B+1): #A안에 B찾기(index설정)
        cnt = 0
        for j in range(B):
            if str1[i+j] == str2[j]:
                cnt += 1
            else:
                break
        if cnt == B:
            print('여기부터 일치',i)
            return i
    return -1
tmp = BruteForce(str1,str2)
print(tmp)