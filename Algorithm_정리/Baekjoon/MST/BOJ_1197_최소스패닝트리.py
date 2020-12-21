'''
MST
크루스칼, 프림 이용해서 풀기
'''
import sys
sys.stdin = open('input.txt','r')
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def prim_heapq():
    visited = [False] *(V+1)
    heap = []
    heapq.heappush(heap,[0,1])
    ans = 0
    while heap:
        w,v = heapq.heappop(heap)
        if not visited[v]:
            ans += w
            visited[v] = True

            for weight, idx in adj[v]:
                if not visited[idx]:
                    heapq.heappush(heap,[weight,idx])
    return ans

##kruskal
# def make_set(x):
#     p[x] = x
#
def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    if find_set(x) != find_set(y):
        p[find_set(y)] = find_set(x)

def kruskal(graph):
    graph = sorted(graph,key = lambda x : x[2])
    # for i in range(V+1):
    #     make_set(i)
    ans = 0
#처음한개가 이미 연결돼있어서 1부터 시작
    cnt = 1
    idx = 0
    while cnt < V:
        x = graph[idx][0]
        y = graph[idx][1]
        if find_set(x) != find_set(y):
            union(x,y)
            cnt += 1
            ans += graph[idx][2]
        idx+=1
        # print('idx',idx)
    return ans



V,E = map(int,input().split())
adj = [[] for _ in range(V+1)]
edges = []
#make_set과정 포함하면 p만듦
p = [x for x in range(V+1)]
# print(p)
for _ in range(E):
    u,v,w = map(int,input().split())
    adj[u].append([w,v])
    adj[v].append([w,u])
    edges.append([u,v,w])
# print(edges)
primHeap = prim_heapq()
# kruskalans = kruskal(edges)
print(primHeap)
# print(kruskalans)
