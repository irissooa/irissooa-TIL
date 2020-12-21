'''
노드를 인접리스트로 노드가 향하는 정점에 담는다
그리고 DFS로 루트 1부터 돌림!
'''
import sys
# sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**10)
def DFS(s):
    visited[s] = True
    for e in node[s]:
        if not visited[e]:
            child[s].append(e)
            parent[e] = s
            DFS(e)

#노드의 개수
N = int(input())
node = [[] for _ in range(N+1)]
child = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    s,e = map(int,input().split())
    node[s].append(e)
    node[e].append(s)
# print(node)
visited = [False for _ in range(N+1)]
DFS(1)
for p in range(2,N+1):
    print(parent[p])
# print(parent)