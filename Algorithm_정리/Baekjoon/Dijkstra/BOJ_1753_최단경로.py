import heapq
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
# def dijkstra(x):
#     dist = [[987654321,x] for _ in range(V+1)]
#     heap = []
#     #start 거리표시
#     dist[x] = [0,x]
#     heapq.heappush(heap,(dist[x][0],x))
#     while heap:
#         w,p = heapq.heappop(heap)
#         # print(current)
#         #현재값의 dist에 저장돼있는 값이 지금 거리보다 작다면 continue -> 시간줄이기위해
#         if dist[p][0] < w:
#             continue
#         #
#         for nw,nx in adj[p]:
#             nw += w
#             if nw < dist[nx][0]:
#                 dist[nx][0] = nw
#                 heapq.heappush(heap,[nw,nx])
#     return dist

def djs(start):
    dist = [INF for _ in range(V+1)]
    dist[start] = 0
    heap = [[dist[start],start]]
    while heap:
        w,v = heapq.heappop(heap)
        if dist[v] < w:
            continue
        for nv,nw in adj[v].items():
            nw += w
            if dist[nv] > nw:
                dist[nv] = nw
                heapq.heappush(heap,[nw,nv])
    return dist


#정점개수,간선개수
V,E = map(int,input().split())
#시작정점번호
start = int(input())
#u -> v , w가중치
#1부터 V까지
# adj = [[]*(V+1) for _ in range(V+1)]
adj = [dict() for _ in range(V+1)]
for _ in range(E):
    u,e,w = map(int,input().split())
    # adj[u].append([w,e])
    if e in adj[u]:
        adj[u][e] = min(w,adj[u][e])
    else:
        adj[u][e] = w

ans = djs(start)
# print(ans)
for i in range(1,V+1):
    if ans[i] < INF:
        print(ans[i])
    else:
        print('INF')


# ans = dijkstra(start)
# print(ans)
# for i in range(1,V+1):
#     if ans[i][0] != 987654321:
#         print(ans[i][0])
#     else:
#         print('INF')