# Algorithm BFS, Queue, 순열

## SWEA_4881_배열최소합

### 순열

```python
arr = [1,2,3]
N = len(arr)
for i in range(N):
    #0idx기준 교환
    arr[0], arr[i] = arr[i], arr[0]
    for j in range(1,N):
        #1idx기준으로 교환
    	arr[1],arr[j] = arr[j], arr[1]
        for k in range(2,N):
            arr[2],arr[k] = arr[k] , arr[2]
            print(arr)
            arr[2],arr[k] = arr[k] , arr[2]
        arr[1],arr[j] = arr[j], arr[1]
	arr[0], arr[i] = arr[i], arr[0]
```

- 위 식을 재귀로 바꿔보자!
- 앞의 idx가 0->1->2로 늘어남...! 그외에는 다 똑같음!

```python
arr = [1,2,3]
N = len(arr)

def perm(k):
    if k == N:
        print(arr)
    else:
		for i in range(k,N):
            #k idx의 위치를 기준으로!
		    arr[k], arr[i] = arr[i], arr[k]
             perm(k+1) #다음 idx로 넘어감
		    arr[k], arr[i] = arr[i], arr[k]
perm(0)
```

- 문제

```python
'''
NxN배열에 숫자가 들어있음
한줄에 하나씩 N개의 숫자를 골라 합이 최소가 되게하려함
한줄에 하나, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없음.
'''
import sys
sys.stdin = open('input.txt','r')

def perm(i,sum):
    global MIN
    # sum이 MIN보다 크거나 같으면 종료
    if sum >= MIN:
        return
    #idx가 N과 같아지면
    if i == N:
        #저장된 MIN과 sum을 비교해서 MIN보다 작으면 갱신함
        if MIN > sum:
            MIN = sum
        return
    
    for k in range(N):
        #방문표시 했다면 지나가라
        if visited[k]:
            continue
        #방문을 했다고 표시
        visited[k] = True
        #다음 idx로 함수 호출, 그 값을 더해준것을 같이 보냄
        perm(i+1,sum+board[i][k])
        #다시 방문 표시 원상 복구
        visited[k] = False


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for i in range(N)]
    visited = [False for i in range(N)]
    MIN = 9999999
    select = [-1 for i in range(N)]
    perm(0,0)
    print('#{} {}'.format(tc,MIN))
```

- 선생님 코드

1. 재귀만 사용! -> 7개에서 timeerror

```python
#순열을 하려면 열값을 [0,1,2,....N-1]까지 각 idx에 있는 값을 행의 같은 idx에 저장!
#이렇게 하면 7개에서 timeerror!
def perm(k):
    if k == N:
        S = 0
        for r,c in enumerate(cols):
            S += arr[r][c]
        global ans;ans = min(ans,S)
    else:
        for i in range(k,N):
        #k idx의 위치를 기준으로!
		    cols[k], cols[i] = cols[i], cols[k]
            perm(k+1) #다음 idx로 넘어감
            cols[k], cols[i] = cols[i], cols[k]

for tc in range(int(int(input()))+1):
    N = int(input())
    arr = [list(map(int,input().split())) for_ in range(N)]
    cols = [i for i in range(N)]
    ans = 0xffffff
    perm(0)
```

2. 가지치기! cur_sum만 인자로 하나 더 추가했을 때

- 이렇게하면 9개에서 timeerror

```python
#가지치기 -> 이렇게 하면 9개에서 timeerror
def perm(k,cur_sum): #cur_sum : 0~k-1행에 선택한 값들의 합
    global ans
    if k == N:
        ans = min(ans,cur_sum)

    else:
        for i in range(k,N):
        #k idx의 위치를 기준으로!
		    cols[k], cols[i] = cols[i], cols[k]
        #K행에 선택한 열값은 cols의 [k]idx에 있다!
            perm(k+1,cur_sum + arr[k][cols[k]]) #다음 idx로 넘어감
            cols[k], cols[i] = cols[i], cols[k]
```

3. 가지치기! 

