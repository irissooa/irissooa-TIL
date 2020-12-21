'''
시작,끝,구간길이를 입력받고 인접리스트에 시작idx리스트에 (끝점, 구간길이)를 담아줌
BFS돌리는데 구간길이를 dist에 담아줌!
만약 dist 다음 점이 현재점에서 구간길이를 더한값보다 작다면 갱신!
'''
import sys
sys.stdin = open('input.txt','r')
from collections import deque

#BFS로 풀기
def BFS(node):
    q = deque()
    q.append(node)
    dist[node] = 0
    while q:
        p = q.popleft()
        if p == N:
            continue
        for n in range(len(linked[p])):
            next, length = linked[p][n]
            if dist[next] != -1 and dist[next] < dist[p] + length:
                continue
            dist[next] = dist[p] + length
            q.append(next)

#다익스트라로 풀기

T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())
    linked = [[] for i in range(N+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        linked[s].append([e,w])
    # for x in range(N+1):
        # print(x,linked[x])
    dist = [-1 for _ in range(N+1)]
    BFS(0)
    print('#{} {}'.format(tc,dist[N]))