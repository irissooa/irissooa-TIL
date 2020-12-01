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

- 다른사람 코드

```python
def clean(r,c,d):
    if visited[r][c] == 0:
        visited[r][c] = 1
    cnt = 1
    while True:
        for i in range(1,5):
            tmp_d = (d-i) % 4
            dr = r + d_row[tmp_d]
            dc = c + d_col[tmp_d]
            if visited[dr][dc]==0 and area[dr][dc] == 0:
                visited[dr][dc] = 1
                r = dr
                c = dc
                d = tmp_d
                cnt += 1
                break
        else:
            tmp_d = (d-2) % 4
            r += d_row[tmp_d]
            c += d_col[tmp_d]
            if area[r][c] == 1:
                return cnt

d_row = [-1,0,1,0]
d_col = [0,1,0,-1]
N,M = map(int,input().split())
r,c,d = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
print(clean(r,c,d))
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

- 반복문으로 풀어보기

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

- 다른 사람 코드

```python
chkbit = 0b111111
D = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]

N, M, K = map(int, input().split())
pl = [list(map(int, input().split())) for _ in range(M)]


while K and len(pl) > 1:
    K -= 1
    tpl = []
    temp_postion = dict()
    for planet in pl:
        y, x, m, s, d = planet
        tx, ty = (x + D[d][0] * s) % N, (y + D[d][1] * s) % N
        position = (tx << 6) + ty
        planet[0] = ty
        planet[1] = tx
        if temp_postion.get(position):
            temp_postion[position].append(planet)
        else:
            temp_postion[position] = [planet]
    for k, v in temp_postion.items():
        if len(v) == 1:
            tpl.append(v[0])
        else:
            x = k >> 6
            y = k & chkbit
            chk_value = v[0][4] & 1
            chk = False
            temp_mass = 0
            temp_speed = 0
            for planet in v:
                temp_mass += planet[2]
                temp_speed += planet[3]
                if planet[4] & 1 != chk_value:
                    chk = True
            temp_mass //= 5
            temp_speed //= len(v)
            if temp_mass:
                if not chk:
                    tpl.append([y, x, temp_mass, temp_speed, 0])
                    tpl.append([y, x, temp_mass, temp_speed, 2])
                    tpl.append([y, x, temp_mass, temp_speed, 4])
                    tpl.append([y, x, temp_mass, temp_speed, 6])
                else:
                    tpl.append([y, x, temp_mass, temp_speed, 1])
                    tpl.append([y, x, temp_mass, temp_speed, 3])
                    tpl.append([y, x, temp_mass, temp_speed, 5])
                    tpl.append([y, x, temp_mass, temp_speed, 7])
    pl = tpl
result = 0
for planet in pl:
    result += planet[2]