- 지금까지 발견한 가장 좋은 해를 저장
- 탐색을 하다가 지금까지 가장 좋은 해와 비교했더니 이미 크면 더 안가봐도 되므로 바로 끊고, 그 이전의 자신을 호출한 함수로 돌아가, 아직 확인하지 못한 곳을 봐라!

```python
def perm(k,cur_sum): #cur_sum : 0~k-1행에 선택한 값들의 합
    global ans
    #가지치기
    if ans <= cur_sum:
        return #더이상 보지않고, 안해본 다른 선택지를 보러감

    if k == N:
        ans = min(ans,cur_sum)

    else:
        for i in range(k,N):
        #k idx의 위치를 기준으로!
		    cols[k], cols[i] = cols[i], cols[k]
        #K행에 선택한 열값은 cols의 [k]idx에 있다!
            perm(k+1,cur_sum + arr[k][cols[k]]) #다음 idx로 넘어감
            cols[k], cols[i] = cols[i], cols[k]
```





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

![image-20200904110052672](0903_algorithm(문제)_BFS,Queue.assets/image-20200904110052672.png)

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

![image-20200904111540803](0903_algorithm(문제)_BFS,Queue.assets/image-20200904111540803.png)

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

![image-20200904101126044](0903_algorithm(문제)_BFS,Queue.assets/image-20200904101126044.png)

![image-20200904101635000](0903_algorithm(문제)_BFS,Queue.assets/image-20200904101635000.png)

![image-20200904101751106](0903_algorithm(문제)_BFS,Queue.assets/image-20200904101751106.png)

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



## SWEA_1238_Contact

- 내풀이 어제 풀때 아래 내용과 BFS조건 중 
  1.  `arr[p][i]`인접한 정점일때!(방문안했을 떄만 표시함..)
  2. 아래 코드를 안해줘서 답이 안나왔다..

```python
for i in range(2,101):
        #크거나 같을때 , 같다면 더 idx가 큰 값!
        if visited[MAX_idx] <= visited[i]:
            MAX_idx = i
```



```python
def BFS(s):
    q = []
    #시작점을 넣는다
    q.append(s)
    visited[s] = 1

    while q:# q가 있다면
        #queue는 선입선출, 제일 앞 정점을 뽑음
        p = q.pop(0)
        for i in range(1,101):
            #인접한 정점이고, 그 정점을 방문하지 않았다면
            if arr[p][i] and not visited[i]:
                #queue에 append를 하고 방문표시
                q.append(i)
                visited[i] = visited[p] + 1



for tc in range(1,11):
    L,S = map(int,input().split())
    temp = list(map(int,input().split()))
    #인접행렬, 최대 인원 100이기 때문
    arr = [[0 for j in range(101)] for i in range(101)]
    #데이터의 길이만큼 시작점, 끝점 이어진 것 표시, 2개씩 시작,끝 시작 끝 반복
    for i in range(0,L,2):
        arr[temp[i]][temp[i+1]] = 1

    visited = [0] * (100+1) #정점+1개의 방문배열 만듦,0idx는 사용안함
    MAX_idx = 1#제일 큰값을 담을 변수
    BFS(S)
    for i in range(2,101):
        #크거나 같을때 , 같다면 더 idx가 큰 값!
        if visited[MAX_idx] <= visited[i]:
            MAX_idx = i

    print('#{} {}'.format(tc,MAX_idx))
```



- 선생님 풀이

```python
#선생님 풀이
for tc in range(1,11):
    N, s = map(int,input().split())
    arr = list(map(int,input().split()))

    G = [[0] * 101 for _ in range(101)] #정점번호 1~100
    for i in range(0,N,2): #arr[i]-->arr[i+1]
        #유향그래프
        G[arr[i]][arr[i+1]] = 1
    visit = [0] *101
    Q = [s]
    visit[s] = 1

    while Q:
        v = Q.pop(0)
        #인접정점 w
        for w in range(1,101):
            #인접정점이면서 방문하지 않은 것들을 둘러볼거야
            if G[v][w] and not visit[w]:
                visit[w] = visit[v] + 1 #이건 가장 큰 값을 구할거니까 굳이 나중에 1안빼줘도됨
                Q.append(w)
    ans = 1
    for i in range(2,101):
        #크거나 같을때 , 같다면 더 idx가 큰 값!
        if visit[ans] <= visit[i]:
            ans = i
    print(ans)

```



