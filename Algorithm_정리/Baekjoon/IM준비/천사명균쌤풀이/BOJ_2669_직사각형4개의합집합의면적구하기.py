arr = [[0] * 102 for _ in range(102)]

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1
ans = 0
for i in range(102):
    ans += sum(arr[i])

print(ans)
