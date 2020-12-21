'''
다익스트라 이용(heapq이용)
1.
'''
import sys
sys.stdin = open('input.txt', 'r')
import heapq
from collections import defaultdict

# 다익스트라로 풀기
# 탐색할 그래프와 시작 정점을 인자로 전달받음
def dijkstra(graph, start):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성, 큰값(987654321)으로 초기화
    # distances = {node: 987654321 for node in range(N+1)}
    distances = [987654321]*(N+1)
    # print(distances)
    # 그래프의 시작 정점의 거리는 0으로 초기화해줌
    distances[start] = 0
    # 모든 정점이 저장될 큐(힙)를 생성
    queue = []
    # 그래프의 시작 정점의 거리(0)와 시작 정점을 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start],start])
    # print(queue)

    while queue:
        # 큐에서 가장 작은 원소를 삭제 후에 그 값을 리턴, 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트
        #현위치까지의 거리,현위치
        current_distance,current_node = heapq.heappop(queue)
        # print('aa',current_node,current_distance)
        #
        if distances[current_node] < current_distance:
            continue

        for weight,adjacent in graph[current_node]:
            # print('dd',graph[current_node],adjacent,weight)
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우
            # print(distance,adjacent)
            if distance < distances[adjacent]:
                # 거리를 업데이트
                distances[adjacent] = distance
                heapq.heappush(queue, [distance,adjacent])
    return distances[N]

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    # print(N,'node')
    #딕셔너리에 값이 없을떄 빈 배열을 초기값으로 설정
    adj = defaultdict(list)
    for _ in range(E):
        s,e,w = map(int,input().split())
        #start노드를 키값으로 가지고, 가중치(w)와 end를 튜플로 담아줌
        adj[s].append((w,e))
    # print(adj)
    ans = dijkstra(adj, 0)
    # print(ans[N])
    print('#{} {}'.format(tc,ans))
