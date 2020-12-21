def dist_calc(idx, pos):
    if idx == 1:  # 북
        return pos
    elif idx == 2:  # 남
        return C + R + C - pos
    elif idx == 3:  # 서
        return C + R + C + R - pos
    else:  # 동
        return C + pos


C, R = map(int, input().split())
circumference= (C+R)*2

N = int(input())

dist = []
for i in range(N+1):
    idx, pos = map(int,input().split())
    dist.append(dist_calc(idx,pos))

my_dist = dist[-1]

ans = 0

for i in range(N):
    clockwise = abs(my_dist-dist[i])
    ans += min(clockwise,circumference-clockwise)
print(ans)