## SWEA_5105_미로의 거리

- 처음에 벽이 1인데 0이라고 조건을 잘못줌..ㅎ

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
            # print(visited[pi][pj],'거리')
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

- 선생님 코드

```python
#선생님 풀이
dx = [0,0,1,-1]#우좌하상
dy = [1,-1,0,0]
for tc in range(1,int(input())+1):
    N = int(input())
    #문자열로 받음
    maze = [input() for _ in range(N)]
    #정수로 받음
    # maze = [lsit(map(int,input())) for _ in range(N)]

    sx = sy = ex= ey = 0
    for i in range(N):
        for j in range(N):
            #문자열로 받았으니 ''해줘야됨
            if maze[i][j] == '2':
                sx,sy = i,j
            elif maxe[i][j] == '3':
                ex,ey = i,j
    visit = [[0] * N for _ in range(N)]
    Q = [[sx,sy]] #시작점 행과 열을 같이 묶어 넣음
    visit[sx][sy] = 1

    while Q:
        x, y = Q.pop(0)
        #종료조건
        if x == ex and y == ey:
            break
        for i in range(4):
            tx,ty = x + dx[i], y + dy[i]

            #경계 체크(가장먼저!!해야됨), 통로인지, 방문정보 체크해야됨
            #N보다 클수 없기 떄문에 ==로 표시
            if tx < 0 or tx == N or ty < 0  or ty ==N:
                continue
                #벽인경우 못감, 또는 이미 방문을 했다면
            if maze[tx][ty] == '1' or visit[tx][ty]:
                continue
            visit[tx][ty]  = visit[x][y] +1
            # #종료조건
            # if tx == ex and ty ==ey:
            #     Q.clear()
            #     break
            Q.append([tx,ty])
    #출발과 도착의 칸 개수를 빼줘야 원하는 거리가 나옴
    #but 도착하지 못하는 경우, 0
    if visit[ex][ey]: #0이아닌경우
        visit[ex][ey] -= 2
    
    print(visit[ex,ey])
```





## SWEA_4613_러시아 국기 같은 깃발

```python
'''
러시아 국기 만들기
N행 M열 배열 주어짐
위에서 부터 최소 한줄 흰 , 파, 빨강 색을 만들어야 됨
새로 칠 해야 하는 칸긔 개수 최소값을 구하라
최소 1줄씩은 색이 있어야됨(첫줄, 마지막줄은 흰, 빨로 고정)
하영's hint
for문으로 보는데 W는 0,N-2까지, B는 w+1,N-1까지, R는 b+1,N까지!
열을 다 둘러봤을 때 다음 코드를 적으며 cnt를 세고! 다 더한 뒤 MIN값을 갱신!
'''
import sys
sys.stdin =open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    color = [list(input()) for _ in range(N)]
    cnt = 0#색을 바꾼 횟수를 담을 변수
    MIN = 987654321
    #하영's hint
    #for문으로 보는데 W는 0,N-2까지, B는 w+1,N-1까지, R는 b+1,N까지!
    #열을 다 둘러봤을 때 다음 코드를 적으며 cnt를 세고! 다 더한 뒤 MIN값을 갱신!
    w_cnt = 0 #하양
    for w in range(0,N-2):
        for j in range(M):
            if color[w][j] != 'W':
                w_cnt += 1
        b_cnt = 0 #파랑
        for b in range(w+1,N-1):
            for j in range(M):
                if color[b][j] != 'B':
                    b_cnt += 1
            r_cnt = 0 #빨강
            for r in range(b+1,N):
                for j in range(M):
                    if color[r][j] != 'R':
                        r_cnt += 1
            #여기서 cnt = 모든 색의 cnt를 더한 것!
            cnt = w_cnt + b_cnt + r_cnt
            if MIN > cnt:
                MIN = cnt
    print('#{} {}'.format(tc,MIN))
```

- 다른사람 코드

