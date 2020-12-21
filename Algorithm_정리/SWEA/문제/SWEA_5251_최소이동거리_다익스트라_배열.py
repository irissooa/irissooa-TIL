'''
다익스트라 이용
1. 인접행렬을 만드는데 초기값으로 값으로 올수 없는 큰값으로 초기화
2. 인접행렬에 s행 e열에(유향그래프) 가중치(w) 입력
3. dist와 visited 배열을 node수만큼 만듦
4. MIN값 갱신과 MIN방문표시
5. 갱신된 MIN값에서 모든 노드들을 둘러보면서 최소값으로 dist를 갱신
'''
import sys
sys.stdin = open('input.txt','r')

#다익스트라로 풀기
def dijkstra():
    dist = [987654321]*(N+1)
    visited = [False] * (N+1)
    #시작 node 거리표시
    dist[0] = 0

    for _ in range(N):
        minIdx = -1
        MIN = 987654321
        #방문표시와 MIN값 갱신
        for i in range(N+1):
            #방문하지 않았고, MIN보다 더 짧다면 MIN값 갱신
            if not visited[i] and MIN > dist[i]:
                MIN = dist[i]
                minIdx = i
        #min값 방문표시
        visited[minIdx] = True
        
        #갱신한 MIN에서 j로 향할때 더 작은 값이 있으면 dist를 더 작은값으로 바꿔줌
        for j in range(N+1):
            #방문하지 않았고, min에서 j로 향하는 값이 더 작은게 있다면 dist[j] 갱신
            if not visited[j] and dist[j] > adj[minIdx][j] + dist[minIdx]:
                dist[j] = adj[minIdx][j] + dist[minIdx]
    return dist[N]

T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())
    adj = [[987654321] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        adj[s][e] = w
    print('#{} {}'.format(tc,dijkstra()))