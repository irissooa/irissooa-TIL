'''
가로세로 크기 100도화지
종이 둘레 길이 구하기
색종이를 1로 전부 만들고
상하좌우 dfs돌리면서 범위 벗어나고, 0인것 개수 구하기
'''
import sys
sys.setrecursionlimit(10**8)
#상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]
def dfs(i,j):
    global ans
    visited[i][j] = True
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= 100 or nj <0 or nj >= 100:
            ans+=1
            continue
        if visited[ni][nj]:
            continue
        if not arr[ni][nj]:
            ans+=1
            continue
        dfs(ni,nj)

N = int(input())
arr = [[0 for j in range(100)] for i in range(100)]
visited = [[False for j in range(100)] for i in range(100)]
ans = 0
for n in range(N):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1
for i in range(100):
    for j in range(100):
        if arr[i][j] and not visited[i][j]:
            dfs(i,j)
print(ans)