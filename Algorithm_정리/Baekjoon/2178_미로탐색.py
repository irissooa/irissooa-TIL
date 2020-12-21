'''
미로는 1은 이동가능 0은 불가
(1,1)에서 출발->(N,M)의 위치로 이동할 때 지나야하는 최소의 칸수?
행,열 제일 앞에 0으로 채워서 인덱스 맞춰줌
서로 인접한 칸으로만 이동가능
최소의 칸수니까 BFS로 해야되지 않을까?->아몰라!!!!!DFS로 해본다....후
'''
di = [1,-1,0,0] #우좌하상
dj = [0,0,1,-1]
def DFS(i,j,dist):
    visited[i][j] = True
    dist += 1

    if i == N and j == M:
        print(dist)
        return dist
    else:
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if ni <= 0 or ni >= N+1 or nj <= 0 or nj >= M+1:
                continue
            if arr[ni][nj] == 0:
                continue
            if visited[ni][nj] == True:
                continue
            DFS(ni,nj,dist)
def BFS(i,j):
    q=[[i,j]]
    while q:
        top = q.pop(0)
        pi,pj = top[0],top[1]
        if pi == N and pj == M:
            return dist[pi][pj] +1
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if arr[ni][nj] == 0:
                continue
            if dist[ni][nj] != 0:
                continue
            dist[ni][nj] = dist[pi][pj] + 1
            q.append([ni,nj])
    return -1


N,M = map(int,input().split())
temp=[list(input()) for _ in range(N)]
arr = [[0 for j in range(M+2)] for i in range(N+2)]
for i in range(1,N+1):
    for j in range(1,M+1):
        arr[i][j] = int(temp[i-1][j-1])
# from pprint import pprint
# pprint(arr)
visited = [[False for j in range(M+1)] for i in range(N+1)]
dist = [[0 for j in range(M+1)] for i in range(N+1)]
# DFS(1,1,0)
print(BFS(1,1))