print(result)
```





## BOJ_14888_연산자끼워넣기

```python
'''
N개의 수 N-1연산자 더하기 빼기 곱하기 나누기로 주어짐
순서대로 수를 계산하고, 음수나누기는 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꿈
나올수 있는 수들의 최대 최소 값을 구함

1. 연산자들을 보면서 0이 아닌 수 들 중 빼면서 순열!을 구함
2. 계산하는 함수를 만들어서 계산한 뒤, 최대 최소 값을 구함
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
INF = sys.maxsize

#계산하는 함수
def calc(opr):
    ans = numbers[0]
    # print(opr,'연산자')
    for s in range(N-1):
        o_idx = opr[s]
        if o_idx == 0:
            ans += numbers[s+1]
        elif o_idx == 1:
            ans -= numbers[s+1]
        elif o_idx== 2:
            ans *= numbers[s+1]
        else:
            if ans >= 0:
                ans //= numbers[s+1]
            else:
                ans = -(abs(ans)//numbers[s+1])
        # print(numbers[s],ans)
    return ans

#순열
def perm(idx):
    global MAX,MIN
    if idx == N-1:
        ans = calc(sel)
        if MAX < ans:
            MAX = ans
        if MIN > ans:
            MIN = ans
        return
    for o in range(4):
        if operators[o]:
            sel[idx] = o
            operators[o] -= 1
            perm(idx+1)
            operators[o] += 1
            sel[idx] =0




N = int(input())
numbers = list(map(int,input().split()))
# + - * //
operators = list(map(int,input().split()))
# print('연산자',operators)
sel = [0]*(N-1)
MAX,MIN = -INF,INF
perm(0)
print(MAX)
print(MIN)
```



## BOJ_14502_연구소

```python
'''
NxM연구소 바이러스 상하좌우로 퍼져나감, 새로 세울수 있는 벽 3개!
0은 빈칸, 1은 벽, 2는 바이러스
바이러스가 퍼질 수 없는 곳, 안전영역! 그 크기가 최대인 것을 구해라
완전탐색...0인것들 중 3곳씩만 1로 바꾼뒤 바이러스가 얼마나 퍼지는지 bfs돌리고, 0인곳 세기! 최댓값 갱신
'''
import sys
from collections import deque
import copy
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

#조합!
def comb(idx,sidx):
    if sidx == 3:
        wall = []
        for s in sel:
            wall.append([bin[s][0],bin[s][1]])
        temp = copy.deepcopy(start)
        BFS(temp,wall)
        return
    if idx == len(bin):
        return
    sel[sidx] = idx
    comb(idx+1,sidx+1)
    sel[sidx] = 0
    comb(idx+1,sidx)

di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]
def BFS(q,sel):
    global MAX
    visited = [[False for j in range(M)] for i in range(N)]
    #처음시작점 방문처리
    for v in q:
        i,j = v
        visited[i][j] = True
    #조합으로 뽑은 수 방문 처리(벽이 됐기 때문)
    for s in sel:
        i,j = s
        visited[i][j] = True
    # print(sel,q)
    cnt = zero
    while q:
        if cnt <=MAX:
            break
        pi,pj = q.popleft()
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if visited[ni][nj]:
                continue
            if laboratory[ni][nj] == 1:
                continue
            if not visited[ni][nj] and not laboratory[ni][nj]:
                cnt+=1
            if cnt <= MAX:
                break
            # print(ni,nj)
            visited[ni][nj] = True
            q.append([ni,nj])
    # print('여기안오니')
    ans = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and not laboratory[i][j]:
                # print(ans,'여긴!!!!')
                ans += 1
    # for x in visited:
    #     print(x)

    if MAX < ans:
        MAX = ans
    return

N,M = map(int,input().split())
laboratory = [list(map(int,input().split())) for _ in range(N)]
start = deque()
bin = deque()
MAX = 0
#0인곳과, start(바이러스가 있는곳)위치 담기
for i in range(N):
    for j in range(M):
        if laboratory[i][j] == 2:
            start.append([i,j])
        if laboratory[i][j] == 0:
            bin.append([i,j])
zero = len(bin)-3
sel = [0]*3
comb(0,0)
print(MAX)
```

- 다른 사람 코드

```python
N,M = map(int,input().split())
matrix = []
#벽으로 둘러쌈
for i in range(N+2):
    if i == 0 or i == N+1:
        a = []
        for i in range(M+2):
            a.append(1)
        matrix.append(a)
    else:
        matrix.append([1]+list(map(int, input().split()))+[1])


zero = []
virus = []

def build_wall(r1,r2,r3,c1,c2,c3,m): # 리스트는 call by reference
    a = m[:]
    a[r1],a[r2],a[r3] = a[r1][:],a[r2][:],a[r3][:]
    a[r1][c1],a[r2][c2],a[r3][c3] = 1,1,1
    return a

#상하좌우로 바이러스로 전염됨
def search(r, c, mat):
    if r > N or c > M:
        return
    
    if mat[r][c+1] == 0:
        mat[r][c+1] = 2
        search(r,c+1,mat)
    
    if mat[r+1][c] == 0:
        mat[r+1][c] = 2
        search(r+1,c,mat)
        
    if mat[r-1][c] == 0:
        mat[r-1][c] = 2
        search(r-1,c,mat)
        
    if mat[r][c-1] ==0:
        mat[r][c-1] = 2
        search(r,c-1,mat)


# zero위치 및 virus위치탐지
for i in range(N+1):
    for j in range(M+1):
        if matrix[i][j]==0:
            zero.append((i,j))
        if matrix[i][j]==2:
            virus.append((i,j))

count = []
for i in range(len(zero)):
    for j in range(len(zero)-1-i):
        for k in range(len(zero)-2-j-i):
            #zero를 전부 돌면서 3개만 벽으로 바꿈!
            r1,c1 = zero[i][0],zero[i][1]
            r2,c2 = zero[j+i+1][0],zero[j+i+1][1]
            r3,c3 = zero[k+j+i+2][0],zero[k+j+i+2][1]
            
            a = build_wall(r1,r2,r3,c1,c2,c3,matrix)
            
            copy_a = a[:]
            for row in range(len(copy_a)):
                copy_a[row] = copy_a[row][:]

            for l in range(len(virus)): # 바이러스 위치
                r, c = virus[l][0],virus[l][1]                
                search(r,c,copy_a)
            count_zero = 0
            
            for cnt in range(len(copy_a)):
                count_zero += copy_a[cnt].count(0)
            count.append(count_zero)
print(max(count))
```

- 다른사람코드

```python
from collections import deque

n, m = map(int, input().split())
world = []
virus = []
safe_cnt = 0
for i in range(n):
    row = list(map(int, input().split()))
    world.extend(row)
    for j, v in enumerate(row):
        if v == 2:
            virus.append(i * m + j)
        elif v == 0:
            safe_cnt += 1


def spread_cnt(world, n, m, virus, safe_cnt):
    q = deque(virus)
    while q:
        now = q.popleft()
        if now - m >= 0 and world[now - m] == 0:
            world[now - m] = 2
            q.append(now - m)
            safe_cnt -= 1
        if now + m < n * m and world[now + m] == 0:
            world[now + m] = 2
            q.append(now + m)
            safe_cnt -= 1
        if now % m != 0 and world[now - 1] == 0:
            world[now - 1] = 2
            q.append(now - 1)
            safe_cnt -= 1
        if now % m + 1 != m and world[now + 1] == 0:
            world[now + 1] = 2
            q.append(now + 1)
            safe_cnt -= 1
    return safe_cnt


answer = 0

for i1 in range(n * m):
    if world[i1] == 0:
        world[i1] = 1
        for i2 in range(i1 + 1, n * m):
            if world[i2] == 0:
                world[i2] = 1
                for i3 in range(i2 + 1, n * m):
                    if world[i3] == 0:
                        world[i3] = 1
                        answer = max(answer, spread_cnt(world[:], n, m, virus, safe_cnt - 3))
                        world[i3] = 0
                world[i2] = 0
        world[i1] = 0

print(answer)
```



## BOJ_15686_치킨배달

> 답은 맞다고 나오는데....시간초과...ㅠㅠ 시간을 어떻게 줄일까.......ㅎㅎ
>
> 근데...반례도 틀림,,,,,,뭐가 틀렸지,,,ㅠ 다시 고민해보자....
>
> 하...엄청...멍청한 실수를 했다.... 치킨집은 1이아니고 2,,집은 1.............!!!!!!!!!!!

```python
'''
2020-11-28 21:07
NxN인 도시,각 칸 빈칸(0), 치킨집(2), 집(1) 중 하나
r행 c열 1부터 시작
치킨거리 = 집과 가장 가까운 치킨집 사이의 거리(|r1-r2|+|c1-c2|)
도시의 치킨거리는 모든 집의 치킨 거리의 합
M개의 치킨집만 고르고 나머지 치킨집 없애야 됨
어떻게 고르면 도시의 치킨 거리가 가장 작게 될까
출발점인 2를 전부 start에 담는다,
1인 점을 담고, 조합으로 3개의 좌표를 뽑는다
start와 store의 조합을 구한뒤 각각의 거리들을 구하고, 최소값을 뽑자!!!
'''

import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline


def comb(idx):
    global cnt,MIN
    # print(cnt,sel)
    temp = 0
    if cnt == M:
        # print(sel)
        # visited = [0]*len(store)
        for s in range(len(start)):
            # print('--MIN---',MIN)
            minans = sys.maxsize

            for e in range(len(store)):
                if sel[e]:
                    si,sj = start[s]
                    ei,ej = store[e]
                    ans = abs(si-ei) + abs(sj-ej)
                    if minans > ans:
                        minans = ans
                    # print(s,e,ans,minans,temp)
            temp += minans
            if temp > MIN:
                return
        if MIN > temp:
            MIN = temp
        return
    if idx == len(store):
        return
    sel[idx] = store[idx]
    cnt += 1
    comb(idx+1)
    sel[idx] = 0
    cnt -=1
    comb(idx+1)



N, M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
start,store = deque(),deque()
for i in range(N):
    for j in range(N):
        #집
        if city[i][j] == 1:
            start.append([i+1,j+1])
        #치킨집
        if city[i][j] == 2:
            store.append([i+1,j+1])
# print('start',start)
# print(N,M,'store',store)
# for x in city:
#     print(x)
sel = [0]*len(store)
cnt = 0 #몇개뽑았는지 세어줌
MIN = sys.maxsize
# visit = [0]*len(store)
comb(0)
print(MIN)
```



## BOJ_3190_뱀

```python
'''
2020-11-30 15:30-16:20
NxN 몇칸 사과, 상하좌우 끝에 벽이 있음
뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
뱀 맨위,맨좌측에서 위치, 길이는 1, 처음에 오른쪽을 향함
뱀이동규칙
1. 몸 길이를 늘려 머리를 다음 칸에 위치시킴
2. 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
3. 만약 이동한 칸에 사과가 없다면, 몸 길이를 줄여서 꼬리가 위치한 칸을 비워줌
즉, 몸길이는 변하지 않음,
사과의 위치와 뱀의 이동경로가 주어질때 이 게임이 몇초에 끝나는지 계산

