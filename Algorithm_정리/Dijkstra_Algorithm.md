# Dijkstra_Algorithm(최단경로찾기)

[toc]

- 다익스트라 알고리즘은 음이 아닌 가중치가 있는 그래프에서 최단 경로를 찾는 가장 기본적이고 효율적인 알고리즘
- 정점의 수가 V, 간선의 수가 E일 때 다익스트라 알고리즘은 구현하는 방법에 따라 매 루프마다 전체 정점을 탐색해서 최단 거리의 정점을 선택하여 `O(V^2+E)`,
- 힙을 사용한 우선순위 큐로 구현하여 `O(VlogE+ElogE)`, 피보나치 힙을 사용해 시간복잡도를 줄이지만 큰 상수 때문에 실제로는 거의 사용되지 않는 `O(VlogV+E)` 등의 시간복잡도를 가질 수 있지만, 이 중 가장 대중적이면서도 대부분의 문제에 사용해도 무리가 없는 버전은 힙을 사용한 우선순위 큐

## 쉽게 틀릴 수 있는 문제점들

>V개의 정점과 E개의 간선이 있고, 정점에는 1부터 V까지의 자연수 번호가 붙어있다. 간선은 단방향이고 중복되지 않으며 1 이상 10^6 이하의 자연수 가중치를 가진다. 1번 정점에서 V번 정점으로 가는 최단 거리를 구하여라.

-  각 정점에 대해 인접 리스트를 만들고, 구조체에서 비교 함수를 거리로 정의한 뒤 라이브러리에서 제공하는 우선순위 큐를 이용해 거리가 짧은 정점부터 빼낸 뒤 그 정점에서 갈 수 있는 다른 정점들에 대한 거리를 갱신해주고 우선순위 큐에 다시 넣는다.

### 이미 방문한 정점을 다시 방문(시간줄여줌)

```python
#적어줘야됨
if distances[current_node] < current_distance:
            continue
```

정답 코드와 같이 구현을 하면 같은 정점이 우선순위 큐에 중복으로 삽입되는 일이 생길 수 있다. 우선순위 큐에서 뺀 적이 없는데도, 거리가 갱신되면 다시 삽입을 하기 때문이다. 물론 이렇게 해도 우선순위 큐에는 최대 간선의 수만큼만 원소가 삽입되므로 시간복잡도에 문제는 없다.

중요한 것은 뺀 이후다. 정답 코드에서 이부분을 지운다면?

이미 방문했던 정점을 다시 방문하는 것이 시간을 많이 걸리게 하려면 현재 정점에서 나가는 간선들에 대한 체크를 많이 하게 만들어야 한다. 또한 같은 정점을 방문하는 횟수가 많아질수록 더 오래 걸림

### 거꾸로 된 비교 연산자

### 정점의 거리 대신 간선의 가중치를 우선순위 큐에 넣기

### 간선의 가중치를 우선순위 큐에 넣을 뿐만 아니라, 비교 연산자도 틀리기



## SWEA_5251_최소이동거리

### 배열이용

```python
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
```



### Heapq 이용

```python
import heapq

def dijstra():
    # p = [None] * (V+1)
    dist = [987654321] * (V + 1)
    visited = [False] * (V + 1)
    heap = []
    #가중치와 인덱스
    heapq.heappush(heap,(0,0))
    dist[0] = 0

    while heap:
        #우선순위(w로 정렬됨)에 따라 제일 작은값이 pop돼서 나옴
        w, v = heapq.heappop(heap)

        if not visited[v]:
            visited[v] = True
            dist[v] = w
            for i in range(V+1):
                if not visited[i] and (dist[i] > dist[v]+adj[v][i]):
                    heapq.heappush(heap, (dist[v]+adj[v][i], i))


    return dist[V]

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj = [[987654321] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        st, ed, w = map(int, input().split())
        adj[st][ed] = w

    print("#{} {}".format(tc, dijstra()))

```



### heapq와 딕셔너리 이용

