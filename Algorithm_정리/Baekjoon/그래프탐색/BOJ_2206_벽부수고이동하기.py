import sys
sys.stdin = open('input.txt','r')
from collections import deque
di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]
def BFS(i,j):
    global MIN
    q = deque()
    q.append([i,j])
    dist[i][j] = 1
    while q:
        pi,pj = q.popleft()
        if dist[pi][pj] > MIN:
            return
        if pi==N-1 and pj == M-1:
            return
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if dist[ni][nj]:
                continue
            if maze[ni][nj] == '1':
                continue

            dist[ni][nj] = dist[pi][pj] + 1
            q.append([ni,nj])



N,M = map(int,input().split())
maze = [list(input()) for _ in range(N)]
walls = []
for i in range(N):
    for j in range(M):
        if maze[i][j] == '1':
            walls.append([i,j])

MIN = 987654321
dist = [[0 for c in range(M)] for r in range(N)]
BFS(0,0)
for w in walls:
    dist = [[0 for c in range(M)] for r in range(N)]
    r,c = w
    maze[r][c] = '0'
    # print(r,c)
    BFS(0,0)
    maze[r][c] = '1'
    if dist[N-1][M-1] and MIN > dist[N-1][M-1]:
        MIN = dist[N-1][M-1]
    # for x in dist:
    #     print(x)


if MIN == 987654321:
    print(-1)
else:
    print(MIN)
    # for x in maze:
    #     print(x)
    # print('-----')