방향은 오른쪽부터! dir을 처음부터 pop해서  X를 -1씩 줄여나가며 0이됐을때 방향이 L(왼쪽)인지 D(오른쪽)인지 확인한 뒤 90도
우 -> L:상,D:하
하 -> L:우, D:좌
좌 -> L:하, D:상
상 -> L:좌,D:우
L 은 (d+3)%4, D는 (d+1)%4방향을 확인하면됨!!

뱀이 처음부터 이동할때 다음칸을 볼때 사과가 있으면 그 사과(2)를 0으로 바꾸고 뱀이 위치한 좌표 표시하며 계속하면서 움직임,
만약에 사과가 없다면 제일끝 뱀좌표pop함
만약 1인 백에 닿거나 자기몸에 부딪히면 게임 끝, 초 세어주기
'''

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque
di =[0,1,0,-1] #우하좌상
dj = [1,0,-1,0]
def snake(i,j):
    global time
    visited.append([i,j])
    pi,pj,d = i,j,0
    px,pd = dir.popleft()
    while True:
        ni = pi + di[d]
        nj = pj + dj[d]
        # print('ni,nj',ni,nj,visited)
        # print('px,pd,time',px,pd,time)
        time +=1
        if arr[ni][nj] == 1 or [ni,nj] in visited:
            return
        if arr[ni][nj] == 0:
            visited.popleft()
            visited.append([ni,nj])
        if arr[ni][nj] == 2:
            arr[ni][nj] = 0
            visited.append([ni,nj])
        pi,pj = ni,nj
        if px == time:
            if pd == 'L':
                d = (d+3)%4
            else:
                d = (d+1)%4
            if dir:
                px,pd = dir.popleft()



N = int(input())
# 1로 둘러싸서 벽을 만듦
arr = [[1]+[0 for j in range(N)]+[1] for i in range(N)]
arr.insert(0,[1]*(N+2))
arr.insert(N+1,[1]*(N+2))
#사과개수
K = int(input())
#사과 위치, 정수행, 정수열 1행1열부터 시작(여긴 사과없음)
for k in range(K):
    r,c = map(int,input().split())
    arr[r][c] = 2
# for x in arr:
#     print(x)
#뱀의 방향 변환 횟수
dir = deque()
L = int(input())
for l in range(L):
    #정수  X, 문자  C
    X,C = input().split()
    # 게임시작시간으로부터 X초가 끝난 뒤 왼쪽 'L'또는 오른쪽'D'로 90도 회전시킨다는 뜻
    dir.append([int(X),C])
visited = deque()
time = 0
snake(1,1)
print(time)
```



## BOJ_15683_감시

> 하나하나 완전탐색해야될거같은데......복잡하다...이따 다시풀어야지ㅠ

```python
'''
2020-11-30 16:25
CCTV종류
1: 한 방향
2: 서로 반대 두 방향(상하,좌우)
3: 90도 두방향(우하,좌상,우상,좌하)
4: 세방향(한개제외)
5: 네 방향
cctv는 회전가능(대각선만안되면 됨)
벽(6)은 통과할수없지만 cctv는 통과가능
감시할 수 없는 사각지대가 최소인 크기를 구해라
dfs를 돌릴건데
각 cctv좌표가 갈수 있는 범위 까지 cnt를 세고 상하좌우 모두 돌려서 cnt센뒤 list에 담아주고
cctv번호에 따라 개수를 합해서 세어준뒤 제일 많은 cnt를 total에 더함
이걸 반복해서 전체 0의 수에서 빼줌

