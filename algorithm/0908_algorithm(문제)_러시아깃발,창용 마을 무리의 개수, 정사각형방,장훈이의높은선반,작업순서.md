# Algorithm

## 러시아 깃발

```python
#선생님 풀이
T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    #각 행의 색 카운팅
    w = [0] * N
    b = [0] * N
    r = [0] * N

    for i in range(N):
        color = input()
        w[i] = color.count("W")
        b[i] = color.count("B")
        r[i] = M - w[i] - b[i] #M개에서 w의 개수, b의 개수를 뺀 값이 r의 개수
    #누적합을 구해서 나중에 한번에 계산하기 위해..
    for i in range(1,N):
        w[i] += w[i-1]
        b[i] += b[i-1]
        r[i] += r[i-1]

    ans = N*M
    #흰색의 경계를 정함.마지막에 파랑 빨강을 보장해야됨
    for i in range(N-2):
        #파란색의 경계를 정함
        for j in range(i+1,N-1):
            #흰색칠하기
            #i까지의 전체 개수를 구한 뒤 지금까지 칠해져 있는 화이트 개수를 빼기
            cnt = M *(i+1) -w[i]
            #파란색칠하기
            #j-1를 해서 유의미한 전체의 개수를 뽑고, b[j]-b[i]를 하여 해당 범위의 전체 파랑 개수를 뽑아내기
            cnt += M * (i+1) - (b[j] -b[i])
            #빨간색 칠하기
            #위와 마찬가지...ㅎ
            cnt += M * (N-1 -j)-(r[N-1]-r[j])
            ans = min(ans,cnt)
    print('#{} {}'.format(tc,ans))
```



- 다른풀이-조합

```python

#러시아 국기 조합으로 풀기
def combination(sel,idx,cnt):
    global ans
    if cnt == 2:
        print(sel)
        #각각의 1이 경계를 의미
        w = -1
        b = -1
        for i in range(N):
            if sel[i] == 1:
                if w == -1:
                    a = i
                else:
                    b = i
        count = 0
        #흰색 영역 칠하기
        for W in range(0,w+1):
            for k in range(M):
                if flag[W][k] != 'W':
                    count += 1
        for B in range(w+1,b+1):
            for k in range(M):
                if flag[B][k] != 'B':
                    count += 1
        for R in range(b+1,N):
            for k in range(M):
                if flag[R][k] != 'R':
                    count += 1
        return

    if idx >= N-1:
        return
    #경계 뽑고
    sel[sidx] = 1
    combination(sel,idx+1,cnt+1)
    #경계다시 원상복구
    sel[sidx] = 0
    combination(sel,idx+1,cnt)


T = int(input())
for tc in range(1,T+1):
    N,M =(int,input().split())
    #스트링도 idx가 있기 때문에 list로 안 바꿈
    flag = [input() for _ in range(N)]

    ans = M*N

    combination([0]*N,0,0)




```



## 격자판의 숫자 이어붙이기

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
    # global num_set #리스트나 셋은 새로 만드는 거면 해줘야되지만, 변경하거나 참조하면 안해줘도됨
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
    cnt = 0
    num = ''
    num_set = set()

    for i in range(4):
        for j in range(4):
            DFS(i,j,num)
    # DFS(0,0,arr[0][0])
    print('#{} {}'.format(tc,len(num_set)))
```

- 선생님 풀이

```python
#선생님 풀이
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def DFS(r,c,line):
    if len(line) == 7:
        tmp = ''.join(line)
        if tmp not in ans:
            ans.append(tmp)
        return
    for i in range(4):
        nr = r + dr[i]    
        nc = c + dc[i]
        
        if nr < 0 or nr >=N or nc < 0 or nc >= N:
            continue
        line += [arr[nr][nc]]
        DFS(nr,nc,line)
        #다음 반복문을 위해 원상복귀
        line.pop()
            
