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