카메라가 큰번호부터 방문처리를 하는게 좋겠다
딕셔너리? 카메라번호 key : [각 d별 [cnt,방문한좌표]]
근데 딕셔너리로 했을 떄....중복되는 카메라 처리..해야돼서 다시 생각해보자
'''
import sys
input = sys.stdin.readline

di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]

def cctv(i,j,num):
    pi,pj,d = i,j,0
    cnt = 0
    cntList = []
    visitList = [[] for _ in range(4)]
    while d<4:
        ni = pi + di[d]
        nj = pj + dj[d]
        # print(ni,nj)
        if office[ni][nj] == 6:
            cntList.append(cnt)
            pi,pj = i,j
            d+=1
            cnt = 0
            continue
        if not visited[ni][nj] and not office[ni][nj]:
            cnt += 1
            visitList[d].append([ni,nj])
        pi,pj = ni,nj
    # 겹치는 곳..표시하기
    # print(cntList)
    # print(visitList)
    if num == 1:
        total = [cntList.index(max(cntList))]

    elif num == 2:
        ans1 = sum(cntList[:2])
        ans2 = sum(cntList[2:])
        if ans1 > ans2:
            total = [0,1]
        else:
            total = [2,3]

    elif num == 3:
        total = []
        if cntList[0] > cntList[2]:
            total.append(0)
            if cntList[1] > cntList[3]:
                total.append(1)
            else:
                total.append(3)
        else:
            total.append(2)

    elif num == 4:
        total = []
        for i in range(4):
            if i != cntList.index(min(cntList)):
                total.append(i)
    else:
        total = [0,1,2,3]
    # print(cntList,num,total)
    for i in range(len(total)):
        for j in range(len(visitList[total[i]])):
            vi, vj = visitList[total[i]][j]
            visited[vi][vj] = True
    return

N,M = map(int,input().split())
# 벽 만듦
office = [[6]+list(map(int,input().split()))+[6] for _ in range(N)]
office.insert(0,[6]*(M+2))
office.insert(N+1,[6]*(M+2))

zero = 0
visited = [[False for j in range(M+2)] for i in range(N+2)]
# for x in office:
#     print(x)
cctvList = []
for i in range(1,N+1):
    for j in range(1,M+1):
        if office[i][j] == 0:
            zero += 1
        if office[i][j] != 0 and office[i][j] !=6:
            cctvList.append([office[i][j],i,j])
cctvList.sort(key=lambda x:-x[0])
# print(cctvList)
for x in cctvList:
    cctv(x[1],x[2],x[0])
# for x in visited:
#     print(x)
ans = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if visited[i][j]:
            ans += 1
print(zero-ans)
```



- 다른사람 코드

> **알고리즘 분류 : 브루트 포스** 
>
> 
>
> 5종류의 CCTV를 키고 끄면서, CCTV가 감시할 수 없는 영역인 사각지대의 최소 크기를 맞추는 문제다. 최대 8개의 CCTV가 주어지고, 각 CCTV는 일정한 방향성을 가지고 있다. CCTV는 90도로 회전하며 사용할 수 있고, 이에 따라서 감시 영역이 바뀐다. 이 문제는 N이 최대 8이기 때문에, 모든 경우의 수를 구해서 최소 크기를 구하면 된다.
>
> 
>
> ![img](삼성SW역량기출.assets/994E0D4E5C44AD6803)
>
> 
>
> - CCTV 1~5번에 해당하는 방향을 만든다. 아래 코드에서는 비트 연산을 통해 만들었다.
> - 위쪽 방향 : 0001 == 1<<0 (인덱스 0)
> - 오른쪽 방향 : 0010 == 1<<1 (인덱스 1)
> - 아래쪽 방향 : 0100 == 1<<2 (인덱스 2)
> - 왼쪽 방향 : 1000 == 1<<3 (인덱스 3)
> - 위 4가지를 정하고, OR 연산을 통해 각 CCTV의 방향성을 정했다.
> - DFS 방식으로 CCTV의 개수만큼 깊이 탐색을 시작한다.
> - 각 CCTV를 키고 끄는 방식으로 모든 경우의 수를 구한다.
> - CCTV를 키면 해당 CCTV에 대한 방향성을 토대로 감시 영역을 정해야 한다.
> - 이 경우, a배열에 원래 맵 정보가 들어있고, b배열을 별도로 만들어서 CCTV의 감시 정보를 저장했다.
> - CCTV는 벽(6)을 관통할 수 없다. 맵의 범위를 벗어나는 것을 처리하는 것은, 가장자리를 모두 벽(6)으로 만들면 편하다.
>
> 출처: https://rebas.kr/732 [PROJECT REBAS]

```python
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = [[6]*(m+2)]
b = [[0]*(m+2) for _ in range(n+2)]
v = []
ans = 1e9
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
U, R, D, L = 1, 2, 4, 8
direct = [[0],
         [U, R, D, L],
         [U|D, R|L],
         [U|R, R|D, D|L, L|U],
         [L|U|R, U|R|D, R|D|L, D|L|U],
         [U|R|D|L]]

def init():
    for _ in range(n):
        a.append([6]+list(map(int, input().split()))+[6])
    a.append(list([6]*(m+2)))
    for i in range(n+2):
        for j in range(m+2):
            if a[i][j] == 6:
                b[i][j] = 1
            elif a[i][j]:
                v.append((i, j, a[i][j]))

def observe(x, y, i, d):
    for k in range(4):
        if i & (1<<k):
            nx, ny = x, y
            while a[nx][ny] != 6:
                b[nx][ny] += d
                nx, ny = nx+dx[k], ny+dy[k]

def solve(index):
    global ans
    if index == len(v):
        area = 0
        for i in range(1, n+1):
            area += b[i].count(0)
        ans = min(ans, area)
        return
    x, y, ids = v[index]
    for i in direct[ids]:
        observe(x, y, i, 1)
        solve(index+1)
        observe(x, y, i, -1)

init()
solve(0)
print(ans)


출처: https://rebas.kr/732 [PROJECT REBAS]
```



## BOJ_16235_나무재테크

> 시간초과가 계속 났는데, deque()로 고치니까 됐다!

```python
'''
처음에는 NxN땅 모두 양분5씩
M개의 나무를 심었다
봄 -> 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
각 나무는 자기칸의 양분만 먹고, 여러 나무가 있을 경우 나이가 어린 나무부터 양분을 먹음
만약, 땅에 양분이 부족하다면 그 나무는 바로 죽고 여름에 죽은나무//2만큼 양분 추가
가을 -> 나무 번식, 번식하는 나무는 나이가 5의배수여야함, 인접한 8개 칸에 나이가 1인 나무가 생김
겨울 -> 땅을 돌아다니며 땅에 양분 추가, 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어짐
K년이 지난 후 살아있는 나무 개수?
'''
import sys
sys.stdin= open('input.txt','r')
input = sys.stdin.readline
import heapq
from collections import deque

di = [-1,1,0,0,-1,1,-1,1]#상하좌우,우상대,우하대,좌상대,좌하대
dj = [0,0,-1,1,1,1,-1,-1]

def year():
    # print('--봄--')
    # for x in tree:
    #     print(x)
    for i in range(N):
        for j in range(N):
            food = land[i][j]
            temp = deque()
            if not tree[i][j]:
                continue
            while tree[i][j]:
                # print(type(tree[i][j]),i,j)
                t = tree[i][j].popleft()
                # print(i,j,t)
                ans = food-t
                # 여름 만약 양분이 부족하면 그 t//2만큼 양분 추가
                if ans < 0:
                    # print('---여름--')
                    land[i][j] += t//2
                    # print(t,t//2,land[i][j])
                # 봄 , 나이추가해서 다시 넣기
                else:
                    temp.append(t+1)
                    # print('나이듦',temp,ans)
                    land[i][j] = ans
                    food = ans
            # heapq.heapify(temp)
            # print(temp)
            tree[i][j].extend(temp)
            # for t in temp:
            #     heapq.heappush(tree[i][j],t)
            # print(i,j,tree[i][j])
    # for x in tree:
    #     print(x)
#     가을
#     print('----가을----')
    for i in range(N):
        for j in range(N):
            if not tree[i][j]:
                continue
            for t in tree[i][j]:
                # 나무가 5의 배수라면
                # print(t)
                # print(t)
                # print(tree[i][j])
                if not t % 5:
                    pi,pj = i,j
                    for d in range(8):
                        ni = pi + di[d]
                        nj = pj + dj[d]
                        if ni < 0 or ni >= N or nj < 0 or nj >= N:
                            continue
                        tree[ni][nj].insert(0,1)
#    겨울
#     print('---겨울----')
    for i in range(N):
        for j in range(N):
            land[i][j] += A[i][j]
    # for x in land:
    #     print(x)

N,M,K = map(int,input().split())
tree = [[deque() for j in range(N)] for i in range(N)]
land = [[5 for j in range(N)] for i in range(N)]
# 각 칸에 추가되는 양분의 양
A = deque()
# print('----땅양분----')
# for x in land:
#     print(x)
for _ in range(N):
    A.append(list(map(int,input().split())))
# print('----A-----')
# for x in A:
#     print(x)
info = deque()
for _ in range(M):
    # 심은 나무 i,j,나이age
    info.append(list(map(int,input().split())))
for t in info:
    i,j,age = t
    tree[i-1][j-1].append(age)

# print('----나무----')
# for x in tree:
#     print(x)
for _ in range(K):
    year()
cnt = 0
# for x in tree:
#     print(x)
for i in range(N):
    for j in range(N):
        if tree[i][j]:
            for t in tree[i][j]:
                cnt += 1
print(cnt)
```



## BOJ_16234_인구이동

> union이 여러개로 나눠져있다가 하나의 경계로 인해 합쳐지는 과정이 없는줄 몰라서 시간이 좀 걸렸다..ㅠ

```python
'''
2020-12-01 16:45
NxN 땅이 있음
각 칸 A[r][c]명이 산다
인구이동
1. 국경선을 공유하는 두 나라의 인구 차이가 L명 이상,R명이하
2. 국경선이 모두 열렸다면 인구이동시작
3. 국경선이 열려있다면 인접한칸으로 연합이라고 하고,
연합의 각 칸 인구수 = (연합의 인구수) // (연합을 이루고 있는 칸의 개수)
4. 연합을 해체하고 모든 국경선을 닫음
각 나라 인구수가 주어졌을때 인구 이동이 몇번 발생하나?
각 칸(a)을 돌면서 인접한 칸(b)이 인구이동 조건 1에 맞다면 국경선이 열린 좌표를 set([i,j,인구수])에 b를 담아줄건데
담아줄때 a가 이미 list안에 있으면 b만 넣어주면 되고, 만약에 없으면 새로운 연합! a와 b를 넣은 list을 list에 추가
모든 국경선을 다 연뒤에 인구이동 시작!
연합 list를 돌면서 조건에 맞게 인구이동시킨뒤 다시 값을 넣어줌
그리고 반복
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]
def checkunion(i,j,num):
    # print('연합있니',unionlist,i,j,num)
    for union in unionlist:
        for u in union:
            if [i,j,num] == u:
                # print(u,union,'같냐?')
                return union
    return False

