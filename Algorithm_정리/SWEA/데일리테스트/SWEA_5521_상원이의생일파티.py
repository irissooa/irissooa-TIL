'''
친구관계 리스트를 양방향으로 인접리스트에 담아줌
dist를 써서 bfs, 거리가 2이내인 개수 세주기
'''
import sys
sys.stdin = open('input.txt','r')

def BFS(v):
    q = [v]
    while q:
        p = q.pop(0)
        for n in friends[p]:
            if dist[n]:
                continue
            dist[n] = dist[p]+1
            q.append(n)

T = int(input())
for tc in range(1,T+1):
    #N은 상원이 반 친구들, M은 친한관계수
    N,M = map(int,input().split())
    friends = [[] for i in range(N+1)]
    for m in range(M):
        #a와 b는 친한관계
        a,b = map(int,input().split())
        friends[a].append(b)
        friends[b].append(a)
    # print(friends)
    dist = [0 for i in range(N+1)]
    BFS(1)
    # print(dist)
    cnt = 0
    for d in range(2,N+1):
        if 0 < dist[d] <= 2:
            cnt+=1
    print('#{} {}'.format(tc,cnt))