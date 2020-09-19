# Baekjoon

## 1260_DFS와 BFS

```python
'''
정점 여러개인 경우 작은번호부터 방문, 더이상 방문 할 수 없으면 종료
정점번호는 1번부터 N번까지
정점 개수 N 간선개수 M 탐색 시작할 정점 V
M개의 줄 간선 연결하는 두 정점 번호 주어짐
간선 양방향
첫줄에 DFS수행 결과, 다음 줄 BFS수행 결과 방문 V부터 방문된 점을 순서대로 출력
'''
def DFS(v):
    visited[v] = True
    print(v,end = ' ')
    #해당정점의 인접리스트 보기!
    for i in arr[v]:
        if visited[i] == False:
            # print(i,end=' ')
            DFS(i)

def BFS(v):
    q=[]
    q.append(v)
    dist[v] = 1
    while q:
        top=q.pop(0)
        print(top,end= ' ')

        for i in arr[top]:
            if dist[i] == 0:
                # print('i',i)
                dist[i]=dist[top] +1
                q.append(i)






N,M,V = map(int,input().split())
#인접리스트
arr = [[]*(N+1) for _ in range(N+1)]
for m in range(M):
    st,ed = map(int,input().split())
    #양방향
    arr[st].append(ed)
    arr[ed].append(st)
for i in range(N+1):
    arr[i] = sorted(arr[i])
# print(arr)
visited = [False for _ in range(N+1)]
dist = [0 for _ in range(N+1)]
DFS(V)
print()
BFS(V)
```



## 2606_바이러스

```python
'''
연결되어 있는 컴퓨터 개수 구하기
dfs로 풀어보쟈
정점을 옮길때마다 +1
'''
def DFS(v):
    global num
    visited[v] = True
    for i in arr[v]:
        if visited[i] == False:
            num += 1
            DFS(i)
#컴퓨터수
N = int(input())
#컴퓨터 쌍
M=int(input())
arr = [[]*(N+1) for _ in range(N+1)]
for i in range(M):
    st,ed = map(int,input().split())
    arr[st].append(ed)
    arr[ed].append(st)
# print(arr)
num = 0
visited = [False for _ in range(N+1)]
DFS(1)
print(num)
```



## 1012_유기농 배추

> DFS로 푸니까 런타임 에러가 났고, BFS로 푸니까 성공!

```python
'''
배추1가 있는 뭉텅이에 배추흰지렁이 1마리 필요!
dfs, 델타 방문이용해서 몇 뭉텅이가 있는지!확인(상하좌우) => 런타임에러
bfs로 풀어보자....=>성공!
'''

di = [1,-1,0,0] #우좌하상
dj = [0,0,1,-1]
def DFS(i,j):
    visited[i][j] = True

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue
        if arr[ni][nj] == 0:
            continue
        if visited[ni][nj] == True:
            continue
        DFS(ni,nj)

def BFS(i,j):
    q = []
    q.append([i,j])
    while q:
        top = q.pop(0)
        pi,pj = top[0],top[1]
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if arr[ni][nj] == 0:
                continue
            if dist[ni][nj] != 0:
                continue
            dist[ni][nj] = dist[pi][pj] + 1
            q.append([ni,nj])
            
T = int(input())
for tc in range(1,T+1):
    #배추밭 가로M, 세로,N, 배추 심어진 위치 개수K
    M,N,K = map(int,input().split())
    arr = [[0]*(M) for _ in range(N)]
    for i in range(K):
        #x가 열 y가 행
        x,y = map(int,input().split())
        arr[y][x] = 1
    # from pprint import pprint
    # pprint(arr)
    visited = [[False for j in range(M)] for i in range(N)]
    dist = [[0 for j in range(M)] for i in range(N)]
    num = 0
    for i in range(N):
        for j in range(M):
            # if arr[i][j] == 1 and visited[i][j] == False:
            if arr[i][j] == 1 and dist[i][j] == 0:
                # print('i',i,'j',j)
                num += 1
                # DFS(i,j)
                BFS(i,j)
    print(num)
```



