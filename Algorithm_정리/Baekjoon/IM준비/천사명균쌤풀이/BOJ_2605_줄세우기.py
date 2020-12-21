N = int(input())
choice = list(map(int, input().split()))
ans = []
num = 1
for i in range(N):
    idx = len(ans) - choice[i]
    ans.insert(idx, num)
    num += 1
print(*ans)
