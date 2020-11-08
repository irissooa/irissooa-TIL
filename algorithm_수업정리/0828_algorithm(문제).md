# Algorithm

## 백준_15552(빠른 A+B)

- `sys.stdin.readline()`을 `input()`대신 사용해서 실행속도를 높여줌!

```python
import sys
T = int(sys.stdin.readline())
for tc in range(T):
    A, B = map(int,sys.stdin.readline().split())
    print(A+B)
```



## 어디에 단어가 들어갈 수 있을까?

```python
#NXN 단어배열 특정 길이 K를 갖는 단어가 들어갈수 있는 자리수를 출력
# 테스트케이스
#N,K입력받음
#배열 입력받음
#가로에 K길이가 들어갈 수 있는지 개수 확인(K랑 길이가 같아야됨. 크면안됨)
#세로(zip사용해보자)에도 K길이가 들어갈 수 있나!
import sys
sys.stdin = open('input.txt','r')

def check(arr):
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else: #0이 나왔을 때 그 길이가 K면 ans를 +1해주고 cnt를 리셋해줌
                if cnt == K:
                    ans += 1
                    cnt = 0
                else:#길이가K가 아니면, cnt를 다시 리셋
                    cnt = 0 #연속된 1의 개수를세야됨
        if cnt == K:
            ans += 1
    return ans

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    #가로
    words = [list(map(int,input().split())) for _ in range(N)]
    # print(words)
    #세로
    z_words = list(zip(*words))
    # print(z_words)
    #가로를 탐색하는 함수를 쓸건데 ans를 return하는 함수만들거야
    result = check(words) + check(z_words)
    print('#{} {}'.format(tc,result))
```



- 다른 코드

```python
#정현우
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False for j in range(N)] for i in range(N)]
    ans = 0
    # 0 까만색, 1 흰색
    #가로 체크
    for i in range(N):
        for j in range(N-K+1):
            if board[i][j] == 1 and visited[i][j] == False:
                cnt = 0
                ni,nj = i,j
                while nj < N and board[ni][nj] == 1:
                    visited[ni][nj] = True
                    cnt += 1
                    nj += 1
                if cnt == K:
                    ans += 1
    visited = [[False for j in range(N)] for i in range(N)]
    #세로 체크
    for j in range(N):
        for i in range(N - K + 1):
            if board[i][j] == 1 and visited[i][j] == False:
                cnt = 0
                ni, nj = i, j
                while ni < N and board[ni][nj] == 1:
                    visited[ni][nj] = True
                    cnt += 1
                    ni += 1
                if cnt == K:
                    ans += 1
 
    print('#{} {}'.format(tc,ans))
```

- 

```python
#하영
T = int(input())
 
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    word = []
    row_visited = [[False] * N for _ in range(N)]
    col_visited = [[False] * N for _ in range(N)]
 
    for i in range(N):
        for j in range(N):
            row_cnt, col_cnt = 0, 0
            dx, dy = j, j
            while board[i][dx] and not row_visited[i][dx]:
                row_cnt += 1
                row_visited[i][dx] = True
                if dx >= N - 1:
                    break
                else:
                    dx += 1
            while board[dy][i] and not col_visited[dy][i]:
                col_cnt += 1
                col_visited[dy][i] = True
                if dy >= N - 1:
                    break
                else:
                    dy += 1
            if col_cnt > 1:
                word.append(col_cnt)
            if row_cnt > 1:
                word.append(row_cnt)
 
    print(f'#{tc} {word.count(K)}')
```

- 2차원 배열을 바로 받음
- `crosswords+=(list(map(list,zip(*crosswords))))` 이코드대박
- 그냥 일반배열과, zip으로 돌린 배열도 같이 쭉 출력됨!! 그냥 한번만 훑으면된다...!!!와...오빠 천재....

```python
#병훈
#벽은 0 뚫린 공간은 1
#길이 M 단어가 들어가기 위해서는
#M칸이 1이어야하는데 조건으로는 양 옆이 벽이 되어야 한다
#따라서 M+2 칸을 조사한다.
#총 N 칸 중 M+2 칸을 조사하기 위해서는
#인덱스는 0부터  N+2-(M+2)+1 --> N-M+1
#즉 N이 5 M이 3으로 주어지면, 0,1,2 를 조사한다.
 
for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    crosswords = [0] * (N+2)
    for i in range(1,N+1):
        crosswords[i] =[0] + list(map(int,input().split())) + [0]
    crosswords[0] = [0]*(N+2)
    crosswords[-1] = [0]*(N+2)
 
    crosswords+=(list(map(list,zip(*crosswords))))
    cnt = 0
    for line in crosswords:
        for i in range(N-M+1):
            check_line = line[i:i+M+2]
            if check_line[-1]==0 and check_line[0] == 0 and sum(check_line)==M:
            #M칸이 1이어야하는데 조건으로는 양 옆이 벽이 되어야 한다
                cnt+=1
    print('#{} {}'.format(t,cnt))
```