def findunion(i,j,num):
    # print('연합찾아라',i,j,num)
    pi,pj = i,j
    for d in range(4):
        ni = pi + di[d]
        nj = pj + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        ans = abs(country[ni][nj] - num)
        if ans < L or ans > R:
            continue
        # pi,pj가 연합에 있다면 다음 연합 추가
        # print(pi,pj,num,'-->',ni,nj,country[ni][nj])
        punion = checkunion(pi, pj, num)
        nunion = checkunion(ni,nj,country[ni][nj])
        if punion:
            for u in punion:
                if [ni,nj,country[ni][nj]] == u:
                    break
            else:
                if nunion:
                    punion.extend(nunion)
                    unionlist.remove(nunion)
                else:
                    punion.append([ni,nj,country[ni][nj]])
                # print('--punion연합추가요--')
                # for x in unionlist:
                #     print(x)
            continue
        if nunion:
            for u in nunion:
                if [pi, pj, num] == u:
                    break
            else:
                if punion:
                    nunion.extend(punion)
                    unionlist.remove(punion)
                else:
                    nunion.append([pi, pj, num])
                # print('--nunion연합추가요--')
                # for x in unionlist:
                #     print(x)
            continue
        #연합에 없다면 새로운 연합 list에 넣어줌
        newunion = []
        newunion.append([pi,pj,num])
        newunion.append([ni,nj,country[ni][nj]])
        unionlist.append(newunion)
        # print('--연합추가요--')
        # for x in unionlist:
        #     print(x)


