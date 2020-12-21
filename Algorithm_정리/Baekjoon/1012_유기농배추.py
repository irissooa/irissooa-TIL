'''
배추1가 있는 뭉텅이에 배추흰지렁이 1마리 필요!
dfs, 델타 방문이용해서 몇 뭉텅이가 있는지!확인(상하좌우) => 런타임에러
bfs로 풀어보자....
'''

di = [1,-1,0,0] #우좌하상
dj = [0,0,1,-1]
def DFS(i,j):
    visited[i][j] = True

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue
        if arr[ni][nj] == 0:
            continue
        if visited[ni][nj] == True:
            continue
        DFS(ni,nj)

def BFS(i,j):
    q = []
    q.append([i,j])
    while q:
        top = q.pop(0)
        pi,pj = top[0],top[1]
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if arr[ni][nj] == 0:
                continue
            if dist[ni][nj] != 0:
                continue
            dist[ni][nj] = dist[pi][pj] + 1
            q.append([ni,nj])

T = int(input())
for tc in range(1,T+1):
    #배추밭 가로M, 세로,N, 배추 심어진 위치 개수K
    M,N,K = map(int,input().split())
    arr = [[0]*(M) for _ in range(N)]
    for i in range(K):
        #x가 열 y가 행
        x,y = map(int,input().split())
        arr[y][x] = 1
    # from pprint import pprint
    # pprint(arr)
    visited = [[False for j in range(M)] for i in range(N)]
    dist = [[0 for j in range(M)] for i in range(N)]
    num = 0
    for i in range(N):
        for j in range(M):
            # if arr[i][j] == 1 and visited[i][j] == False:
            if arr[i][j] == 1 and dist[i][j] == 0:
                # print('i',i,'j',j)
                num += 1
                # DFS(i,j)
                BFS(i,j)
    print(num)