## 2178_미로탐색

> 최소거리는 무조건 BFS!!!!!
>
> 1,1이 start 지점일 경우 0으로 배열을 둘러싸주는 것이 범위 지정도 안해도 되고 편함!

```python
'''
미로는 1은 이동가능 0은 불가
(1,1)에서 출발->(N,M)의 위치로 이동할 때 지나야하는 최소의 칸수?
행,열 제일 앞에 0으로 채워서 인덱스 맞춰줌
서로 인접한 칸으로만 이동가능
최소의 칸수니까 BFS로 해야되지 않을까?->아몰라!!!!!DFS로 해본다....후
'''
di = [1,-1,0,0] #우좌하상
dj = [0,0,1,-1]
def DFS(i,j,dist):
    visited[i][j] = True
    dist += 1

    if i == N and j == M:
        #print(dist)
        return dist
    else:
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if ni <= 0 or ni >= N+1 or nj <= 0 or nj >= M+1:
                continue
            if arr[ni][nj] == 0:
                continue
            if visited[ni][nj] == True:
                continue
            DFS(ni,nj,dist)
def BFS(i,j):
    q=[[i,j]]
    while q:
        top = q.pop(0)
        pi,pj = top[0],top[1]
        if pi == N and pj == M:
            return dist[pi][pj] +1
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if arr[ni][nj] == 0:
                continue
            if dist[ni][nj] != 0:
                continue
            dist[ni][nj] = dist[pi][pj] + 1
            q.append([ni,nj])
    return -1


N,M = map(int,input().split())
temp=[list(input()) for _ in range(N)]
arr = [[0 for j in range(M+2)] for i in range(N+2)]
for i in range(1,N+1):
    for j in range(1,M+1):
        arr[i][j] = int(temp[i-1][j-1])
# from pprint import pprint
# pprint(arr)
visited = [[False for j in range(M+1)] for i in range(N+1)]
dist = [[0 for j in range(M+1)] for i in range(N+1)]
# DFS(1,1,0)
print(BFS(1,1))
```





## 7576_토마토

> `from collections import deque` 로 deque를 불러옴! 아니면 시간 초과 난다!
>
> pop은 `popleft`로 처리하면 됨!
>
> 일단 1인 것들을 deque에 넣고, BFS 인자로 q를 준다!
>
> 그리고 방문(dist) 하지 않았고, 그 값이 0으로 안익은 토마토가 있다면 -1을 출력하고, 그렇지 않다면 방문한 것 중 MAX인 dist값을 출력
>
> **오류가 났음! 이유는 배열의 값이 0이 아닐때 continue를 해야되는데 -1일 때 continue를 해서 처음부터 전부 익은토마토(1)가 있을 때도 dist가 +1됐음!

```python
'''
토마토 익는 것 최소 일수
BFS
익은 토마토 1 익지 않은 토마토 0 토마토가 없는 칸 -1
처음부터 토마토 모두 익어있으면 0
모두 익지 못하는 상황이면 -1
'''
from collections import deque
di = [1,-1,0,0]
dj = [0,0,1,-1]

def BFS(q):

    while q:
        top = q.popleft()
        pi,pj = top[0],top[1]
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if arr[ni][nj] != 0:
                continue
            if dist[ni][nj] != 0:
                continue
            dist[ni][nj] = dist[pi][pj] + 1
            q.append([ni,nj])

#M가로,N세로
M,N = map(int,input().split())
arr= [list(map(int,input().split())) for i in range(N)]
# print(arr)
ripen=deque()
dist = [[0 for j in range(M)] for i in range(N)]
# zero = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            ripen.append([i,j])
        # elif arr[i][j] == 0:
        #     zero += 1
# print(zero,ripen)
BFS(ripen)
#만약 dist가 방문 안했는데 arr이 0이면 -1을 뽑고, 아니라면 max를 뽑아라
flag = False
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and dist[i][j] == 0:
            flag = True
# print(max(dist))
if flag:
    print(-1)
else:
    MAX = 0
    for i in range(N):
        for j in range(M):
            if MAX < dist[i][j]:
                MAX = dist[i][j]
    print(MAX)
```







