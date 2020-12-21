'''
소요시간 : 2020/10/25/10:05
방향없는 그래프 -> 인접리스트에 표시
첫째줄부터 연결 요소의 개수를 출력!
dfs하면 될듯
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
sys.setrecursionlimit(10**6)

#근데...런타임에러ㅠ하..bfs로도 해보자
def DFS(s):
    #방문했으니 방문표시
    visited[s] = True
    #인접리스트에 있고, 방문하지 않은 정점이라면
    for e in arr[s]:
        if not visited[e]:
            DFS(e)

def BFS(s):
    q=[s]
    while q:
        p = q.pop()
        for e in arr[p]:
            if not visited[e]:
                visited[e] = True
                q.append(e)


#정점의 개수N,간선의 개수M
N,M = map(int,sys.stdin.readline().split())
#인접리스트
arr = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    #간선의 양 끝점 u,v주어짐
    u,v = map(int,sys.stdin.readline().split())
    #무방향이니까 둘다 표시해줌
    arr[u].append(v)
    arr[v].append(u)
cnt = 0 #연결요소를 세어줌
for s in range(1,N+1):
    if not visited[s]:
        DFS(s)
        # BFS(s)
        cnt += 1
# pprint(arr)
print(cnt)