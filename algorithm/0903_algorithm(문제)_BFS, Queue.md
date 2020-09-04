# Algorithm BFS, Queue

## BFS

## SWEA_ 5105_미로의 거리

```python
'''
NxN크기 미로
최소 몇 개의 칸을 지나면 출발지 도착?
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수,
경로가 없는 경우 0을 출력
1:벽, 0:통로 2:출발 3:도착
bfs로 품
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,0,1,-1]#우좌하상
dj = [1,-1,0,0]
def BFS(i,j):
    # global dist
    q = []
    q.append([i,j]) #시작점 넣기[i,j]
    visited[i][j] = -1 #방문을 했다는 표시..와 동시에 처음부터 거리를 1빼줌

    while q: #q가 비어있지 않으면 계속 돈다
        temp = q.pop(0) #맨앞의 원소를 담음
        #현재의 i와 j를 변수로 표시
        pi, pj = temp[0],temp[1]
        #종료조건
        if maze[pi][pj] == 3:
            # print(visited[pi][pj],'거ㄹㅣ')
            return visited[pi][pj]

        #4방향 탐색
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            #범위를 벗어났다면 넘어가기
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
                #갈수있는 자리가 아니거나
            if maze[ni][nj] == 1:
                continue
                #이미 거리를 구했다면 넘어가기
            if visited[ni][nj] != 0:
                continue
            #그게아니다!! 거리를 갱신 후 큐에 삽입
            q.append([ni,nj]) #다음 좌표를 추가
            ###제일중요!!!!!방문처리를 여기다가 해줌(최단거리를 구할때 보통 현재위치 pi,pj의 방문배열에다가 1씩 더해줌!-> 다음좌표로 넘어가면서 1씩 더해짐)
            visited[ni][nj] = 1 + visited[pi][pj]
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    visited = [[0 for j in range(N)] for i in range(N)]
    dist = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                result = BFS(i,j)
    print('#{} {}'.format(tc,result))
```



## SWEA_5102_노드의 거리

- 그래프 탐색 -> 출발점에서 도달가능한 정점들 찾을 수 있음(경로)
- BFS는 그래프 탐색을 하게되면 특성상 출발점에서 가장 가까운 정점(인접정점, 거리가 1인 정점) 
  - q에 저장
  - 거리가 1인 것 저장, 2인것 저장....도착점까지 가는 거리 저장
  - DFS 보다 **최단으로 갈 수 있는 거리(최적화)**를 더 쉽게 구할 수 있음!(DFS로는 보장할 수 없음)
- 예시

![image-20200904110052672](0903_algorithm(문제)_BFS, Queue.assets/image-20200904110052672.png)

- v -> w
- visit[w] = 1
- D[w] = D[v] +1
- P[w] = v

|           정점            | 1(출발) |  2   |  3   |  4   |  5   |  6   |  7   |
| :-----------------------: | :-----: | :--: | :--: | :--: | :--: | :--: | :--: |
|   D(출발점에서최단거리)   |    0    |  1   |  1   |  2   |  2   |  3   |  2   |
| P(BFS트리,이전 방문 정점) |    1    |  1   |  1   |  2   |  2   |  4   |  3   |

- Q = 1 2 3 4 5 7 6 (경로)
- P는 부모(어디서 왔는지)를 알 수 있음, 도착점의 이전 정점번호를 읽으면서 실제 최단 거리까지의 정점들의 경로를 알 수 있음(보통 거리를 구하라고 함, 굳이 출력하라고 하지 않음)
- 1번에서 7번까지 가는 경로가 3가지인데 그중 가장 짧은 것이 2번만에 가는 것이다
- 이런식으로 추가해서 생성할 수 있음, 하지만 방문이랑 D랑 같이 쓰면 간편하기 때문에 같이 쓰는 경우도 많음

![image-20200904111540803](0903_algorithm(문제)_BFS, Queue.assets/image-20200904111540803.png)

- 문제풀기

