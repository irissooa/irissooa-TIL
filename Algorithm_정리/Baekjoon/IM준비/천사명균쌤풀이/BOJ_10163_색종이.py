N = int(input())

paper = [[0] * 101 for _ in range(101)]

num = 1

for _ in range(N):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            paper[i][j] = num

    num += 1

for i in range(1, N + 1):
    cnt = 0
    for r in range(101):
        cnt += paper[r].count(i)
    print(cnt)