def move(ulist):
    global cnt
    # print('인구이동')
    cnt += 1
    for union in ulist:
        # print(union)
        if not union:
            continue
        people = 0
        for u in union:
            people+=u[2]
        ans = people //len(union)
        for u in union:
            i,j,num = u[0],u[1],u[2]
            country[i][j] = ans
    # for x in country:
    #     print(x)
    return

N,L,R = map(int,input().split())
country = [list(map(int,input().split())) for _ in range(N)]
unionlist = []
cnt =0
while True:
    # print(cnt+1,'여긴몇번')
    # for x in country:
    #     print(x)
    if cnt > 2000:
        break
    for i in range(N):
        for j in range(N):
            findunion(i,j,country[i][j])
    if unionlist:
        move(unionlist)
        unionlist=[]
    else:
        print(cnt)
        break

```



- 다른사람코드

```python
import sys
from collections import deque
read = sys.stdin.readline

N, L, R = map(int, read().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, read().split())))

def BFS(memo, pos, matrix):

    global N, L, R
    i, j = pos
    memo[i][j] = 1
    nations = [(i, j)]
    q = deque([(i, j)])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        i, j = q.popleft()
        for idx in range(4):
            new_i = i + dx[idx]
            new_j = j + dy[idx]
            if new_i < 0 or new_j < 0 or  new_i >= N or new_j >= N:
                continue
            elif memo[new_i][new_j] == 0 and (L <= abs(matrix[i][j] - matrix[new_i][new_j]) <= R):
                q.append((new_i, new_j))
                nations.append((new_i, new_j))
                memo[new_i][new_j] = 1

    if len(nations) == 1:
        return

    sum_v = 0
    for nation in nations:
        sum_v += matrix[nation[0]][nation[1]]
    avg = sum_v // len(nations)
    for nation in nations:
        matrix[nation[0]][nation[1]] = avg



def divide(matrix):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    global N
    memo = [[0]*N for _ in range(N)]
    k = 0
    for i in range(N):
        for j in range(N):
            if memo[i][j] == 0:
                k += 1
                need_bfs = False

                for idx in range(4):
                    new_i = i + dx[idx]
                    new_j = j + dy[idx]
                    if new_i < 0 or new_j < 0 or  new_i >= N or new_j >= N:
                        continue
                    elif memo[new_i][new_j] == 0 and (L <= abs(matrix[i][j] - matrix[new_i][new_j]) <= R):
                        need_bfs = True
                        break

                if need_bfs:
                    BFS(memo, (i, j), matrix)
                else:
                    memo[i][j] = 1

    return k