## DFS를 사용하여 1의 개수 세서 출력!

```python
#DFS를 사용하여 1의 개수 세서 출력
#상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def DFS(r,c):
    #개수를 위한 글로벌선언
    global cnt
    #요기왔다는건 1이라는 뜻이므로 카운트 증가
    arr[r][c] = 0 #수를 이미 셌으니 0으로 바꿈
    cnt += 1
    #4방향 탐색
    for i in range(4):
        nr = r + dr[i]
        nc = c +dc[i]
        #idx값 넘지않게!
        #범위를 벗어나면 out,다음좌표가 0이라면 out
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        #이미 센거 안세게!
        if arr[nr][nc] == 0:
            continue
        #조건에 만족되면, 다음 DFS로 넘어감!
        #위에 다걸리지 않았다면, 다음좌표도 1이고 맵의 크기도 안벗어난 것이므로 재귀
        DFS(nr,nc)



N = int(input())
arr = [list(int(input())) for _ in range(N)]
# visited = [[False for j in range(N+1)] for i in range(N+1)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0
            DFS(i,j)
            print(cnt)
```



## 오셀로 게임

```python
import sys
sys.stdin = open('input.txt','r')
#인풋을 받는다
#입력은 열 행 컬러
#돌을 놓았을 떄 8방향 탐색을 하면서
#나와 같은 컬로 찾는다(이떄 중간에 공백이 있거나, 맵의 범위를 벗어나면 수행x)
#찾은 컬러의 좌표부터 지금 놓은 좌표까지 돌아오면서 색갈을 모조리다 나의 컬러로 바꾼다
#위의 과정을 M번 반복하면 끝

#첫 위치를 배열의 len을 구하고 //2해준 위치,
#
# 8방배열을 할거야
# 오셀로 입력값은

# 8방 우 좌 하 상 오상대 오하대 좌상대 좌하대
di = [0, 0, 1, -1, -1, 1, -1, 1]
dj = [1, -1, 0, 0, 1, 1, -1, -1]


def put(i, j, color):
    arr[i][j] = color  # 놓은 곳의 색깔이 달라짐!
    opp_color = -1 #반대컬러 선언
    if color == 1:
        opp_color = 2
    else:
        opp_color = 1

    # 놓음과 동시에 8방으로 훑어보고 색을 바꿔 줘야됨
    for d in range(8):
        ni = i + di[d]
        nj = j + dj[d]
        flag = False  # 중간에 끼인 값들 색을 바꿔줘야된다고 할 표시
        cnt = 0  # 그 중간에 몇개가 껴있는지 세어야됨

        while ni >= 0 and ni < N and nj >= 0 and nj < N:
            #공백일때(0) 빠져나옴
            if arr[ni][nj] == 0:
                break
            if arr[ni][nj] == opp_color:
                cnt += 1
            if arr[ni][nj] == color:
                flag = True #여기까지 색을바꿀거야
                break #같은애 찾았으니 나와랏!
            #그방향으로 계속 감!
            ni += di[d]
            nj += dj[d]
        if flag: #True
            #i,j시작값과 flag가 True인 값 사이의 값을 같은 색으로 바꿀거야!
            for c in range(1,cnt+1): #cnt만큼 돌거야 근데 c는 1부터 해당 cnt까지 돌아야됨!!!!
                #di[d]와 dj[d]가 c만큼 움직였으니까 그거를 원래 좌표에 더한 그 위치를 내 색으로 바꿈!
                arr[i+di[d]*c][j+dj[d]*c] = color




T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0 for j in range(N)] for i in range(N)]
    arr[N // 2][N // 2] = 2
    arr[(N // 2) - 1][(N // 2) - 1] = 2
    arr[(N // 2) - 1][N // 2] = 1
    arr[(N // 2)][(N // 2) - 1] = 1
    # print(arr)

    for _ in range(M):
        row, col, color = map(int, input().split())
        #이게 4X4배열일때 입력받은 idx가 1부터 4까지로 해놓음! 그래서 하나씩 빼줘서(컴퓨터배열은 0~3이니까) idx를 맞춰줌!
        put(row-1,col-1,color)
    #흑돌 백돌 개수를 세어야됨!!!
    black ,white = 0,0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            if arr[i][j] == 2: #0이있을수도 잇으니 else를 하면 안됨!!!!!!
                white += 1
    print('#{} {} {}'.format(tc,black,white))
```

