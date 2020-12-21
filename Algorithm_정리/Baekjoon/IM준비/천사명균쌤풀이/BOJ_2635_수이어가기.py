N = int(input())

ans = []
maxlen = 0
for i in range(N,-1,-1):
    tmp = [N]
    K = i
    while K >= 0:
        tmp.append(K)
        K = tmp[len(tmp)-2]-tmp[len(tmp)-1]
    if len(tmp) > maxlen:
        maxlen = len(tmp)
        ans = tmp[:]

print(len(ans))
print(*ans)