cnt = 0
while True:
    nations_list = []
    k = divide(matrix)
    if k == N*N:
        print(cnt)
        sys.exit()
    cnt += 1

```

- 다른사람코드

```python
'''
1, dfs 를 돌려서 그룹화하자
2, 그룹별로 이동을시키자
이걸 반복하되 1,2에서 변화가 없으면 그만하자
'''

import sys, copy
sys.setrecursionlimit(10**6)
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
ans = 0
def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print("")

def dfs(y, x):
    global group, group_count_sum
    graph_group[y][x] = group
    # 그 그룹에 몇개가 있는지
    group_count_sum[group][0] += 1
    # 그 그룹에 인구가 얼마나 있는지
    group_count_sum[group][1] += graph[y][x]

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=nx<N and 0<=ny<N and graph_group[ny][nx]==0:
            if L<= abs(graph[y][x] -graph[ny][nx]) <=R:
                graph_group[ny][nx] = group
                dfs(ny, nx)

def is_same(graph, graph_backup):
    for i in range(N):
        for j in range(N):
            if graph[i][j] !=  graph_backup[i][j]:
                return False
    return True

while True:
    graph_group = [[0] * N for _ in range(N)]
    # group_count_sum = [[0, 0]] * ((N**2)+1)
    group_count_sum = [[0]*2 for _ in range(N*N +1)]
    graph_backup = copy.deepcopy(graph)
    group = 1
    #그룹화하고 그룹별 갯수, 인구수 구하기
    for i in range(N):
        for j in range(N):
            if graph_group[i][j]==0:
                dfs(i, j)
                group +=1

    #인구 이동시키기
    for i in range(N):
        for j in range(N):
            graph[i][j] = group_count_sum[graph_group[i][j]][1] // group_count_sum[graph_group[i][j]][0]

    if is_same(graph, graph_backup):
        break
    else:
        ans +=1

print(ans)

