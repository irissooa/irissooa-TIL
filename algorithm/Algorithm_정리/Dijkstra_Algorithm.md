# Dijkstra_Algorithm

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



## python code

### 

```python
def dijstra():
    # p = [None] * (V+1)
    dist = [987654321] * (V + 1)
    visited = [False] * (V + 1)

    dist[0] = 0

    for _ in range(V):
        minIdx = -1
        min = 987654321
        for i in range(V + 1):
            if not visited[i] and min > dist[i]:
                min = dist[i]
                minIdx = i
        visited[minIdx] = True
        for j in range(V + 1):
            if not visited[j] and dist[j] > adj[minIdx][j] + dist[minIdx]:
                dist[j] = adj[minIdx][j] + dist[minIdx]
                # p[j] = minIdx
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



## Reference

http://www.secmem.org/blog/2019/01/09/wrong-dijkstra/