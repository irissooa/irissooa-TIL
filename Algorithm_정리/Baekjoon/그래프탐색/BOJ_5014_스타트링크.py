'''
2020-12-09 23:40-
F층으로 이루어진 건물, G층으로 가야됨, 강호가 있는 곳은 S층
엘베 버튼 2개밖에 없음 U버튼은 위로 U층을 가는 버튼, D버튼은 밑으로 D층을 가는 버튼, 갔는데 해당 층이 없으면 엘베 안움직임
G층에 도착하려면 최소 몇번 버튼 눌러야 되나
갈수없다면 use the stairs출력

1. F까지의 1차원 dist배열을 만듦
2. S에서 +U만큼, -D만큼 보냄
3. 거기서 범위체크 계속하며 dist최소값 갱신, dist[G-1]-1을 뽑는다 없다면  use the stairs출력
'''
import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque


def BFS(node):
    q = deque()
    q.append(node)
    dist[node] = 1
    while q:
        p = q.popleft()
        if p == G:
            return
        for n in [U,-D]:
            next = p + n
            # print(next,p,n)
            if next <= 0 or next > F:
                continue
            # if dist[next] and dist[next] < dist[p] + 1:
            #     continue
            if dist[next]:
                continue
            dist[next] = dist[p] + 1
            if next == G:
                return
            q.append(next)


if __name__ == '__main__':
    # 가장높은층 F, 강호위치S층, G층이목표, U위로 올라감,D아래로 내려감
    F,S,G,U,D = map(int,input().split())
    dist = [0 for _ in range(F+1)]
    # BFS(S)
    q = deque()
    q.append(S)
    dist[S] = 1
    while q:
        p = q.popleft()
        if p == G:
            break
        for n in [U, -D]:
            next = p + n
            # print(next,p,n)
            if next <= 0 or next > F:
                continue
            # if dist[next] and dist[next] < dist[p] + 1:
            #     continue
            if dist[next]:
                continue
            dist[next] = dist[p] + 1
            q.append(next)
    ans = dist[G]-1
    if S == G:
        print(0)
    elif ans >0:
        print(ans)
    else:
        print('use the stairs')
    # print(dist)