```



## BOJ_17144_미세먼지안녕!

> pypy3으로 하니 통과하고 python으로는 시간초과남..

```python
'''
1. 미세먼지확산, 모든 칸 동시에 일어남
인접한 네방향으로 확산되는데 공기청정기가 있거나, 칸이 없으면 그 방향으로 확산 일어나지 않음
확산되는 양은 A[r][c]//5
A[r][c]에 남은 미세먼지의 양은 A[r][c]-A[r][c]//5*확산된방향개수
2. 공기청정기 작동
위쪽 공기청정기의 바람은 반시계방향으로 순환,
아래쪽 공기청정기의 바람은 시계방향으로 순환
바람 불면 미세먼지가 바람의 방향대로 한칸씩 이동
공기청정기에서 부는 바람은 미세먼지 없는 바람, 공기청정기로 들어간 미세먼지는 모두 정화됨
방의 정보가 주어졌을때, T초가 지난 후 남은 미세먼지의 양

1)미세먼지 확산 함수
for돌리다가 먼지가 있는곳 상하좌우 보면서 범위밖이거나 공기청정기가 있는 칸이 아니라면
A[r][c]//5를 추가해주고 cnt를 세어줌, 그런뒤 해당 칸은 A[r][c]//5*cnt만큼 빼줌

2) 공기청정기 함수
공기 청정기가 있는 위에칸은 반시계방향으로 순환하기때문에 처음부터 첫 -1이 있는행까지 반시계로 테두리만 돌림
temp에 해당 크기만큼 배열을 만든 뒤,
반시계방향
2-1.j가 0이고 i가 마지막이 아니라면 temp[i+1][j] = room[i][j]
2-2. i가 마지막이고, j가 마지막이 아니라면 temp[i][j+1] = room[i][j]
2-3. j가 마지막이고, i가 처음이 아니라면 temp[i-1][j] = room[i][j]
2-4. i가 처음이고,j가 처음이 아니라면 temp[i][j-1]= room[i][j]
시계방향
2-1 j가 0이고, i가 처음이 아니라면 temp[i-1][j] = room[i][j]
2-2 i가 0이고, j가 마지막이 아니라면 temp[i][j+1] = room[i][j]
2-3 j가 마지막이고, i가 마지막이 아니라면 temp[i+1][j] = room[i][j]
2-4 i가 마지막이고, j가 처음이 아니라면 temp[i][j-1] = room[i][j]

이동한 곳에 공기청정기가 있다면 0이됨
T초간 반복
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def dust(q):
    while q:
        pi,pj,dustnum = q.popleft()
        cnt = 0
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= R or nj < 0 or nj >= C:
                continue
            if room[ni][nj] == -1:
                continue
            if not dustnum//5:
                continue
            room[ni][nj] += (dustnum//5)
            # print(pi,pj,room[pi][pj],'-->',ni,nj,room[ni][nj])
            cnt+=1
        room[pi][pj] = room[pi][pj] - ((dustnum//5)*cnt)
        # print(cnt,room[pi][pj])
        # for x in room:
        #     print(x)


# 반시계
def revcleaner(row):
    temp = [[0 for j in range(C)] for i in range(row+1)]
    # for x in temp:
    #     print(x)
    for i in range(row+1):
        for j in range(C):
            # 공기청정기는 안움직임
            if room[i][j] == -1:
                temp[i][j] = room[i][j]
                continue
            # # 공기청정기에 닿아서 정화될 먼지
            # if i == row-1 and j == 0:
            #     room[i][j] = 0
            # 2-1.j가 0이고 i가 마지막이 아니라면 temp[i+1][j] = room[i][j]
            if (j==0 and i!= row):
                temp[i + 1][j] = room[i][j]
                continue
            # 2-2. i가 마지막이고, j가 마지막이 아니라면 temp[i][j+1] = room[i][j]
            if (i==row and j != C-1):
                temp[i][j + 1] = room[i][j]
                continue
            # 2-3. j가 마지막이고, i가 처음이 아니라면 temp[i-1][j] = room[i][j]
            if (j == C-1 and i != 0):
                temp[i - 1][j] = room[i][j]
                continue
            # 2-4. i가 처음이고,j가 처음이 아니라면 temp[i][j-1]= room[i][j]
            if (i == 0 and j != 0):
                temp[i][j - 1] = room[i][j]
                continue
            temp[i][j] = room[i][j]
    temp[row][0] = -1
    # for x in temp:
    #     print(x)
    return temp

# 시계
def clockcleaner(row):
    temp = [[0 for j in range(C)] for i in range(row,R)]
    for i in range(row,R):
        for j in range(C):
            # 공기청정기는 안움직임
            if room[i][j] == -1:
                temp[i-row][j] = room[i][j]
                continue
            # # 공기청정기에 닿아서 정화될 먼지
            # if i == row + 1 and j == 0:
            #     room[i][j] = 0
            #2-1 j가 0이고, i가 처음이 아니라면 temp[i-1][j] = room[i][j]
            if (j == 0 and i != row):
                temp[i-1-row][j] = room[i][j]
                continue
            # 2-2 i가 0이고, j가 마지막이 아니라면 temp[i][j+1] = room[i][j]
            if (i==row and j != C-1):
                temp[i-row][j + 1] = room[i][j]
                continue
            # 2-3 j가 마지막이고, i가 마지막이 아니라면 temp[i+1][j] = room[i][j]
            if (j==C-1 and i != R-1):
                temp[i + 1-row][j] = room[i][j]
                continue
            # 2-4 i가 마지막이고, j가 처음이 아니라면 temp[i][j-1] = room[i][j]
            if (i == R-1 and j !=0):
                temp[i-row][j - 1] = room[i][j]
                continue
            temp[i-row][j] = room[i][j]
    temp[0][0] = -1
    # for x in temp:
    #     print(x)
    return temp




R,C,T = map(int,input().split())
# 공기청정기 -1, 나머지는 미세먼지양
room = [list(map(int,input().split())) for _ in range(R)]
# for x in room:
#     print(x)
cleanerRow = 0
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            cleanerRow = i
            break
    if cleanerRow:
        break
# print(cleanerRow)
while T:
    # 1단계 미세먼지 확산
    T-=1
    dustlist = deque()
    for i in range(R):
        for j in range(C):
            if room[i][j] != -1 and room[i][j]:
                dustlist.append([i,j,room[i][j]])
    dust(dustlist)
    # print('미세먼지확산')
    # for x in room:
    #     print(x)
    # 2단계 공기청정
    # print('반시계공기청정')
    temp1 = revcleaner(cleanerRow)
    # print('시계공기청정')
    temp2 = clockcleaner(cleanerRow+1)
    room = temp1+temp2
    # print('바뀐room')
    # for x in room:
    #     print(x)
total = 0
for i in range(R):
    for j in range(C):
        if room[i][j] != -1 and room[i][j]:
            total += room[i][j]

print(total)
```

- 파이썬 통과 다른코드

```python
def spreadDust(): #확산
    move = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if dust[i][j] >= 5:
                d = dust[i][j]//5
                for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < R and 0 <= nj < C and dust[ni][nj] != -1:
                        move[ni][nj] += d
                        dust[i][j] -= d
    for i in range(R):
        for j in range(C):
            dust[i][j] += move[i][j]

def cleanAir(start, dir): # 시작행, dir-방향 -1:위, 1:아래
    if dir == -1:
        # 1. 위로
        for i in range(start - 1, 0, -1):
            dust[i][0]= dust[i - 1][0]
        # 2. 오른쪽으로
        for j in range(0, C - 1):
            dust[0][j] = dust[0][j + 1]
        # 3. 아래로
        for i in range(0, start):
            dust[i][C - 1] = dust[i + 1][C - 1]
        # 4. 왼쪽으로
        for j in range(C - 1, 1, -1):
            dust[start][j] = dust[start][j - 1]
    else:
        for i in range(start + 1, R - 1):
            dust[i][0] = dust[i + 1][0]
        for j in range(0, C - 1):
            dust[R - 1][j] = dust[R - 1][j + 1]
        for i in range(R - 1, start, -1):
            dust[i][C - 1] = dust[i - 1][C - 1]
        for j in range(C - 1, 1, -1):
            dust[start][j] = dust[start][j - 1]
    dust[start][1] = 0

R, C, T = map(int, input().split()) # R:행, C:열, T:초
dust = [list(map(int, input().split())) for _ in range(R)]
cleaner = [] # 공기청정기
for i in range(R):
    if dust[i][0] == -1:
        cleaner.append(i)
        cleaner.append(i + 1)
        break
# T초 동안
for _ in range(T):
    spreadDust()
    cleanAir(cleaner[0], -1) # 반시계방향
    cleanAir(cleaner[1], 1) # 시계방향

dust[cleaner[0]][0], dust[cleaner[1]][0] = 0, 0
print(sum(map(sum, dust)))
```

