'''
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
부모와 자식 사이 1촌
주어진사람들 촌수 구하기
#1. parent idx list에 child를 append(양방향으로!!)
#2. BFS(s)를 한뒤 구하고자하는 e까지 bfs돌리고 dist+=1추가해서 몇촌인지 구하기
'''
from collections import deque
def BFS(start):
    R.append(start)
    while R:
        ps = R.popleft()
        if ps == e:
            return
        for pe in family[ps]:
            if dist[pe]:
                continue
            dist[pe] = dist[ps] + 1
            R.append(pe)

#전체 사람 수
n = int(input())
#촌수 계싼해야되는 두 사람의 번호
s,e = map(int,input().split())
#부모 자식들 간의 관계의 개수
m = int(input())
family = [[0]*(n+1) for _ in range(n+1)]
dist = [0]*(n+1)
R = deque()
for _ in range(m):
    parent, child = map(int,input().split())
    family[parent].append(child)
    family[child].append(parent)
BFS(s)
if dist[e]:
    print(dist[e])
else:
    print(-1)