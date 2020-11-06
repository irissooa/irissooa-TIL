## 삼성SW역량기출

[toc]

## BOJ_13458_시험감독

> [BOJ_13458_시험감독](https://www.acmicpc.net/problem/13458)

```python
#시험장 개수 N
N = int(input())
#각 시험장 응시자 수
students = list(map(int,input().split()))
#총 감독관 감시가능 수, 부감독관 감시가능 수
B,C = map(int,input().split())
cnt = 0
for i in range(N):
    students[i] -=B
    cnt += 1
# print(students)
for i in range(N):
    if students[i] > 0:
        if students[i]%C:
            cnt += students[i]//C +1
        else:
            cnt += students[i]//C
print(cnt)
```



## SWEA_1953_탈주범검거(BFS)

> [SWEA_1953_탈주범검거](https://swexpertacademy.com/main/solvingProblem/solvingProblem.do)
>
> 다음에는 범위가 주어졌으니 딕셔너리같은 곳에 담아서 한번에 불러오쟈...ㅎㅎ

```python
import sys
sys.stdin = open('input.txt','r')

di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def BFS(i,j):
    q = [(i,j)]
    dist[i][j] = 1
    while q:
        pi,pj = q.pop(0)
        if dist[pi][pj] >= L:
            return
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if not tunnel[ni][nj]:
                continue
            if dist[ni][nj]:
                continue
            #우, 현재 위치가 1,3,4,5가 아니거나 다음 위치가 1,3,6,7이 아니면 못감
            if d ==0 and (tunnel[pi][pj] not in [1,3,4,5] or tunnel[ni][nj] not in [1,3,6,7]):
                continue
            #하, 현재 위치가 1,2,5,6가 아니거나 다음 위치가 1,2,4,7이 아니면 못감
            if d==1 and (tunnel[pi][pj] not in [1,2,5,6] or tunnel[ni][nj] not in [1,2,4,7]):
                continue
            #좌,현재 위치가 1,3,6,7가 아니거나 다음 위치가 1,3,4,5이 아니면 못감
            if d == 2 and (tunnel[pi][pj] not in [1,3,6,7] or tunnel[ni][nj] not in [1,3,4,5]):
                continue
            #상,현재 위치가 1,2,4,7가 아니거나 다음 위치가 1,2,5,6이 아니면 못감
            if d==3 and (tunnel[pi][pj] not in [1,2,4,7] or tunnel[ni][nj] not in [1,2,5,6]):
                continue
            dist[ni][nj] = dist[pi][pj] + 1
            q.append((ni,nj))



T = int(input())
for tc in range(1,T+1):
    #세로N, 가로M, 맨홀뚜껑 위치한 장소 세로위치R,가로위치,탈출후 소요된시간 L
    N,M,R,C,L = map(int,input().split())
    #N줄 터널 지도 정보 M개의 숫자
    tunnel = [list(map(int,input().split())) for _ in range(N)]
    dist = [[0 for j in range(M)] for i in range(N)]
    BFS(R,C)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < dist[i][j] <= L:
                cnt+=1
    # from pprint import pprint
    # print('소요시간',L)
    # pprint(tunnel)
    # print('처음위치',R,C)
    # pprint(dist)
    print('#{} {}'.format(tc,cnt))

```

- 현우's code

```python
from collections import deque
from pprint import pprint
di = [0,0,1,-1] # 우,좌,하,상
dj = [1,-1,0,0]

go_dir = {1: [0,1,2,3], 2: [2,3], 3: [0,1], 4: [0,3],
          5: [0,2], 6: [1,2], 7: [1,3]}
next_pipe = {0: [1,3,6,7], 1: [1,3,4,5], 2: [1,2,4,7], 3: [1,2,5,6]}

T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dist = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append([R,C])
    dist[R][C] = 1
    ans = 0
    while q:
        pi,pj = q.popleft()
        pipe = arr[pi][pj]
        if dist[pi][pj] > L:
            break
        for d in go_dir[pipe]:
            ni,nj = pi+di[d], pj + dj[d]
            if ni < 0 or nj < 0 or ni >= N or nj >= M:
                continue
            if dist[ni][nj] != 0:
                continue
            if arr[ni][nj] in next_pipe[d]:
                dist[ni][nj] = dist[pi][pj]+1
                q.append([ni,nj])
    #print()
    #pprint(dist)
    for i in range(N):
        for j in range(M):
            if dist[i][j] == 0:
                continue
            if dist[i][j] <= L:
                ans += 1
    print('#{} {}'.format(tc,ans))
```



- 승범's code

```python
from collections import deque
def bfs():
    global cnt
    q = deque()
    q.append((R, C, 1, maps[R][C]))
    maps[R][C] = 0
    while len(q):
        r, c, l, info_num = q.popleft()
        if l == L + 1: return
        else: cnt += 1;
        for i in info[info_num]:
            rr, cc = r + dr[i], c + dc[i]
            if 0 <= rr < N and 0 <= cc < M:
                #(i+2)%4 -> 다음 파이프가 상일때는 하, 좌일때는 우니까 방향을 상좌하우로 해주고 모듈연산사용..
                if maps[rr][cc] != 0 and (i + 2) % 4 in info[maps[rr][cc]]:
                    q.append((rr, cc, l + 1, maps[rr][cc]))
                    maps[rr][cc] = 0
dr = [-1, 0, 1, 0] # 상좌하우
dc = [0, -1, 0, 1]
info = [0, [0, 1, 2, 3], [0, 2], [1, 3], [0, 3], [2, 3], [2, 1], [0, 1]]
for t in range(1, 1 + int(input())):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    bfs()
    print('#{} {}'.format(t, cnt))
```





## SWEA_1249_보급로(BFS)

```python
'''
출발지에서 도착지까지 가는 bfs만듦
도로가 파여진 깊이에 비례해서 복구시간 증가
가장짧은 경로!

'''
import sys
sys.stdin = open('input.txt','r')
from collections import deque

di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]
def BFS(i,j):
    q = deque()
    q.append([i,j])
    times[i][j] = 0
    while q:
        pi,pj = q.popleft()
        # print(pi,pj)
        if pi == N-1 and pj == N-1:
            continue
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            #  <= 에 '='을 붙이고 안붙이고 시간차이가 엄청 난당...
            if times[ni][nj] != -1 and times[ni][nj] <= times[pi][pj] + int(arr[ni][nj]):
                continue
            # print(int(arr[ni][nj]))
            times[ni][nj] = times[pi][pj] + int(arr[ni][nj])
            q.append([ni,nj])


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # for x in range(N):
    #     print(arr[x])
    times = [[-1 for j in range(N)] for i in range(N)]
    BFS(0,0)
    # print(times)
    print('#{} {}'.format(tc,times[N-1][N-1]))
```

