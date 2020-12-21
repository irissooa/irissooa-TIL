'''
출발지에서 도착지까지 가는 bfs만듦
도로가 파여진 깊이에 비례해서 복구시간 증가
가장짧은 경로!

'''
import sys
sys.stdin = open('input.txt','r')
from collections import deque

di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]
def BFS(i,j):
    q = deque()
    q.append([i,j])
    times[i][j] = 0
    while q:
        pi,pj = q.popleft()
        # print(pi,pj)
        if pi == N-1 and pj == N-1:
            continue
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            #  <= 에 '='을 붙이고 안붙이고 시간차이가 엄청 난당...
            if times[ni][nj] != -1 and times[ni][nj] <= times[pi][pj] + int(arr[ni][nj]):
                continue
            # print(int(arr[ni][nj]))
            times[ni][nj] = times[pi][pj] + int(arr[ni][nj])
            q.append([ni,nj])


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # for x in range(N):
    #     print(arr[x])
    times = [[-1 for j in range(N)] for i in range(N)]
    BFS(0,0)
    # print(times)
    print('#{} {}'.format(tc,times[N-1][N-1]))