'''
2020-12-09 19:30-19:50
지역의 높이를 파악하고, 물에 잠기지 않는 안전한 영역이 몇개인지 조사
위아래 오른쪽 왼쪽으로 인접해있는 안전영역 뭉치 개수가 최대가 되는 값

상하좌우 dfs돌면서 뭉치의 개수 최대치 구하기
배열을 받을 때 높이 최소, 최대값 기록해두기
1. 높이 H(최소부터 시작) for문 돌면서 배열값이 높이 H 초과인 것의 뭉치 개수를 델타이용해서 찾기
2. 개수 다 찾은 뒤 최대 갱신하고, H+1해서 다시 찾기
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
INF = sys.maxsize
sys.setrecursionlimit(10**8)

di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def DFS(i,j):
    visited[i][j] = True
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if visited[ni][nj]:
            continue
        if arr[ni][nj] <=H:
            continue
        DFS(ni,nj)


N = int(input())
arr = []
maxnum,minnum=-INF,INF
for _ in range(N):
    temp = list(map(int,input().split()))
    if max(temp) > maxnum:
        maxnum = max(temp)
    if min(temp) < minnum:
        minnum = min(temp)
    arr.append(temp)
# for x in arr:
#     print(x)
# print(maxnum,minnum)

MAX = 0
H=minnum-1
while H <= maxnum:
    visited = [[False for j in range(N)] for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > H and not visited[i][j]:
                cnt+=1
                DFS(i,j)
    if cnt > MAX:
        MAX = cnt
    H+=1
print(MAX)