T = int(input())
for tc in range(1,T+1):
    N = 4
    arr = [input().split() for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            DFS(i,j,[arr[i][j]])
    print('#{} {}'.format(tc,ans))
```



## 조합

- 조합_반복문

```python
arr = [1,2,3,4]
N = 4
R = 2
sel=[0]*R
#arr idx와 sel의 idx
def combination(idx,sidx):
    if sidx == R:
        print(sel)
        return
    for i in range(idx,N):
        sel[sidx] = arr[i]
        combination(i+1,sidx+1)
combination(0,0)
```

- 조합_재귀

```python
arr = [1,2,3,4]
N = 4
R = 2
sel=[0]*R
#arr idx와 sel의 idx
def combination(idx,sidx):
    #순서도 중요! sidx 종료조건을 먼저 줘야됨!
    if sidx == R:
        print(sel)
        return
    if idx == N:
        return
   	sel[sidx] = arr[idx]
    #뽑고가고
    combination(idx+1,sidx+1)
    #안뽑고가고
    combination(idx+1,sidx)
    
combination(0,0)
```



## SWEA_7465_창용마을무리의 개수

```python
'''
창용마을 N명
1~N번까지 사람 번호 붙어있음
서로 아는 관계라면 이어져있음 -> 하나의 무리
창용 마을에 몇 개의 무리가 존재하냐?
'''
import sys
sys.stdin = open('input.txt','r')

def DFS(i):
    visited[i] = True
    for j in range(N+1):
        if linked[i][j] == 1 and visited[j] == False:
            DFS(j)

T = int(input())
for tc in range(1,T+1):
    #마을사람의 수, 관계의 수(같은 관계는 반복해서 주어지지 않음->무향)
    N, M = map(int,input().split())
    linked = [[0]*(N+1) for _ in range(N+1)]
    for m in range(M):
        st,ed = map(int,input().split())
        linked[st][ed] = 1
        linked[ed][st] = 1
    visited = [False for _ in range(N+1)]
    cnt = 0
    #0번부터돌아서 한개 더 생김....
    for i in range(1,N+1):
        if visited[i] == False:
            DFS(i)
            cnt += 1
            # print(visited)
    print('#{} {}'.format(tc,cnt))
```



## SWEA_1861_정사각형 방

```python
'''
arr[i][j]방에 Aij가 적혀있음 이 숫자는 모든 방에 대해 서로 다름
이동하려는 방이 존재해야함, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야됨
처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있는가?

출력
처음 출발해야 하는 방 번호, 최대 몇개의 방을 이동할수있는지.
이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그중 가장 작은 수 출력
dfs -> 재귀에러 뜸
bfs로 풀기
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,0,1,-1] #우좌하상
dj = [1,-1,0,0]
# def DFS(i,j):
#     global cnt
#     visited[i][j] = True
#     # print(i,j)
#     for d in range(4):
#         ni = i + di[d]
#         nj = j + dj[d]
#         if ni < 0 or ni >= N or nj < 0 or nj >= N:
#             continue
#         #현재 값보다 1큰값이 아니면 지나감
#         if room[ni][nj] != room[i][j] + 1:
#             continue
#         if visited[ni][nj] == True:
#             continue
#         cnt += 1
#         DFS(ni,nj)

#재귀에러떠서... bfs로 풀기
def BFS(i,j):
    global cnt
    q = []
    #시작점 넣기
    q.append([i,j])
    # dist[i][j] = 1
    while q:
        #맨 앞의 원소를 담음
        temp = q.pop(0)
        pi,pj = temp[0],temp[1]
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            # 현재 값보다 1큰값이 아니면 지나감
            if room[ni][nj] != room[pi][pj] + 1:
                continue
            # if dist[ni][nj] != 0:
            #     continue
            cnt += 1
            q.append([ni,nj])
            # dist[ni][nj] = 1 + dist[pi][pj]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    #이동하는 방 최대 이동수
    MAX = 0
    for i in range(N):
        for j in range(N):
            # #몇개의 방을 이동할수 있는지 저장
            cnt = 1
            #방문배열 리셋
            # visited = [[False for j in range(N)] for i in range(N)]
            # dist = [[0 for j in range(N)] for i in range(N)]
            # DFS(i,j)
            BFS(i,j)
            if cnt > MAX:
                MAX = cnt
                START = room[i][j]
                # print(MAX_S,'최대값들')
            #같을 떄는 START값에 저장된 값보다 작은값에서 시작하면 START갱신
            elif cnt == MAX:
                if START > room[i][j]:
                    START = room[i][j]
    print('#{} {} {}'.format(tc,START,MAX))
```



## SWEA_1486_장훈이의 높은 선반

```python
'''
서점에는 높이가 B인 선반이 하나 있음
N명의 점원들, 각 점원의 키 Hi로 나타냄, 탑을 쌓아서 선반 위의 물건을 사용하기로 함
점원들이 쌓는 탑은 점원 1명 이상으로 이루어짐
탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명이상이면 그 탑을 만든 모든 점원의 키의 합과 같음
탑의 높이가 B이상, 선반 위의 물건을 사용하는데 탑의 높이가 높을수록 위험
높이가 B이상인 탑중에서 높이가 가장 낮은 탑은?

부분집합..이용..해서 sum이 B이상인 것 중 가장 작은 값!

'''
import sys
sys.stdin = open('input.txt','r')

def powerset(idx,sum_num):
    global MIN
    #이미 값이 MIN보다 크면 끝냄
    if sum_num > MIN:
        # print(sum_num)
        return
    if idx == N:
        total = 0
        for i in range(N):
            if ans[i]: #값이 존재할때
                total += height[i]
        # print(total)
        if total >= B:
            # print(total)
            if MIN > total:
                MIN = total
        return


    #k번째 선택
    ans[idx] = 1
    powerset(idx+1,sum_num)
    #k번째 비선택
    ans[idx] = 0
    powerset(idx+1,sum_num)

T = int(input())
for tc in range(1,T+1):
    #점원, 높이
    N,B = map(int,input().split())
    height = list(map(int,input().split()))
    #점원들 키의 합
    S = sum(height)
    ans = [0]*N
    MIN = S
    sum_num = 0
    # print(S)
    powerset(0,0)


    print('#{} {}'.format(tc,MIN-B))
```

