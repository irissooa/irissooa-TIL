'''
22:15
청소기 방향 있음 동(우)서(좌)남(하)북(상)
지도 각 칸 (r(행),c(열))
1:벽 0:빈칸
로봇청소기 작동
1. 현재 위치 청소
2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색
2-1. 왼쪽 방향에 아직 청소하지 않은 곳 있으면 그 방향으로 회전, 한칸 전진, 1번 진행
2-2. 왼쪽 청소 공간 없으면 그방향 회전 후 2번
2-3. 네방향 모두 청소 돼있거나 벽, 바라보는 방향 유지, 한칸 후진, 2번 돌아감
2-4. 네방향 모두 청소, 벽, 뒤도 벽, 작동 멈춤

DFS(r,c,dir)로 돌리는데  (dir+3)%4의 순서로 본다! 상(0) -> 좌(3), 우(1) -> 상(0), 하(2)->우(1), 좌(3)->하(2)
현재 방향에 아직 청소하지 않은 곳이 있으면 (dir+3)%4로 방향전환, 1칸 가고, 그 방향의 또 (dir+3)%4로 이동(갈수있다면)
청소할 공간 없다! -> (dir+3)%4회전 후 다시 (dir+3)%4로 넘어감!
네방향 모두 청소할 공간이 없다! 현재 방향에서 뒤로 한칸! (dir+2)%4로 방향 전환!
네방향 모두 청소, 벽, 뒤도 벽, 작동 멈춤
'''
import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

di = [-1,0,1,0]#상우하좌
dj = [0,1,0,-1]
def DFS(i,j,dir,cnt):
    visited[i][j] = True

    if cnt == 4:
        d = (dir+2)%4
        ni = i + di[d]
        nj = j + dj[d]
        if arr[ni][nj]:
            return
        else:
            DFS(ni, nj, dir,0)
    else:
        d = (dir + 3)%4
        ni = i + di[d]
        nj = j + dj[d]
        if arr[ni][nj] == 0 and not visited[ni][nj]:
            DFS(ni,nj,d,0)
        else:
            DFS(i,j,d,cnt+1)



#세로,가로
N,M = map(int,input().split())
#r,c좌표, 바라보는 방향 0:북(상), 1:동(우),2:남(하),3:서(좌)
r,c,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# print(r,c,d)
# for x in arr:
#     print(x)
visited = [[False for j in range(M)] for i in range(N)]
DFS(r,c,d,0)
ans = 0
# for x in visited:
#     print(x)
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            ans +=1
print(ans)