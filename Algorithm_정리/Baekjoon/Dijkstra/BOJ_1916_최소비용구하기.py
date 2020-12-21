import sys
sys.stdin = open('input.txt', 'r')
import heapq

def dijkstra(st):
    dist = [987654321]*(N+1)
    heap = []
    dist[st] = 0
    heapq.heappush(heap,(dist[st],start_city))
    while heap:
        w,v = heapq.heappop(heap)
        if dist[v] < w:
            continue
        for nw,nv in adj[v]:
            nw += w
            if nw < dist[nv]:
                dist[nv] = nw
                heapq.heappush(heap,(nw,nv))
    return dist[end_city]
# input = sys.stdin.readline
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    start,end,cost = map(int,sys.stdin.readline().split())
    adj[start].append([cost,end])
start_city,end_city = map(int,sys.stdin.readline().split())
# print(adj)
# print(start_city,end_city)
print(dijkstra(start_city))
# print(dist)