```python
'''
V개의 노드 개수
방향성 없는 E개 간선
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는가
S와 G가 서로 연결되어 있지 않다면 0 출력
BFS이용, 방문하면 +1을 하여 최단 거리를 기록함
인접리스트도 이용함
'''
import sys
sys.stdin =open('input.txt','r')

def BFS(s):
    q = []
    #시작점을 넣는다
    q.append(s)
    visited[s] = 1

    while q:# q가 있다면
        #queue는 선입선출, 제일 앞 정점을 뽑음
        p = q.pop(0)

        #해당 정점의 인접리스트를 볼거야
        for i in adj_list[p]:
            #그 정점을 방문하지 않았다면
            if not visited[i]:
                #queue에 append를 하고 방문표시
                q.append(i)
                visited[i] = visited[p] + 1 #다음 방문표시를 해주는데, 현 방문표시에+1로 거리를 표현함
            #종료조건(도착한다면)
            if p == G:
                #출발점(0부터시작인데 1이 더해졌으니 빼줌)
                return visited[G]-1
    #도착하지 못한다면
    return 0



T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    #인접 리스트
    adj_list = [[] for _ in range(V+1)]
    #간선수만큼 시작점, 끝점 이어진 것 표시
    for i in range(E):
        st,ed = map(int,input().split())
        #시작점(idx)의 list에 ed를 넣음
        adj_list[st].append(ed)
        #끝점(idx)의 list에 st를 넣음
        adj_list[ed].append(st)
    S, G = map(int,input().split())
    visited = [0] * (V+1) #정점+1개의 방문배열 만듦,0idx는 사용안함
    # BFS(S)

    print('#{} {}'.format(tc,BFS(S)))
```

- 선생님 코드

```python
#선생님풀이
for tc in range(1,int(input())+1):
    V,E = map(int,input().split())
    #인접행렬
    G = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        u,v = map(int,input().split())
        #방향이 없기 때문
        G[u][v] = G[v][u] = 1
        
    s,e = map(int,input().split()) #출발 도착
    
    visit = [0] * (V+1) #정점의 개수만큼 만듦
    Q = [s] #출발점을 미리 넣어둠
    visit[s] = 1 #출발점의 방문표시 0으로 해야되지만 방문표시랑 같이 사용하기 위해 1이라고 함, 큐에 삽입
    
    while Q: #빈큐가 아닐동안 반복
        v = Q.pop(0) #큐에서 뺌
        #v의 방문하지 않은 인접정점을 찾는다
        #연결된 모든 정점들 확인함
        for w in range(1,V+1):
            if G[v][w] and not visit[w]: #G[v][w] == 1 and visit[w]==0:이란 말
                visit[w] = visit[v] + 1 #거리계산
                Q.append(w)
    print(visit[e]-1)#visit을 방문표시와 거리를 같이 표현했기 떄문에 원래 거리로 했을 시 0부터 시작이니 1을 빼줌
```

- 종료조건을 주는 것도 좋음!
  - while문 바로 아래에 둬도 되고, 
  - for문 안에 두고 도착지점에 도달했을 때 break하기전에 Q를 비워주고 break하면 while문도 나올 수 있음

```python
    while Q: #빈큐가 아닐동안 반복
        v = Q.pop(0) #큐에서 뺌
        #방법 1. 여기다가 종료조건을 줘도됨
        # if v == e:
        #     break
        #v의 방문하지 않은 인접정점을 찾는다
        #연결된 모든 정점들 확인함
        for w in range(1,V+1):
            if G[v][w] and not visit[w]: #G[v][w] == 1 and visit[w]==0:이란 말
                visit[w] = visit[v] + 1 #거리계산
                #방법2 종료조건 
                #if w == e:# 도착점에 도착했네?
                #     Q.clear() #큐를 비우고(break해도 while에서 못나가서) 빠짐
                #     break
                Q.append(w)
```

- 인접리스트로 사용하는 것이 좀 더 효율적!! 익숙해지자

```python
for tc in range(1,int(input())+1):
    V,E = map(int,input().split())
    #인접리스트
    G = [[] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        u,v = map(int,input().split())
        G[u].append(v)
        G[v].append(u)

    s,e = map(int,input().split()) #출발 도착
    
    visit = [0] * (V+1) #정점의 개수만큼 만듦
    Q = [s] #출발점을 미리 넣어둠
    visit[s] = 1 #출발점의 방문표시 0으로 해야되지만 방문표시랑 같이 사용하기 위해 1이라고 함, 큐에 삽입
    
    while Q: #빈큐가 아닐동안 반복
        v = Q.pop(0) #큐에서 뺌
        #여기다가 종료조건을 줘도됨
         if v == e:
             break
        #인접리스트
        for w in G[v]:
            if visit[w] == 0:#방문하지 않았다면
                visit[w] = visit[v]+1 #거리계산
                Q.append(w)
    print(visit[e]-1)#visit을 방문표시와 거리를 같이 표현했기 떄문에 원래 거리로 했을 시 0부터 시작이니 1을 빼줌
```



## SWEA_5097_회전

