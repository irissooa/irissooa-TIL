'''
 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토
 토마토 익은거 1 안익은거 0 없는거 -1
 최소 일수 ->BFS
'''
from collections import deque
import sys
dh = [1,-1,0,0,0,0] #위,아래,왼쪽,오른쪽,앞,뒤
di = [0,0,0,0,-1,1]
dj = [0,0,-1,1,0,0]

def BFS(q):
    while q:
        top = q.popleft()
        ph,pi,pj = top[0],top[1],top[2]
        for d in range(6):
            nh = ph + dh[d]
            ni = pi +di[d]
            nj = pj + dj[d]
            if nh < 0 or nh >= H or ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if arr[nh][ni][nj] != 0:
                continue
            if dist[nh][ni][nj] != 0:
                continue
            q.append([nh,ni,nj])
            dist[nh][ni][nj] = dist[ph][pi][pj] +1
#가로 M 세로 N 높이 H
M,N,H = map(int,sys.stdin.readline().split())
#가장 밑의 상자부터 가장 위의 상자까지 저장된 토마토 정보 주어짐
#N개의 줄이 H번 반복
arr = [[list(map(int,sys.stdin.readline().split())) for i in range(N)] for h in range(H)]
# print(arr)
dist=[[[0 for j in range(M)] for i in range(N)] for h in range(H)]
ripen = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                ripen.append([h,i,j])
# print(ripen)
BFS(ripen)
#만약 dist가 방문 안했는데 arr이 0이면 -1을 뽑고, 아니라면 max를 뽑아라
flag = False
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 0 and dist[h][i][j] == 0:
                flag = True
    # print(max(dist))
if flag:
    print(-1)
else:
    MAX = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if MAX < dist[h][i][j]:
                    MAX = dist[h][i][j]
    print(MAX)