```python
#의수
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    temp = []

    # 각행의 색깔의 갯수를 카운트 하여 temp에 리스트 형태로 저장된다
    for i in range(N):
        w = arr[i].count('W')
        b = arr[i].count('B')
        r = arr[i].count('R')
        temp.append([w, b, r])

    # 가장 최소이동의 경우의 수를 맞춰야 하기 때문에 누적합을 이용한다
    # 원래의 상태
    # temp = [[3, 0, 2], [2, 2, 1], [3, 0, 2], [2, 1, 2]]
    # 아래 포문 후 상태
    # temp = [[3, 0, 2], [5, 2, 3], [8, 2, 5], [10, 3, 7]]
    # 즉, 맨 아래 행렬의 값인 [10, 3, 7] 이 의미하는 바는 국기에서 각각의 색이 가지고 있는 수의 합이다.
    # white = 10, blue = 3, red = 7 총 N * M = 20
    for i in range(1, N):
        temp[i][0] += temp[i - 1][0]
        temp[i][1] += temp[i - 1][1]
        temp[i][2] += temp[i - 1][2]

    # 첫번째 i, range 범위는 맨 윗쪽의 white의 색이기 때문에 아래 최소 2가지 색이 남을 수 있으니 N-2한다
    # 두번째 j, range 범위는 가운데 파랑색을 돌리는 것이라 최소 i(white)의 갯수+1 부터 최대 마지막 red 한줄을 남겨야 해서 N-1
    # 반복문을 돌리며 최소로 소모되는 이동을 구해야 하니 모든 경우의 수 탐색
    # res에 값에는 움직이지 안아도 될 ww, bb, rr의 갯수의 합의 최댓값이 저장된다
    # 출력할때 N * M - res 하면 이동해야 할 최솟값이 나온다!
    res = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            # 0 은 white, 1은 blue, 2는 red
            # temp엔 누적합이 저장되어 있다
            # 첫번째 ww는 그냥 그대로의 값을 받는다
            ww = temp[i][0]
            # bb는 j까지 누적된 합에서 i까지 누적된 합을 빼면 안움직여도 되는 갯수가 나온다
            bb = temp[j][1] - temp[i][1]
            # rr는 맨 마지막줄에 적혀있는 누적합에서 red의 j 값까지의 누적합을 배면 red에서 움직이지 않아야 하는 갯수가 나온다.
            rr = temp[N - 1][2] - temp[j][2]
            # 최댓값 res 저장 (전체에서 빼면 움직여야할 최솟값이 나오므로!)
            if res < ww + bb + rr:
                res = ww + bb + rr
    print('#{} {}'.format(tc, M * N - res))
```

- DFS

```python
#현우
# 가운데 애들은 일단 시작은 흰색 아니면 파란색.
# 근데 가운데 중 최소 한 줄은 파란색이어야 함.
# 파란색으로 칠했으면, 그담 부터는 파랑 아니면 빨강
# 빨강으로 칠했으면, 그담 부터는 무조건 빨강
# 따라서 파란색,빨간색 칠했음을 나타내는 표시가 있어야함
# 걔네를 DFS에 인자로 줌

# 해당 줄에서 그 색이 아닌애들 세는거
def count_not_color(i, color):
    not_color = 0
    for j in range(M):
        if board[i][j] != color:
            not_color += 1
    return not_color


def DFS(i, painted_blue, painted_red, cnt):
    if i == N - 1:
        # print(cnt,row_color)
        # 파란색 칠해져 있을 때만 답임
        if painted_blue:
            global ans
            if cnt < ans:
                ans = cnt
        return
    # i번째 줄을 칠한다.
    # 파랑 색 안칠했으면, 흰색,파랑색 칠 가능
    if not painted_blue:
        # 흰색 으로 칠함.
        not_white = count_not_color(i, 'W')
        # 다음 줄 칠하러 감
        row_color[i] = 'W'
        DFS(i + 1, False, False, cnt + not_white)
        # 파랑색으로 칠함
        row_color[i] = 'B'
        not_blue = count_not_color(i, 'B')

        DFS(i + 1, True, False, cnt + not_blue)
    # 파랑색 칠 했을 때
    else:
        # 빨강을 이미 칠한 경우 빨강만 칠 가능
        if painted_red:
            not_red = count_not_color(i, 'R')
            row_color[i] = 'R'
            DFS(i + 1, True, True, cnt + not_red)
        # 빨강을 안 칠한 경우 파랑,빨강 가능
        else:
            not_blue = count_not_color(i, 'B')
            row_color[i] = 'B'
            DFS(i + 1, True, False, cnt + not_blue)
            row_color[i] = 'R'
            not_red = count_not_color(i, 'R')
            DFS(i + 1, True, True, cnt + not_red)


T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    ans = 987654321
    board = []
    for _ in range(N):
        board.append(list(input()))
    cnt = 0
    row_color = ['' for i in range(N)]
    row_color[0], row_color[N - 1] = 'W', 'R'
    # 첫 한 줄은 무조건 흰색
    # 마지막 한 줄은 무조건 빨간색
    # 아닌 애들 cnt에 추가
    for j in range(M):
        if board[0][j] != 'W':
            cnt += 1
        if board[N - 1][j] != 'R':
            cnt += 1
    # print(cnt)
    DFS(1, False, False, cnt)
    print('#{} {}'.format(tc, ans))
```

