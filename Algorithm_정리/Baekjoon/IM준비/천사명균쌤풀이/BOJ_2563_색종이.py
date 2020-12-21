N = int(input())

paper = [[0] * 102 for _ in range(102)]

for i in range(N):
    r, c = map(int, input().split())
    for j in range(r, r + 10):
        for k in range(c, c + 10):
            paper[j][k] = 1

ans = 0
for i in range(102):
    ans += paper[i].count(1)
print(ans)
