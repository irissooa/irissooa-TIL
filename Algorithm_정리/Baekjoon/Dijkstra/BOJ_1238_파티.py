import sys, heapq
sys.stdin = open('input.txt','r')

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    dist = [INF]*(N+1)
    heap = []
    dist[start] = 0
    heapq.heappush(heap,[dist[start],start])
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




N,M,X = map(int,input().split())
adj = [dict() for _ in range(N+1)]
for _ in range(M):
    #i번째 도로의 시작점, 끝점,소요시간
    u,v,t = map(int,input().split())
    if v in adj[u]:
        adj[u][v] = min(adj[u][v],t)
    else:
        adj[u][v] = t
# print(adj)
MAX = -INF
for s in range(1,N+1):
    ans = dijkstra(s)[X]
    back = dijkstra(X)[s]
    if MAX < ans+back:
        MAX = ans+back
print(MAX)