- 

```python
#병훈
#W의 행 : w는  1부터 N-3까지 --> 바꿔야될 것의 합은 W[w]
#B의 행 : b는 w+1부터 N-2까지 --> 바꿔야될 것의 합은 B[b]-B[w]
#R의 행 : r는 b+1부터 N-1까지 --> 바꿔야될 것의 합은 R[M-1]-R[b]
 
for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    B=[M]*N;R=[M]*N;W=[M]*N
    for i in range(N):
        line = input()
        for color in line:
            if color == 'W':
                W[i]-=1
            elif color =='B':
                B[i]-=1
            else:
                R[i]-=1
        if i != 0:
            W[i]+=W[i-1]
            B[i]+=B[i-1]
            R[i]+=R[i-1]
    MIN = M*N
    for w in range(N-2):
        for b in range(w+1,N-1):
            change = W[w] + B[b]-B[w] + R[N-1]-R[b]
            if change < MIN:
                MIN = change
    print("#{} {}".format(t,MIN))
```



## SWEA_2918_격자판의 숫자 이어 붙이기

- 처음 DFS에서 recursionerror가 나옴 ->DFS가 종료조건에 들어가지 못함.
- 수를 str로 처음에 입력받고 DFS인자로 num(만들어진 수str)을 추가 인자로 만들어줘서 종료조건에서 이 num의 길이가 7이 되면 set에 담고 중복을 없애줌

```python
'''
4X4 크기 격자판
각 격 자판 0부처 9까지
동서남북 4방향으로 인접한 격자로 총 6번 이동
각 칸 숫자 차례로 이어붙이면 7자리
한번 거쳤던 격자칸 다시 거쳐도 됨
0으로 시작 가능
격자판 벗어나면 안됨
서로 다른 일곱자리 수 개수 구하기

음...DFS? -> RecursionError남
현우's hint
수를 입력받을떄 str로 받아라
DFS인자로 num을 주고 다음 num 은 num = num + arr[i][j]
if len(num)이 7이면 return
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,0,1,-1] #우좌하상
dj = [1,-1,0,0]
def DFS(i,j,num):
    global num_set
    #d 밑에다가 넣는다면 num이 계속 붙어버려서 밖에다 처음 등장햇을 떄! 처리해야됨
    num = num + arr[i][j]
    # print('i',i,'j',j,'num',num)
    if len(num) == 7:
        num_set.add(num)
        print(num_set)
        return
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= 4 or nj < 0 or nj >= 4:
            continue
        DFS(ni,nj,num)

T = int(input())
for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]
    # print(arr)
   
    num = ''
    num_set = set()

    for i in range(4):
        for j in range(4):
            DFS(i,j,num)
    # DFS(0,0,arr[0][0])
    print('#{} {}'.format(tc,len(num_set)))
```





## collections 모듈 - deque (데크)

[참고](https://excelsior-cjh.tistory.com/96)