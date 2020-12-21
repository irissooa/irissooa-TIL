import sys
sys.stdin = open('input.txt','r')
from collections import deque
di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def BFS(i,j):
    q = deque()
    q.append((i,j))
    dist[i][j] = 1
    while q:
        pi,pj = q.popleft()
        if dist[pi][pj] >= L:
            return
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if not tunnel[ni][nj]:
                continue
            if dist[ni][nj]:
                continue
            #우
            if d ==0 and (tunnel[pi][pj] not in [1,3,4,5] or tunnel[ni][nj] not in [1,3,6,7]):
                continue
            #하
            if d==1 and (tunnel[pi][pj] not in [1,2,5,6] or tunnel[ni][nj] not in [1,2,4,7]):
                continue
            #좌
            if d == 2 and (tunnel[pi][pj] not in [1,3,6,7] or tunnel[ni][nj] not in [1,3,4,5]):
                continue
            #상
            if d==3 and (tunnel[pi][pj] not in [1,2,4,7] or tunnel[ni][nj] not in [1,2,5,6]):
                continue
            dist[ni][nj] = dist[pi][pj] + 1
            q.append((ni,nj))



T = int(input())
for tc in range(1,T+1):
    #세로N, 가로M, 맨홀뚜껑 위치한 장소 세로위치R,가로위치,탈출후 소요된시간 L
    N,M,R,C,L = map(int,input().split())
    #N줄 터널 지도 정보 M개의 숫자
    tunnel = [list(map(int,input().split())) for _ in range(N)]
    dist = [[0 for j in range(M)] for i in range(N)]
    BFS(R,C)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < dist[i][j] <= L:
                cnt+=1
    # from pprint import pprint
    # print('소요시간',L)
    # pprint(tunnel)
    # print('처음위치',R,C)
    # pprint(dist)
    print('#{} {}'.format(tc,cnt))
