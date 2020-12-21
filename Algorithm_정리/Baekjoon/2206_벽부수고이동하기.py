'''
NxM 행렬 0이동할수 있는곳, 1은 이동할 수 없는 벽
(1,1)->(N,M)으로 이동
최단경로-> BFS
딱 1번 벽을 부수고 이동했을 때 경로가 더 짧아진다면 1개까지만 부술 수 잇음
불가능 -1 출력
'''
from collections import deque
import sys
di = [0,0,1,-1] #우좌하상
dj = [1,-1,0,0]

def BFS(i,j):
    q = deque()
    q.append((i,j))
    dist[i][j] = 1
    while q:
        pi,pj = q.popleft()
        if pi == N and pj == M:
            return dist[pi][pj]
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if arr[ni][nj] != 0:
                continue
            if dist[ni][nj] != 0:
                continue
            dist[ni][nj] = dist[pi][pj] + 1
            q.append((ni,nj))
    return -1
N,M = map(int,sys.stdin.readline().split())
temp = [list(sys.stdin.readline()) for _ in range(N)]
arr = [[0 for j in range(M+2)] for i in range(N+2)]
for i in range(N):
    for j in range(M):
        arr[i][j] = int(temp[i][j])
print(arr)
dist = [[0 for j in range(M+2)] for i in range(N+2)]
print(BFS(1,1))
