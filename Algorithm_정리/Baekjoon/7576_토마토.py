'''
토마토 익는 것 최소 일수
BFS
익은 토마토 1 익지 않은 토마토 0 토마토가 없는 칸 -1
처음부터 토마토 모두 익어있으면 0
모두 익지 못하는 상황이면 -1
'''
from collections import deque
di = [1,-1,0,0]
dj = [0,0,1,-1]

def BFS(q):

    while q:
        top = q.popleft()
        pi,pj = top[0],top[1]
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
            q.append([ni,nj])

#M가로,N세로
M,N = map(int,input().split())
arr= [list(map(int,input().split())) for i in range(N)]
# print(arr)
ripen=deque()
dist = [[0 for j in range(M)] for i in range(N)]
# zero = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            ripen.append([i,j])
        # elif arr[i][j] == 0:
        #     zero += 1
# print(zero,ripen)
BFS(ripen)
#만약 dist가 방문 안했는데 arr이 0이면 -1을 뽑고, 아니라면 max를 뽑아라
flag = False
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and dist[i][j] == 0:
            flag = True
# print(max(dist))
if flag:
    print(-1)
else:
    MAX = 0
    for i in range(N):
        for j in range(M):
            if MAX < dist[i][j]:
                MAX = dist[i][j]
    print(MAX)
