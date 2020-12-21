import sys
sys.stdin=open('input.txt','r')
from pprint import pprint

'''
map을 입력받는다.
bfs를 돌리는데 넘어갈때 기본 1더해줌 높이가 높은곳으로 가면 그 차만큼 더 더해줌
dist에서 만약 값이 있다면 더 작은 값으로 갱신해줘야됨
'''
from collections import deque
di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]
def BFS(i,j):
    q = deque()
    q.append([i,j])
    dist[i][j] = 0
    while q:
        pi,pj = q.popleft()
        # 도착해도 다른경우가 더 짧을수있으니까.. continue
        if pi == N-1 and pj == N-1:
            continue
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            cost = arr[ni][nj] - arr[pi][pj]
            if cost < 0:
                cost = 0
            # 다음 값에 들어가 있는게 현재 값에서 비용과 1을 더한것(지금구하는값)보다 더 작은게 있으니까
            if dist[ni][nj] != -1 and dist[ni][nj] <= dist[pi][pj] + cost+1:
                continue
            dist[ni][nj] = dist[pi][pj] + cost + 1
            q.append([ni,nj])


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dist = [[-1 for j in range(N)] for i in range(N)]
    BFS(0,0)
    print('#{} {}'.format(tc,dist[N-1][N-1]))