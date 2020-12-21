def fibo3(n):
    f = [0,1] #memo 테이블
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]
print(fibo3(1000))
#
# f = [0,1]
# for i in range(2, 7+1):
#     f.append(f[i-1]+f[i-2])
# print(f[7])