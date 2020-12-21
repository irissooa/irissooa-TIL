'''
수빈이 N, 동생 K
수빈이 위치가 X, 걷는다면 1초후 X-1 or X+1, 순간이동 2*X
수빈이가 동생을 찾을 수 있는 가장 빠른 시간
최소시간이니까 BFS....?ㅠ 우째풀어.....하ㅏㅏ......ㅠ
'''
from collections import deque
def BFS(n):
    q = deque()
    q.append(n)
    while q:
        X = q.popleft()
        if X == K:
            return dist[K] -1
        a = X-1
        b = 2*X
        c = X+1
        if 0 <= a <100001 and dist[a] ==0:
            dist[a] = dist[X]+1
            q.append(a)
        if 0 <= b <100001 and dist[b] ==0:
            dist[b] = dist[X]+1
            q.append(b)
        if 0 <= c <100001 and dist[c] ==0:
            dist[c] = dist[X]+1
            q.append(c)

#답(다른사람꺼 내꺼랑 뭐가다를까)
def bfs():
    q = deque()
    q.append(N)
    while q:
        X = q.popleft()
        if X == K:
            print(dist[X])
            return
        for next in (X-1,X+1,X*2):
            if 0 <= next < MAX and not dist[next]:
                dist[next] = dist[X] + 1
                q.append(next)

N,K = map(int,input().split())
# N,K=5,17
MAX = 100001
dist = [0 for _ in range(MAX)]
dist[N] = 1
print(BFS(N))
# bfs()