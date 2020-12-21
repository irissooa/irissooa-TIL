import sys
input = sys.stdin.readline
from collections import deque

di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def BFS(i,j):
    q = deque()
    q.append([i,j])
    visited.add((i,j))
    while q:
        pi,pj = q.popleft()
        zero = 0
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if (ni,nj) in visited:
                continue
            if not arr[ni][nj]:
                zero+=1
                continue
            visited.add((ni,nj))
            q.append([ni,nj])
        change.append([pi,pj,zero])

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
year = 0
change = deque()
ice = deque()
for i in range(1,N-1):
    for j in range(1,M-1):
        if arr[i][j]:
            ice.append((i,j))
while True:
    cnt = 0
    # temp = [[0 for j in range(M)] for i in range(N)]
    visited = set()
    while ice:
        i = ice.popleft()
        if i not in visited:
            cnt += 1
            BFS(i[0],i[1])
    if cnt >=2:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
    year += 1
    ice =deque()
    while change:
        i,j,zero = change.popleft()
        arr[i][j] -= zero
        if arr[i][j] <=0:
            arr[i][j] = 0
        else:
            ice.append((i,j))
    # for x in arr:
    #     print(x)