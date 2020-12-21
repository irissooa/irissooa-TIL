'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인
마지막 줄의 2에서 출발해서 0을 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,0,1,-1] #우좌하상
dj = [1,-1,0,0]
def DFS(i,j):
    global result
    visited[i][j] = True
    if maize[i][j] == 3:
        result = 1
        return result
    else:
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if maize[ni][nj] == 1:
                continue
            if visited[ni][nj] == True:
                continue
            DFS(ni,nj)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maize = [list(map(int,input())) for _ in range(N)]
    visited = [[False for j in range(N)] for i in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if maize[i][j] == 2:
                DFS(i,j)
    print('#{} {}'.format(tc,result))