```python
'''
다익스트라 이용(heapq이용)

'''
import sys
sys.stdin = open('input.txt', 'r')
import heapq
from collections import defaultdict
INF = sys.maxsize

# 다익스트라로 풀기
# 탐색할 그래프와 시작 정점을 인자로 전달받음
def dijkstra(graph, start):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성, 큰값(987654321)으로 초기화
    # distances = {node: 987654321 for node in range(N+1)}
    distances = [INF]*(N+1)
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

```



## BOJ_1753_최단경로

> [BOJ_1753_최단경로](https://www.acmicpc.net/problem/1753)
>
> python으로 제출하면 시간초과!! pypy3는 통과..!
>
> WHY?? input 받을때 sys.stdin.readline()으로 받으면 된다!! => 입력이 너무 커서 시간초과가남

```python
import sys
sys.stdin = open('input.txt','r')
import heapq

#추가하면 input()이 모두 sys.stin.readline()으로됨
input = sys.stdin.readline
INF = sys.maxsize
def dijkstra(x):
    #dist배열을 매우큰값으로 초기화
    dist = [987654321]*(V+1)
    heap = []
    #start 거리표시
    dist[x] = 0
    #heap에다가 (0(처음거리),출발점)넣는다.
    heapq.heappush(heap,(dist[x],x))
    #heap이 다 빌 때까지 반복
    while heap:
        #현재위치까지의 거리와 현 위치
        w,p = heapq.heappop(heap)  
        #현재값의 dist에 저장돼있는 값이 지금 거리보다 작다면 continue -> 시간줄이기위해
        if dist[p] < w:
            continue
        #nw,nx는 x에서 nx까지 거리, x와 연결된 애
        for nw,nx in adj[p]:
            #nw에 w를 더해줌 :  출발점에서 nx까지 거리
            nw += w
            #이게 기존에 기록해둔 값보다 작으면 갱신
            if nw < dist[nx]:
                dist[nx] = nw
                heapq.heappush(heap,[nw,nx])
    return dist

#정점개수,간선개수
V,E = map(int,input().split())
#시작정점번호
start = int(input())
#u -> v , w가중치
#1부터 V까지
adj = [[]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u,e,w = map(int,input().split())
    adj[u].append([w,e])
ans = dijkstra(start)
# print(ans)
for i in range(1,V+1):
    if ans[i] != 987654321:
        print(ans[i])
    else:
        print('INF')
```

- 현우's code

> 딕셔너리 이용

```python
import sys,heapq
INF = sys.maxsize
input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())
#정점별로 딕셔너리만듦
adj = [dict() for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    #adj u정점에 v 키값이 있으면 그 value값과 w(현재입력받은 가중치)를 비교해서 더 작은값을 받음
    if v in adj[u]:
        adj[u][v] = min(adj[u][v],w)
    #v 키값이 없으면 v키에 w value값을 담음
    else:
        adj[u][v] = w

d = [INF for _ in range(V+1)]
d[K] = 0
pq = [[d[K],K]]

while pq:
    cur_w,cur_v = heapq.heappop(pq)
    if cur_w > d[cur_v]:
        continue
    for next_v,next_w in adj[cur_v].items():
        if d[next_v] > cur_w + next_w:
            d[next_v] = cur_w + next_w
            heapq.heappush(pq, [d[next_v],next_v])

for i in range(1,V+1):
    if d[i] == INF:
        print('INF')
    else:
        print(d[i])
```



## BOJ_1916_최소비용구하기

> [BOJ_1916_최소비용구하기](https://www.acmicpc.net/problem/1916)
>
> WHY?? input 받을때 sys.stdin.readline()으로 받으면 된다!! => 입력이 너무 커서 시간초과가남

```python
import sys
sys.stdin = open('input.txt', 'r')
import heapq

#추가하면 input()이 모두 sys.stin.readline()으로됨
input = sys.stdin.readline

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

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    start,end,cost = map(int,input().split())
    adj[start].append([cost,end])
start_city,end_city = map(int,input().split())
# print(adj)
# print(start_city,end_city)
print(dijkstra(start_city))
# print(dist)
```



## BOJ_1238_파티

> [BOJ_1238_파티](https://www.acmicpc.net/problem/1238)

```python
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
```





## Reference

http://www.secmem.org/blog/2019/01/09/wrong-dijkstra/