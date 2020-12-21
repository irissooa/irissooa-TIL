K = int(input())

pos = []
for i in range(6):
    dir, length = map(int, input().split())
    pos.append(length)

big = 0
small = 0
for i in range(6):
    tmp = pos[i] * pos[(i + 1) % 6]
    if big < tmp:
        big = tmp
        idx = i
small = pos[(idx + 3) % 6] * pos[(idx + 4) % 6]
print(K * (big - small))