```python
'''
N개의 숫자로 이루어진수열, 맨앞의 숫자를 맨 뒤로 보내는 작업 M번
수열의 맨 앞에 있는 숫자를 출력
'''
import sys
sys. stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) #M은 최대 1000
    arr= list(map(int,input().split()))
#M번 작업을 진행, 맨앞의 숫자를 pop하고, 그 숫자를 제일 뒤에 붙임
    for i in range(M):
        arr.append(arr.pop(0))
    print('#{} {}'.format(tc,arr[0]))
```

- 선생님 풀이1, 나처럼도 풀고, 다양한 방법 보여주심

```python
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) #M은 최대 1000
    arr= list(map(int,input().split()))
#아래 식을 안쓰고 M % N의 idx값을 넣어도 답을 구할 수 있음
    print('#{} {}'.format(tc,arr[M % N]))
```

- 선형 큐

```python
 #선형큐일경우(파이썬제외) 뒤에 M번 만큼 추가할 리스트를 추가해줘야됨
    arr= list(map(int,input().split())) + ([0] * M)
    f,r = -1,N-1
    for _ in range(M):
        f += 1 #arr[f]
        r += 1
        arr[r] = arr[f]
    print(arr[f+1])
```

- 원형큐

```python
#원형큐일경우
    arr= [0] +list(map(int,input().split()))
    f,r = 0,N
    SIZE = N+1
    for _ in range(M):
        f = (f+1) % SIZE
        r = (r+1) % SIZE
        arr[r] = arr[f]
    print(arr[(f+1) % SIZE])
```



## SWEA_5099_피자굽기

![image-20200904101126044](0903_algorithm(문제)_BFS, Queue.assets/image-20200904101126044.png)

![image-20200904101635000](0903_algorithm(문제)_BFS, Queue.assets/image-20200904101635000.png)

![image-20200904101751106](0903_algorithm(문제)_BFS, Queue.assets/image-20200904101751106.png)

- 한바퀴 돌고 1번을 예로 들면 치즈 양이 7이니까 7//2=3 으로 꺼냈다가 다시 넣음
- 제일 앞 꺼내고 제일 뒤로 보냄
- 다시돌면 2번 나옴 반복(피자 치즈 양이 0 이되면 뺌)
- 여분으로 남아있는 피자를 다시 넣으면 된다.

```python
for tc in range(1,int(input())+1):
    N,M = map(int,input().split()) #N:화덕의 크기 M:피자수
    #피자번호와 idx번호를 맞추기 위해 앞에 0을 추가함
    pizza = [0] + list(map(int,input().split())) #치즈양
    #화덕(q처럼 사용할 예정), 피자번호를 저장함
    oven = [i for i in range(1,N+1)] #피자번호
    pos = N+1 #추가될 남은 피자 초기값(M개중에 오븐에 N개들어가고 남은 것 시작 점)

    while len(oven) > 1: #한개가 되면 pop해서 없앨거야
        num = oven.pop(0)
        pizza[num] = pizza[num] // 2 #치즈양 한바퀴,반으로 줄어듦
        if pizza[num]: #0이 아님
            oven.append(num)
        else: #0이면 새로운 피자 집어넣음
            if pos <= M: #M까지만 넣고 넘으면 추가안함
                oven.append(pos)
                pos += 1 #다음번호를 가리키게 함
    print('#{} {}'.format(tc,oven[0]))

```

- 방법2

```python
#방법2
for tc in range(1,int(input())+1):
    N,M = map(int,input().split()) #N:화덕의 크기 M:피자수
    #피자번호와 idx번호를 맞추기 위해 앞에 0을 추가함
    pizza = [0] + list(map(int,input().split())) #치즈양
    #번호랑 치즈양을 묶어서넣어줌
    oven = [[i,pizza[i]] for i in range(1,N+1)] #피자번호
    #남은 피자
    remain = [[i,pizza[i]] for i in range(N+1,M)]
    pos = N+1 #추가될 남은 피자 초기값(M개중에 오븐에 N개들어가고 남은 것 시작 점)

    while len(oven) > 1: #한개가 되면 pop해서 없앨거야
        num, cheeze = oven.pop(0)
        cheeze = cheeze // 2 #치즈양 한바퀴,반으로 줄어듦
        if cheeze: #0이 아님
            oven.append(num,cheeze)
        else: #0이면 새로운 피자 집어넣음
            if remain: #M까지만 넣고 넘으면 추가안함
                oven.append(remain.pop(0))
    print('#{} {}'.format(tc,oven[0]))

```

