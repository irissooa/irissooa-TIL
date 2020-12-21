N = int(input())

pillar = [0] * 1001
max_H = 0
max_idx = 0
for _ in range(N):
    idx, height = map(int, input().split())
    pillar[idx] = height
    if max_H < height:
        max_H = height
        max_idx = idx

curr_H = 0
ans = 0
for i in range(max_idx + 1):
    if pillar[i] > curr_H:
        curr_H = pillar[i]
    ans += curr_H

curr_H = 0
for i in range(1000, max_idx, -1):
    if pillar[i] > curr_H:
        curr_H = pillar[i]
    ans += curr_H

print(ans)