## 7569_토마토 3차원

> 3차원인데 그냥 배열 받을때, 델타 등 h만 추가로 주니까 값이 나왔다!
>
> 그런데 input으로 받으니 시간초과가 나와서
>
> `import sys`
>
> `sys.stdin.readline()`을 `input()`대신 쓰니까 시간 초과 안남

```python
'''
 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토
 토마토 익은거 1 안익은거 0 없는거 -1
 최소 일수 ->BFS
'''
from collections import deque
import sys
dh = [1,-1,0,0,0,0] #위,아래,왼쪽,오른쪽,앞,뒤
di = [0,0,0,0,-1,1]
dj = [0,0,-1,1,0,0]

def BFS(q):
    while q:
        top = q.popleft()
        ph,pi,pj = top[0],top[1],top[2]
        for d in range(6):
            nh = ph + dh[d]
            ni = pi +di[d]
            nj = pj + dj[d]
            if nh < 0 or nh >= H or ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if arr[nh][ni][nj] != 0:
                continue
            if dist[nh][ni][nj] != 0:
                continue
            q.append([nh,ni,nj])
            dist[nh][ni][nj] = dist[ph][pi][pj] +1
#가로 M 세로 N 높이 H
M,N,H = map(int,sys.stdin.readline().split())
#가장 밑의 상자부터 가장 위의 상자까지 저장된 토마토 정보 주어짐
#N개의 줄이 H번 반복
arr = [[list(map(int,sys.stdin.readline().split())) for i in range(N)] for h in range(H)]
# print(arr)
dist=[[[0 for j in range(M)] for i in range(N)] for h in range(H)]
ripen = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                ripen.append([h,i,j])
# print(ripen)
BFS(ripen)
#만약 dist가 방문 안했는데 arr이 0이면 -1을 뽑고, 아니라면 max를 뽑아라
flag = False
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 0 and dist[h][i][j] == 0:
                flag = True
    # print(max(dist))
if flag:
    print(-1)
else:
    MAX = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if MAX < dist[h][i][j]:
                    MAX = dist[h][i][j]
    print(MAX)
```



## 1691_숨바꼭질

> 하...이거 정말...ㅎ
>
> 어떻게 다를까

- 내코드

```python
'''
수빈이 N, 동생 K
수빈이 위치가 X, 걷는다면 1초후 X-1 or X+1, 순간이동 2*X
수빈이가 동생을 찾을 수 있는 가장 빠른 시간
최소시간이니까 BFS....?ㅠ 우째풀어.....하ㅏㅏ......ㅠ
'''
from collections import deque
def BFS(n):
    q = deque()
    q.append(n)
    while q:
        X = q.popleft()
        if X == K:
            return dist[K]
        a = X-1
        b = 2*X
        c = X+1
        if 0 <= a <MAX and dist[a] ==0:
            dist[a] = dist[X]+1
            q.append(a)
        if 0 <= b <MAX and dist[b] ==0:
            dist[b] = dist[X]+1
            q.append(b)
        if 0 <= c <MAX and dist[c] ==0:
            dist[c] = dist[X]+1
            q.append(c)

N,K = map(int,input().split())
# N,K=5,17
MAX = 100001
dist = [0 for _ in range(MAX)]
# print(BFS(N))
bfs()
```

- 답 코드

```python
from collections import deque
#답(다른사람꺼 내꺼랑 뭐가다를까)
def bfs():
    q = deque()
    q.append(N)
    while q:
        X = q.popleft()
        if X == K:
            print(dist[X])
            return
        for next in (X-1,X+1,X*2):
            if 0 <= next < MAX and not dist[next]:
                dist[next] = dist[X] + 1
                q.append(next)

N,K = map(int,input().split())
# N,K=5,17
MAX = 100001
dist = [0 for _ in range(MAX)]
bfs()
```

