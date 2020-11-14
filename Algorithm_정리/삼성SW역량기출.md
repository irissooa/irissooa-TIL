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



## BOJ_14889_스타트와링크

> [BOJ_14889_스타트와링크](https://www.acmicpc.net/problem/14889)

```python
'''
14:11
조합 차 최소구하기
'''
import sys
input = sys.stdin.readline

def power(sel,ops):
    sans = 0
    lans = 0
    # print(sel,ops)
    for i in range(N//2):
        for j in range(N//2):
            if i != j:
                # print(sans,lans)
                sans += arr[sel[i]][sel[j]]
                lans += arr[ops[i]][ops[j]]
    return abs(sans-lans)


def comb(idx,sidx):
    global MIN
    if sidx == N//2:
        # print(steam)
        ops = []
        for i in range(N):
            if i not in steam:
                ops.append(i)
        ans = power(steam,ops)
        # print(ans)
        if ans < MIN:
            MIN = ans
        return
    if idx == N:
        return
    steam[sidx] = idx
    comb(idx+1,sidx+1)
    comb(idx+1,sidx)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
steam = [0]*(N//2)
MIN = 987654321
comb(0,0)
print(MIN)

```

- 다른 사람 코드

```python
import sys
from itertools import combinations as cb
N = int(sys.stdin.readline()) // 2
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
print(newstat)
allstat = sum(newstat) // 2

mins = 65535
for l in cb(newstat[:-1], N):
    mins = min(mins, abs(allstat - sum(l)))
print(mins)
```



## BOJ_20055_컨베이러벨트위의로봇

```python
'''
15:45
로봇이 어떤칸에 올라가거나 이동 -> 내구도 -1
내구도0 -> 로봇갈수 없음
N에 도착하면 로봇은 땅에 내려가야됨
#내구도가 0인것 개수가 K가 되면  stage를 print
#1단계
#arr원소들 한칸씩 미룸,  N번이되면 로봇내려감 오르고 이동하면 내구도-1
#로봇 한칸씩 이동할수있으면 이동 그 다음 장소가 0이거나 로봇이 있으면 안됨
#1번에 로봇이 없으면 올리고 내구도 -1,종료조건인지 확인
#종료조건이 아니라면 다시 단계반복, 몇번째 단계인지 확인
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def move(ans,robot,stage):
    global result
    while True:
        # ans = [0]*2*N
        # print('ans',ans)
        #arr원소를 한칸씩미룸
        # print('로봇이동전',robot)
        # print('벨트이동전',temp)
        # for i in range(2*N):
        #     ans[(i+1)%(2*N)] = temp[i]
        ans.insert(0,ans.pop())

        #로봇도 이동
        for i in range(N-1)[::-1]:
            if robot[i]:
                robot[i+1] = 1
                robot[i] = 0
        if robot[N-1]:
            robot[N-1] = 0
        # print('벨트이동후',ans)
        # print('벨트이동후로봇',robot)
        #로봇이 바뀐 배열이동가능한지 확인하고 1칸씩 이동시킴
        for i in range(N-1)[::-1]:
            if ans[i+1] > 0  and robot[i] and not robot[i+1]:
                robot[i] = 0
                robot[i+1] = 1
                ans[i+1] -=1
            if robot[N-1]:
                robot[N-1] = 0
        # print('로봇이동후',robot)
        # print('이동후벨트',ans)
        #첫번째가 올라갈수있고, 1번에 로봇이 없으면 올림 내구도-1
        if ans[0] and not robot[0]:
            ans[0] -= 1
            robot[0] = 1
            # print('로봇올라감',ans)
            # print('로봇올라감',robot)
        if robot[N-1]:
            robot[N-1] = 0
        cnt = 0
        #내구도 세어줌
        for i in range(2*N):
            if ans[i]<=0:
               cnt += 1
        if cnt >= K:
            result = stage
            return
        stage += 1
        # temp = ans[:]
        # print(stage,'다음단계',temp)




N,K = map(int,input().split())
arr = list(map(int,input().split()))
robotList = [0 for i in range(N)]
# robotList[0]=1
# print(arr)
result= 0
move(arr,robotList,1)
print(result)
```

- 현우's code

```python
N,K = map(int,input().split())
naegudos = list(map(int,input().split()))
robots = []
step = 1
# 0 올라가는 위치 N-1 내려가는 위치
while True:
    # 1. 벨트 한칸 회전
    naegudos.insert(0,naegudos.pop())
    for i in range(len(robots)):
        robots[i] = (robots[i]+1)%(2*N)
    # 내릴 로봇 있으면 내림
    if N-1 in robots:
        robots.remove(N-1)
    # 2. 로봇이 움직일 수 있으면 이동
    rbs = len(robots)
    for i in range(rbs):
        if (robots[i]+1)%(2*N) not in robots and naegudos[(robots[i]+1)%(2*N)] > 0:
            robots[i] = (robots[i]+1)%(2*N)
            naegudos[robots[i]] -= 1
    # 내릴 로봇 있으면 내림
    if N-1 in robots:
        robots.remove(N-1)
    # 로봇 올림
    if 0 not in robots and naegudos[0] > 0:
        robots.append(0)
        naegudos[0] -= 1
    if naegudos.count(0) >= K:
        break
    step += 1
print(step)
```





## BOJ_17142_연구소3

```python
'''
20:10 -> 22:05
0->빈칸
1->벽
2->바이러스위치

바이러스 위치를 받아서 start지점으로 두고, start에 넣어둠! + 빈칸 개수 세어둠
start 개수 중 M개를 조합으로 뽑음
그리고 bfs돌리고 모든 빈칸에 바이러스를 퍼뜨리면 최소시간 갱신!
모든 빈칸에 퍼뜨릴 수 없으면 -1 출력
'''
import sys
sys.stdin = open('input.txt','r')
from collections import deque
INF = sys.maxsize


def comb(idx):
    global MIN,order
    if sum(sel) > M:
        return
    if idx == S:
        if sum(sel) != M:
            return
        ans = 0
        for i in range(S):
            if sel[i]:
                order.append(start[i])
        # print(order)
        ans = BFS(order)
        if ans != -1 and MIN > ans:
            MIN = ans
        return
    sel[idx] = 1
    comb(idx+1)
    sel[idx] = 0
    comb(idx+1)

di = [-1,1,0,0] #상하좌우
dj = [0,0,-1,1]
def BFS(q):
    times = [[0 for j in range(N)] for i in range(N)]
    MAX = -INF
    cnt= 0
    for x in q:
        i,j = x
        times[i][j] = -1
    while q:
        pi,pj = q.popleft()
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            #범위벗어나면 지나감
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            #방문했으면지나감
            if times[ni][nj]:
                continue
            #벽이면 지나감
            if virus[ni][nj] == 1:
                continue
            #빈칸만 세어줌
            if virus[ni][nj] !=2:
                cnt+=1
            #시작점이기 때문에 지나감
            if times[ni][nj] == -1:
                continue
            #현재가 시작점이기 때문에 다음 값은 1
            if times[pi][pj] ==-1:
                times[ni][nj] = 1
            else:
                times[ni][nj] = times[pi][pj] + 1
            #빈칸들 중에서 MAX를 갱신
            if not virus[ni][nj] and MAX < times[ni][nj]:
                MAX = times[ni][nj]
            q.append([ni,nj])
    if cnt != zero:
        MAX = -1
    # for x in times:
    #     print(x)
    # print(MAX)
    return MAX

N,M = map(int,input().split())
virus = [list(map(int,input().split())) for _ in range(N)]
start = deque()
order = deque()
zero = 0
MIN = INF
# for x in virus:
#     print(x)
#시작점을 담아주고 0인 값을 센다
for i in range(N):
    for j in range(N):
        if virus[i][j] == 2:
            start.append([i,j])
        if not virus[i][j]:
            zero += 1
S = len(start)
sel = [0] * S
#zero가 0이라면 안해줘도 되니까 바로 0출력
if not zero:
    print(0)
else:
    #조합으로 start중에서 M개를 뽑아서 BFS돌려주고, times중 최댓값이 작은거 갱신! -> 빈칸이 다 안채워지면 -1 출력
    comb(0)
    if MIN == INF:
        print(-1)
    else:
        print(MIN)

```



## BOJ_14503_로봇청소기

> 힌트봄...ㅠ
>
> 복잡할때는 나눠서 해보자!
>
> 가지 못하는 경우 후진을 해야될때와 아닐때로 나눠서 작성하자
>
> 한번에 처리하려고 하면 꼬이게 됨.......ㅠ

```python
'''
22:15
청소기 방향 있음 동(우)서(좌)남(하)북(상)
지도 각 칸 (r(행),c(열))
1:벽 0:빈칸
로봇청소기 작동
1. 현재 위치 청소
2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색
2-1. 왼쪽 방향에 아직 청소하지 않은 곳 있으면 그 방향으로 회전, 한칸 전진, 1번 진행
2-2. 왼쪽 청소 공간 없으면 그방향 회전 후 2번
2-3. 네방향 모두 청소 돼있거나 벽, 바라보는 방향 유지, 한칸 후진, 2번 돌아감
2-4. 네방향 모두 청소, 벽, 뒤도 벽, 작동 멈춤

#그래도 이건 내가 생각했당....ㅠ
DFS(r,c,dir)로 돌리는데  (dir+3)%4의 순서로 본다! 상(0) -> 좌(3), 우(1) -> 상(0), 하(2)->우(1), 좌(3)->하(2)
현재 방향에 아직 청소하지 않은 곳이 있으면 (dir+3)%4로 방향전환, 1칸 가고, 그 방향의 또 (dir+3)%4로 이동(갈수있다면)
청소할 공간 없다! -> (dir+3)%4회전 후 다시 (dir+3)%4로 넘어감!
네방향 모두 청소할 공간이 없다! 현재 방향에서 뒤로 한칸! (dir+2)%4로 방향 전환!
네방향 모두 청소, 벽, 뒤도 벽, 작동 멈춤
'''
import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

di = [-1,0,1,0]#상우하좌
dj = [0,1,0,-1]
def DFS(i,j,dir,cnt):
    visited[i][j] = True
	#갈 곳이 없을 때 후진!
    if cnt == 4:
        #후진할 방향
        d = (dir+2)%4
        ni = i + di[d]
        nj = j + dj[d]
        #벽이면 못감
        if arr[ni][nj]:
            return
       	#벽이 아니라면 원래의 방향을 가지고 보냄
        else:
            DFS(ni, nj, dir,0)
    else:
        #현재 방향의 왼쪽먼저 살핌
        d = (dir + 3)%4
        ni = i + di[d]
        nj = j + dj[d]
        #앞으로 갈 곳이 갈수 있는 곳이라면 보냄
        if arr[ni][nj] == 0 and not visited[ni][nj]:
            DFS(ni,nj,d,0)
        #아니라면 cnt+1
        else:
            DFS(i,j,d,cnt+1)



#세로,가로
N,M = map(int,input().split())
#r,c좌표, 바라보는 방향 0:북(상), 1:동(우),2:남(하),3:서(좌)
r,c,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# print(r,c,d)
# for x in arr:
#     print(x)
visited = [[False for j in range(M)] for i in range(N)]
DFS(r,c,d,0)
ans = 0
# for x in visited:
#     print(x)
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            ans +=1
print(ans)
```

- 아래처럼 room(arr) 배열 자체에 방문처리를 하면 방문배열 안만들수도 됨!!!

```python
def DFS(R, C, D, fail):
    room[R][C] = '2'
    if fail == 4:
        nr = R + dr[(D+2)%4]
        nc = C + dc[(D+2)%4]
        if room[nr][nc] == 1:
            return
        else:
            DFS(nr, nc, D, 0)
    else:
        nr = R + dr[(D+3)%4]
        nc = C + dc[(D+3)%4]
        if room[nr][nc] == 0:
            DFS(nr, nc, (D+3)%4, 0)
        else:
            DFS(R, C, (D+3)%4, fail + 1)
```



## BOJ_17140_이차원배열과연산

```python
'''
23:00
R연산 : 배열의 모든 행에 대해서 정렬 수행, 행의 개수 >= 열의 개수일 때 적용
C연산 : 배열의 모든 열에 대해서 정렬 수행, 행의 개수 < 열의 개수인 경우 적용
각 수가 몇 번 나왔는지, 그 다음 등장 횟수가 커지는 순으로, 여러가지라면 수가 커지는 순으로 정렬 (수,등장횟수)
연산이 끝난 뒤, R ->가장큰행 기준, C->가장 큰 열 기준으로 0이 채워짐
수를 정렬할 떄는 0을 무시해야됨
행 또는 열의 크기가 100을 넘어가면 처음 100개를 제외하고는 버림
100초가 지나도 A[r][c]=k가 안되면 -1출력

1. R연산을 하는 함수 만들기
행의 개수가 열의 개수보다 같거나 클 때  한행당 열을 둘러보면서 (수,개수)를 나열하는데
등장횟수가 적은것부터 나열 만약 횟수가 같다면 수가 작은것부터! 그렇게 크기가 가장 큰 행을 기준으로 0을 붙임
(배열을 읽을때 0은 제외)
2. C연산을 하는 함수는 1과 마찬가지니까 배열을 돌리는 함수 만들기!(zip사용->그냥 함수도 만들어보기)
3. 연산을 계속하면서 행 또는 열의 크기가100을 넘어가면 100개 제외하고 버림
4. 100초가 지나기전까지 A[r][c] = k가 되는 최소값 찾기
'''
import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

#배열돌리는 함수
def rotate(arr):
    temp = [[0 for j in range(len(arr))] for i in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            temp[j][i] = arr[i][j]
    return temp

#연산함수
def calc(arr):
    result = []
    MAX_len= 0
    #수를 셈
    for i in range(len(arr)):
        cntNums = [0]*101
        l = 0
        for j in range(len(arr[i])):
            ans = arr[i][j]
            if ans:
                l += 1
                cntNums[ans] += 1
            if l >= 100:
                break
        temp = []
        for k in range(1,101):
            if cntNums[k]:
                temp.append((k,cntNums[k]))
        #적게나온 횟수로정렬, 같다면 수가 큰 순으로 정렬
        temp.sort(key = lambda x:(x[1],x[0]))
        # print(temp)
        #가장 긴것만큼 0을 붙여줘야돼서 수를 세어준다
        if MAX_len < len(temp)*2:
            MAX_len = len(temp)*2
        bin = []
        for i in range(len(temp)):
            bin.extend([temp[i][0],temp[i][1]])
        result.append(bin)
    #0을붙여줌
    # print(MAX_len)
    for i in range(len(result)):
        if len(result[i]) < MAX_len:
            result[i].extend([0]*(MAX_len-len(result[i])))
    # for x in result:
    #     print(x)
    # print('-----돌리기전')
    return result



# 왜 cnt를 return했는데 none값이 나오지??
#arr[r][c] = k값을 차는 함수
def find(arr,i,j,findnum):
    global time
    # print(cnt)
    #찾은지 100초가 넘어가면 끝냄
    if time > 100:
        time = -1
        return
    #행이 열보다 같거나 길다면 R연산, 아니라면 C연산(배열돌린뒤연산)
    if len(arr) >= len(arr[0]):
        result = calc(arr)
        time += 1
        # for x in result:
        #     print('r',x)
    else:
        result = rotate(calc(rotate(arr)))
        time+=1
        # for x in result:
        #     print('c',x)
    # print()
    if len(result) > i and len(result[0]) >j:
        if result[i][j] == findnum:
            return
    find(result,i,j,findnum)


r,c,k = map(int,input().split())
nums = [list(map(int,input().split())) for _ in range(3)]
# print('r',r-1,'c',c-1,k)
time=0
if r <= 3 and c <= 3:
    if nums[r-1][c-1] == k:
        print(0)
    else:
        ans = find(nums,r-1,c-1,k)
        print(time)
else:
    ans = find(nums,r-1,c-1,k)
    print(time)
```



- 다른사람 코드

```python
r,c,k = map(int,input().split())
r,c = r-1,c-1
matrix = [list(map(int,input().split())) for _ in range(3)]
result, row_len, col_len = -1, 3, 3

def r_cal(matrix,row_len,col_len):
	max_len = 0 
	length = []
	for y in range(row_len):
		dic = {}
		temp = list(matrix[y])
		for x in range(col_len):
			if temp[x] == 0:
				continue
			if temp[x] not in dic:
				dic[temp[x]] = 0
			dic[temp[x]] += 1
		sort = sorted(list(map(list,dic.items())),key = lambda x : (x[1],x[0]))
		sort = sum(sort,[])
		length.append(len(sort))
		max_len = max(max_len,len(sort))
		matrix[y] = sort
	for y in range(row_len):	
		matrix[y].extend((0,)*(max_len-length[y]))
	return max_len

for cnt in range(101):
	if r+1<=row_len and c+1<= col_len :
		if matrix[r][c] == k:
			result = cnt
			break
	if row_len >= col_len:
		col_len= r_cal(matrix,row_len,col_len)
	else:
		matrix = list(zip(*matrix))
		row_len = r_cal(matrix,col_len,row_len)
		matrix = list(zip(*matrix))
print(result)
```



## BOJ_20056_마법사상어와파이어볼

> 처음에는 temp초기화를 elif밑에다가 해줘서 만약 M이 0일때 continue가 되면 `temp[i][j]`가 초기화 되지 않아서 그대로 남아있다!!
>
> 각 기능별로 분리해서 짜자...ㅠㅠ 디버깅이 매우 힘들었음...ㅠ
>
> ```python
>             if len(temp[i][j])>=2:
>                 # print(i,j,temp[i][j])
>                 M,S=0,0
>                 odd=0
>                 for x in temp[i][j]:
>                     pd,ps,pm = x
>                     M += pm
>                     S += ps
>                     if pd % 2:
>                         odd += 1
>                 #질량
>                 M = M //5
>                 #M이 0이 되면 소멸
>                 if not M:
>                     continue
>                 #속력
>                 S = S// len(temp[i][j])
>                 #4방향으로 보내줌
>                 if odd == len(temp[i][j]) or odd ==0:
>                     D = [0,2,4,6]
>                 else:
>                     D = [1,3,5,7]
>                 for d in D:
>                     # print('변하고, 이동할좌표 i,j,d,S,M')
>                     # print(i,j,d,S,M)
>                     next.append([i,j,d,S,M])
>             #공이 한개만 있을때 한번 더 그 방향과 속력,질량을 갖고 보내기
>             elif temp[i][j]:
>                 # print(temp[i][j])
>                 for x in temp[i][j]:
>                     pd,ps,pm = x
>                     # print('그냥 이동할좌표 i,j,d,S,M')
>                     # print(i,j,pd,ps,pm)
>                     next.append([i,j,pd,ps,pm])
>             #초기화
>             temp[i][j] = []
> ```
>
> 

```python
'''
00:10
NxN 파이어볼 M개 r행 x열 질량 m, 방향 d, 속력 s
8방향 이동 상,우상,우,우하,하,좌하,좌,좌상
1. 모든 파이어볼 자신의 방향 d로 속력 s칸만큼 이동(이동하는 중, 같은칸 여러개의 파이어볼 있을 수 있음)
이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있다면,
2. 같은 칸에 있는 파이어볼은 하나로 합쳐짐
3. 파이어볼은 4개의 파이어볼로 나누어짐
4. 나누어진 파이어볼의 질량, 속력, 방향
4-1. 질량은 [(합쳐진 파이어볼 질량의 합)/5]
4-2 속력은 [(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)]
속력 %N번 하면 최소 움직이는횟수가 나오고 만약 범위를 벗어나면 +N(왼쪽방향), -N(오른쪽방향)을 해주면 됨!
4-3 합쳐지는 파이어볼의 방향이 모두 홀수, 모두 짝수, 방향은 0,2,4,6이 됨,
그렇지 않으면 1,3,5,7이 됨
5. 질량이 0인 파이어볼은 소멸
마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합!

1. 배열에 놓고 각 방향으로 질량을 가지고, 속력 개수만큼 이동!
ni = r-1 + di[d]
nj = c-1 + dj[d]
2.이동이 끝난뒤 2개이상의 파이어볼이 같은 위치에 있다면 하나로 합쳐지고, 질량, 속력, 방향을 구함
3. 그런뒤에 4방향으로 이동시킴 - 이과정을 K번 반복한 뒤 남아있는 파이어볼 질량의 합! 구하기(질량0-소멸)
'''
import sys
sys.stdin= open('input.txt','r')
sys.setrecursionlimit(10**8)
from collections import deque
input = sys.stdin.readline
di = [-1,-1,0,1,1,1,0,-1] #상(0),우상(1),우(2),우하(3),하(4),좌하(5),좌(6),좌상(7)
dj = [0,1,1,1,0,-1,-1,-1]
#공위치시키기
def position(q):
    global cnt
    cnt += 1
    # print(cnt)
    while q:
        pi,pj,pd,ps,pm = q.popleft()
        # print('-현위치-i,j,pd,ps,pm-')
        # print(pi,pj,pd,ps,pm)
        ni = (pi + di[pd] * ps) % N
        nj = (pj + dj[pd] * ps) % N
        # print('-이동후-ni,nj,pd,ps,pm-')
        # print(ni,nj,pd,ps,pm)
        arr[ni][nj].append([pd,ps,pm])
    # for x in arr:
    #     print(x)
    move(arr)

#공움직이기
def move(temp):
    global cnt,ans
    next = deque()
    # print('움직여라')
    # for x in temp:
    #     print(x)
    for i in range(N):
        for j in range(N):
            if not temp[i][j]:
                continue
            #공이 두개이상 만났을떼 질량, 속력,방향 바꾸고 next에 담아주기
            ''''
            4-1. 질량은 [(합쳐진 파이어볼 질량의 합)/5]
            4-2 속력은 [(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)]
            4-3 합쳐지는 파이어볼의 방향이 모두 홀수, 모두 짝수, 방향은 0,2,4,6이 됨,
            그렇지 않으면 1,3,5,7이 됨
            '''
            if len(temp[i][j])>=2:
                # print(i,j,temp[i][j])
                M,S,flag,D=0,0,0,[]
                odd=0
                for x in temp[i][j]:
                    pd,ps,pm = x
                    M += pm
                    S += ps
                    if pd % 2:
                        odd += 1
                    # if flag == 3:
                    #     continue
                    # #방향이홀수
                    # if pd % 2 and flag !=2:
                    #     D = [0,2,4,6]
                    #     flag = 1
                    # #방향이 짝수
                    # elif not pd % 2 and flag !=1:
                    #     D = [0,2,4,6]
                    #     flag =2
                    # #홀수 짝수가 같이 있음
                    # else:
                    #     flag = 3
                    #     D = [1,3,5,7]
                #질량
                M = M //5
                #M이 0이 되면 소멸
                if not M:
                    continue
                #속력
                S = S// len(temp[i][j])
                #4방향으로 보내줌
                if odd == len(temp[i][j]) or odd ==0:
                    D = [0,2,4,6]
                else:
                    D = [1,3,5,7]
                for d in D:
                    # print('변하고, 이동할좌표 i,j,d,S,M')
                    # print(i,j,d,S,M)
                    next.append([i,j,d,S,M])
            #공이 한개만 있을때 한번 더 그 방향과 속력,질량을 갖고 보내기
            elif temp[i][j]:
                # print(temp[i][j])
                for x in temp[i][j]:
                    pd,ps,pm = x
                    # print('그냥 이동할좌표 i,j,d,S,M')
                    # print(i,j,pd,ps,pm)
                    next.append([i,j,pd,ps,pm])
    for i in range(N):
        for j in range(N):
            temp[i][j] = []
    # print('이동할 좌표')
    # for x in next:
    #     print(x)
    if cnt ==K:
        if not next:
            return
        for x in next:
            # print(x)
            ans += x[-1]
            # print(ans)
        return
    else:
        position(next)


N,M,K = map(int,input().split())
arr = [[[] for j in range(N)] for i in range(N)]
#r-1,c-1,m,s,d
cnt = 0
ans = 0
fireball= deque()
for i in range(M):
    r,c,m,s,d = map(int,input().split())
    fireball.append([r-1,c-1,d,s,m])
position(fireball)
# for x in arr:
#     print(x)
print(ans)
```

- 현우's code

```python
di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

N,M,K = map(int,input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    board[r-1][c-1].append([m,s,d])

for _ in range(K):
    temp = [[[] for _ in range(N)] for _ in range(N)]
    # 파이어볼 이동
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                while board[i][j]:
                    m,s,d = board[i][j].pop()
                    ni,nj = (i+s*di[d])%N,(j+s*dj[d])%N
                    temp[ni][nj].append([m,s,d])
    # 파이어볼 합치기
    for i in range(N):
        for j in range(N):
            if len(temp[i][j]) >= 2:
                tot_cnt = len(temp[i][j])
                total_m = 0
                total_s = 0
                holsu_cnt = 0
                while temp[i][j]:
                    m,s,d = temp[i][j].pop()
                    total_m += m
                    total_s += s
                    if d % 2 == 1:
                        holsu_cnt += 1
                total_m = total_m//5
                total_s = total_s//tot_cnt
                if total_m > 0:
                    if holsu_cnt == tot_cnt or holsu_cnt == 0:
                        for k in [0,2,4,6]:
                            temp[i][j].append([total_m,total_s,k])
                    else:
                        for k in [1,3,5,7]:
                            temp[i][j].append([total_m, total_s, k])
    for i in range(N):
        for j in range(N):
            board[i][j] = temp[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            for each in board[i][j]:
                ans += each[0]
print(ans)
```

