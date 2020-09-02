# Algorithm

> 백트래킹 : 조합적 문제 (재귀) + 가지치기
>
> 1. 부분집합
> 2. 순열 , 중복 순열
> 3. 조합, 중복 조합

## 순열

- swap 방법(재귀)
- 원래배열은 그대로 돌아오게됨

```python
arr= [1,2,3]
N = 3
def perm(idx):
    if idx == N:
        print(arr)
        return
   	for i in range(idx,N):
        arr[idx],arr[i] = arr[i], arr[idx]
        perm(idx+1)
        arr[idx],arr[i] = arr[i], arr[idx]
perm(0)
```



```python
def perm(n,k):
    if k == n:
        print(arr)
    else:
        for i in range(k,n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n,k+1)
            arr[k], arr[i] = arr[i],arr[k]
arr = [1,2,3]
N = len(arr)
perm(N,0)
```



## 큐

> stack: push, pop, top
> queue: enQ(파이썬 :`.append(item)`), deQ(파이썬 : `.pop(0)`, Qpeek

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
  - 큐의 뒤에서는 삽입만하고, 앞에서는 삭제만 이루어지는 구조
- 선입선출구조(First In First Out)
  - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장 먼저 삭제됨

![image-20200902103925765](0902_algorithm(이론)_Queue,BFS, 최단경로 등.assets/image-20200902103925765.png)

### 큐의 연산 과정

![image-20200902104146127](0902_algorithm(이론)_Queue,BFS, 최단경로 등.assets/image-20200902104146127.png)

### 큐의 구현

#### 선형 큐

- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - front : 저장된 첫 번째 원소의 인덱스
  - rear : 저장된 마지막 원소의 인덱스
- 상태 표현
  - 초기상태 : front = rear = -1
  - 공백 상태: front = rear
  - 포화 상태: rear = n-1(n:배열의 크기, n-1배열의 마지막 idx)



#### 삽입 : enQueue(item)

- 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
  1. rear값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
  2. 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장

#### 삭제 : deQueue()

- 가장 앞에 있는 원소를 삭제하기 위해
  1. front값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소 이동
  2. 새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능함

#### 공백상태 및 포화상태 검사 : `isEmpty()`,`isFull()`

- 공백상태: front = rear
- 포화상태: rear = n-1(n:배열의 크기, n-1 : 배열의 마지막 idx)

#### 검색 : `Qpeek()`

- 가장 앞에 있는 원소를 검색하여 반환하는 연산
- 현재 front의 한자리 뒤(front+1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환

##### 연습문제1

> 세 개의 데이터 1,2,3을 차례로 큐에 삽입하고 큐에서 세 개의 데이터를 차례로 꺼내서 출력함

```python
#front, rear 이용
Q = [0]*100
front, rear = -1,-1

def enQueue(item):
    global rear
    if rear == len(Q) -1:
        print('Queue Full')
    else:
        rear = rear + 1
        Q[rear] = item
def deQueue():
    global front
    if front == rear:
        print('Queue Empty')
    else:
        front += 1
        return Q[front]
def Qpeek():
    if front == rear:
        print('Queue Empty')
    else:
        return Q[front+1]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())

```

#### 선형 큐 이용시의 문제점

> 파이썬에는 선형과 원형의 차이가 별로 없음.

- 잘못된 포화상태 인식
  - 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불고, rear = n-1인 상태, 즉 포화상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨

##### 해결방법1

- 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴
- 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐

##### 해결방법2

- 1차원 배열을 사용하되, 원형 형태의 큐를 이룬다고 가정하고 사용

### 원형 큐의 구조

- 초기 공백 상태
  - front = rear = 0
- index의 순환
  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동
  - 나머지 연산자 mod를 사용
- front 변수
  - 공백 상태와 포화상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
- 삽입 위치 및 삭제 위치

| 구분   | 삽입위치               | 삭제위치                  |
| ------ | ---------------------- | ------------------------- |
| 선형큐 | rear = rear+1          | front = front+1           |
| 원형큐 | rear = (rear + 1)mod n | front = (front + 1) mod n |

```python
#front, rear 이용
Q = [0]*100
front, rear = -1,-1

def enQueue(item):
    global rear
    if rear == len(Q) -1:
        print('Queue Full')
    else:
        rear = (rear + 1) % SIZE # full
        Q[rear] = item
def deQueue():
    global front
    if front == rear:
        print('Queue Empty')
    else:
        front = (front + 1) % SIZE
        return Q[front]
def Qpeek():
    if front == rear:
        print('Queue Empty')
    else:
        return Q[(front+1) % SIZE]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
enQueue(4)
print(deQueue())
enQueue(5)
print(deQueue())
print(Q)
```



###### 연결 큐의 구조(X)->안함,C언어, B형시험 볼때 필요할 수있지만...파이썬은 아님..



### 우선순위 큐

- 우선순위를 가진 항목들을 저장하는 큐
- FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나감
- 적용분야
  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영체제의 테스크 스케줄링

- 배열을 이용한 우선순위 큐
  - 배열을 이용하여 자료 저장
  - 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
  - 가장 앞에 최고 우선순위의 원소가 위치하게 됨
  - 문제점
    - 배열을 사용하므로 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생
    - 소요시간이나 메모리 낭비가 큼
- 리스트를 이용한 우선순위큐



### 큐의 활용 버퍼(Buffer)

- 버퍼
  - 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  - 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미
- 버퍼의 자료구조
  - 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용됨
  - 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용됨



## **BFS**(Breath First Search) 중요!!!!!

- 그래프(비선형구조)
  - 표현 방법 : 인접행렬, 인접 리스트
  - 순회 : DFS, BFS
-  탐색 방법

> DFS(재귀)는 스택이 빌때까지
>
> BFS는 Queue가 빌때까지

- DFS(깊이 우선탐색)

  ```sh
  - 방문(v)
  - v에 인접한 정점(w)
  - w가 방문(x)
  - dfs(w)
  ```

- BFS(너비 우선 탐색)

  ```sh
  - enQ(v)
  - 방문(v)
  - while Q:
    - v =deQ()
    - v에 인접한 정점(w)
    - w가 방문(x)
      - enQ(w)
      - 방문(w)
  ```

- BFS

  - 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후,
  - 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차레로 방문하는 방식
  - *인접한 정점들에 대해 탐색*(`FIFO형태`)을 한 후, 
  - 차례로 다시 BFS을 진행
  - 선입선출 형태의 자료구조인 **큐**를 활용함

- BFS 알고리즘

- 입력 파라미터 : 그래프 G와 탐색 시작점 v(enQ시 방문처리)

  - 출발점에서 얼만큼 떨어져있는지 visited를 통해 확인 가능

```python
def BFS(G,V): #그래프 G,탐색 시작점 v
    visited = [0] * (n+1) #n:정점의 개수
    q=[] #큐 생성
    
    q.append(v) #시작정점 v를 enQueue
    visited[v] = 1 #방문한 것으로 표시
    
    while len(q) != 0: #큐가 비어있지 않은 경우
        t = q.pop(0) #deQueue(왼쪽 원소 반환)
        for w in G(t): #정점 t와 인접한 정점w에 대해
            if not visited[w]: #방문하지 않은 곳이라면// enQueue할때 방문처리해야됨!!!
                q.append(w) #enQueue
                visited[w] = visited[t]+1 #방문한 것으로 표시
```

1. 초기상태
   1. visited 배열 초기화
   2. Q생성
   3. 시작점 enqueue

2. A점부터 시작
   1. dequeue A
   2. A 방문한것으로 표시
   3. A의 인접점 enqueue

3. 탐색 진행

   1. dequeue B
   2. B 방문한 것으로 표시
   3. B의 인접점 enqueue

   1. dequeue C
   2. C 방문한것으로 표시
   3. C의 인접점 enqueue
   4. D,E,F,G,H,I 도 탐색진행

4. Q가 비었으므로 탐색 종료



#### deQ시 방문처리

```python
def BFS(G,V):#그래프G, 탐색 시작점v
    visitied = [0]*n #n: 정점의 개수
    queue = []#큐생성
    queue.append(v) #시작점 v를 큐에 삽입
    while queue: #큐가 비어있지 않은 경우
        t =  queue.pop(0) #큐의 첫번째 원소 반환
        if not visited[t]: #방문되지 않은 곳이라면
            visited[t] =True #방문한 것으로 표시
            visite(t)
        for i in G[t]: #t와 연결된 모든 선에 대해
            if not visited[i]: #방문되지 않은 곳이라면
                queue.append(i) #큐에 넣기
```



#### 연습문제 3

![image-20200902150719073](0902_algorithm(이론)_Queue,BFS, 최단경로 등.assets/image-20200902150719073.png)

출력값 : 

- 1-2(1)-3(1)-4(2)-5(2)-7(2)-6(3)
- (n) : 1과 떨어진 간선의 수(거리)

```python
'''
7(정점) 8(간선수)
간선 : 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v):
    #큐, 방문처리,
    Q = []
    visit = [0] *(V+1)
    #enQ(v), visit(v)
    Q.append(v)
    visit[v] = 1 #방문체크(True)
    print(v,end = ' ')
    #큐가 비어있지 않은 동안
    while Q:
    	#v = deQ()에서 하나 받아와라
        v = Q.pop(0)
        #v의 인접한 정점(w), 방문안한 정점이면
        for w in range(1,V+1):
        	if G[v][w] ==1 and visit[v][w] == 0:
            #enQ(w), 방문처리(w)
            Q.append(w)
            visit[w] = 1
            print(v,end= ' ')

#입력 -> G:인접행렬(0idx는 쓰지않음,V+1!!!)
V,E = map(int,input().split())
temp = lsit(map(int,input().split()))
#인접행렬 초기화
G = [[0]*(V+1) for _ in range(V+1)]
# 인접행렬 저장
for i in range(E): #간선의 개수: E
    s, e =temp[2*i], temp[2*i+1] #####??
    G[s][e] = G[e][s] = 1 #무향, 연결표시
#인접행렬 출력
for i in range(1,V+1): #0idx안쓰기때문
    print('{} {}'.format(i,G[i]))

bfs(1)
```

- 인접리스트! 이용 방법

```python
'''
7(정점) 8(간선수)
간선 : 1 2/ 1 3/ 2 4/ 2 5/ 4 6/ 5 6/ 6 7/ 3 7
순서대로 넣음! 1에 2를 넣고 2에 1을 넣어라! 이런식으로 리스트를 채워나감
'''

def bfs(v):
    Q = []
    visit = [0] *(V+1)
    #enQ()
    Q.append(v)
    visit[v] = 1
    print(v,end = ' ')
    #Q가 비어있지 않은 동안
    while Q:
        v = Q.pop(0)
        #idx1부터 들어있는 인접리스트를 불러옴
        for w in G[v]:
            #w에 방문을 안했으면
            if not visit[w]:
                Q.append(w)
                visit[w] = 1
            	print(w,end = ' ')


#입력 -> 인접리스트
V,E = map(int,input().split())
temp = lsit(map(int,input().split()))
#인접리스트, 빈리스트로 V+1만큼 만들어라!(초기화)
G = [[] for _ in range(V+1)]
#[[],[],[],[],[],[],[],[]]
for i in range(E):
    s,e = temp[2*i], temp[2*i+1]
    G[s].append(e)
    G[e].append(s)
print(G)
bfs(1) #결과 : 1,3,4,5,7,6



```

- #1에서 가장 멀리 있는 정점의 번호는 얼마이고, 몇칸(간선의 개수) 떨어져 있나요?

```python
'''
7(정점) 8(간선수)
간선 : 1 2/ 1 3/ 2 4/ 2 5/ 4 6/ 5 6/ 6 7/ 3 7
순서대로 넣음! 1에 2를 넣고 2에 1을 넣어라! 이런식으로 리스트를 채워나감
'''

def bfs(v):
    Q = []
    #enQ()
    Q.append(v)
    visit[v] = 1
    print(v,end = ' ')
    #Q가 비어있지 않은 동안
    while Q:
        v = Q.pop(0)
        #idx1부터 들어있는 인접리스트를 불러옴
        for w in G[v]:
            #w에 방문을 안했으면
            if not visit[w]:
                Q.append(w)
                #이거를 적으면 그전꺼 포함해서 거리만큼 1씩 더해짐
                visit[w] = visit[v] + 1
            	print(w,end = ' ')


#입력 -> 인접리스트
V,E = map(int,input().split())
temp = lsit(map(int,input().split()))
#인접리스트, 빈리스트로 V+1만큼 만들어라!(초기화)
G = [[] for _ in range(V+1)]
#[[],[],[],[],[],[],[],[]]
 visit = [0] *(V+1) #visit을 써야되기 때문에 여기에 적음
for i in range(E):
    s,e = temp[2*i], temp[2*i+1]
    G[s].append(e)
    G[e].append(s)
print(G)
bfs(1) #결과 : 1,3,4,5,7,6
print()
max_idx = 0
for i in range(1,V+1):
    if visit[max_idx] <visit[i]:
        max_idx = i
        #시작이 1로들어가있기때문에 1빼줘야됨
print(max_idx,visit[max_idx-1]) #6 3
```

- `#key값과 []가 value로 나옴
  G = {i:[] for i in range(1,V+1)}`
- 이렇게 적을 수도 있음

