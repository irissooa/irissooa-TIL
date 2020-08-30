# Algorithm 월말평가 시험공부

## ladder2

- `break`! 다음 check로 넘어갈 때 return이 없으니 break로 for문을 끊어줌

```python
import sys
sys.stdin = open('input.txt','r')

'''
사다리2
사다리타기를 할건데 이건 종료조건이 없음
제일 밑에까지 내려가면 최소 거리의 start값을 출력하면 됨!
이건 함수에 retrun값이 있는게 아니라 global을 써서 기록을 할거야!
check(i,j,s) 인자 3개로 start값을 저장할거야
지나갈때마다 cnt += 1을 해주고 min_dist를 구할거야
해보자!
'''
di = [0,0,1] #우좌하
dj = [1,-1,0]

def check(i,j,dist):
    global min_dist, flag
    visited[i][j] = True
    # print(i,j,dist)
    #종료조건
    #행이 끝까지 내려가면
    if i == 99:
        #밑에 도착했다고 출발점을 표시
        if min_dist > dist:
            min_dist = dist
            flag = True
        # print('도착')
        return
    else:
        #idx에서 벗어나지 않고, 방문하지 않았고, 길이 0이아닌 곳
        # cnt = 0
        for d in range(3):
            ni = i + di[d]
            nj = j + dj[d]
            if ni < 0 or ni >= 100 or nj < 0  or nj >= 100:
                continue
            if ladder[ni][nj] == 0:
                continue
            if visited[ni][nj] == True:
                continue
            #조건에 만족하니까 cnt += 1을 해줌
            dist += 1
            check(ni,nj,dist)
            break #찾았으니까 break를 해야됐는데!!!!!!!!!!!!!!안했음....

for tc in range(1,11):
    T = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    start = []
    for j in range(100):
        if ladder[0][j] == 1:
            start.append(j)
    # print(start)
    min_dist = 987654321
    START = 0 #출발점 저장할 x좌표
    for s in start:
        # print('{}에서 출발'.format(s))
        visited = [[False for j in range(100)] for i in range(100)]
        flag = False
        check(0,s,0)
        if flag: #flag가 True인것 START값에 s저장
            START = s
    print('#{} {}'.format(tc,START))
```





## 단지 번호

- 재귀는 종료가 될 수 있다면 종료조건이 꼭 있어야 되는건 아님!

```python
'''
백준 문제
정사각형의 지도가 있음
1은 집이 있는곳을, 0은 집이 없는 곳을 나타냄
델타이동을 하면서 0들에 쌓여있으면 순서대로 번호를 부여함

출력 :
첫번째 줄에는 총 단지수 출력
각 단지 내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오


구현방법
DFS로 해야됨!!!!!
지도의 크기를 입력받음
지도를 입력받음
방문배열을 사용할거야
1이 이어져 있는 것들을 단지 번호로 바꿀거야!
그리고 그 안의 1(집)의 수를 세고 집 수 반환(오름차순 정렬)
'''
di = [0,0,1,-1] #우좌하상
dj = [1,-1,0,0]
# cnt = 0 #이거 어쩌냥
def check(i,j,num):
    global home_cnt
    visited[i][j] = True
    home_cnt += 1
    home_list[i][j] = num
    # print(i,j)
    #종료조건
    #더이상갈곳이 없을때인데!!!!이거 어떻게 적냐!!!!!.........어차피 갈곳 없으면 종료돼서 따로 안적어줘도 됨!

    #idx조건, 방문하지않은곳,1인곳
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if home_list[ni][nj] == 0:
            continue
        if visited[ni][nj] == True:
            continue
        check(ni,nj,num)
        # break 왜 이건 안되는데?! 4방향을 모두 봐야되니까........................휴...................

N = int(input())
home_list = [list(map(int,input())) for _ in range(N)]
# print(home_list)
visited = [[False for j in range(N)] for i in range(N)] #방문배열
home = []
num = 1
#단지들(뭉텅이) 구함
for i in range(N):
    for j in range(N):
        #인자가 1이고 방문한곳이 아니면
        if home_list[i][j] == 1 and visited[i][j] == False:
            # print('---')
            home_cnt = 0 #리셋
            check(i,j,num) #세어주고
            home.append(home_cnt)
            num += 1
#총 단지 수 = 단지가 담긴 리스트 길이
print(len(home))
for h in sorted(home):
    print(h)
from pprint import pprint
pprint(home_list)

'''
(입력)
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
(출력)
3
7
8
9
[[0, 1, 1, 0, 2, 0, 0],
 [0, 1, 1, 0, 2, 0, 2],
 [1, 1, 1, 0, 2, 0, 2],
 [0, 0, 0, 0, 2, 2, 2],
 [0, 3, 0, 0, 0, 0, 0],
 [0, 3, 3, 3, 3, 3, 0],
 [0, 3, 3, 3, 0, 0, 0]]
'''
```



## SWEA_2805_농작물 수확하기

- slicing
  - `[1:-1]` 이렇게 하면 idx 1에서 끝(-1) idx 전까지 슬라이싱
  - `[2:-2]` : 2 idx에서 -2 idx까지

```python
import sys
sys.stdin = open('input.txt','r')

'''
농장의 크기는 항상 홀수
수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로 가능
가장 첫 줄에는 테스트케이스
농장의 크기N과 농장 내 농작물의 가치가 주어짐

for문을 돌릴건데
열을 중간부터 1,3,5,7,,,이렇게 slicing을 해줄거야
arr[i][N//2 - i: N//2 + i +1] 이 안의 수들을 한 list에 담고 다 더할거야!
'''

T = int(input())
# print(T)
for tc in range(1,T+1):
    N = int(input())
    # print(N)
    arr = [list(map(int,input())) for _ in range(N)]
    # print(f'#{tc} {arr}')
    SUM = []
    for i in range(N):
        #행 idx 반을 넘어가면 2만큼 슬라이싱이 줄어듦 [1:-1] [2:-2]..이런식으로 됨
        if N//2 < i:
            SUM.extend(arr[i][i-N//2:N//2-i])
            # print(arr[i][i-N//2:N//2-i])
            # print(SUM)
        #행idx가 반이 될때까지 slicing이 중간에서 2씩 늘어남
        else:
            SUM.extend(arr[i][N//2 - i:N//2+i+1])
            # print(arr[i][N//2 - i:N//2+i+1])
            # print(SUM)



    # print(SUM)
    print('#{} {}'.format(tc,sum(SUM)))
```



## 파리퇴치

- 이거 풀때 너무 아무생각이 없었다.....
- 다음부턴 정신차리고...스탭을 세세하게 적고 시작하기...!!!!!

```python
import sys
sys.stdin = open('input.txt','r')

'''
NXN배열을 돌건데
크기가 M인 것을 다 더해서 최대인 것을 구함
for문을 돌건데 idx가 N-M+1만큼 돌거야
'''

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    #NXN을 돌면서 MXM의 값들을 다 더할거야
    MAX = 0
    #NXN을 돌면서 MXM을 돌고 그 원소를 더할거야
    for i in range(N-M+1):
        for j in range(N-M+1):
            SUM = 0
            for m in range(M):
                for n in range(M):
                    SUM += arr[i+m][j+n]
            if SUM > MAX:
                MAX = SUM

    print('#{} {}'.format(tc,MAX))
```



##  칠 영역의 개수 구하기

```python
'''
한 변의 크기가 N인 정방형 판
직사각형 영역으로 검은색을 칠하는 기계가 있음
검정으로 칠해진 단위 역역의 개수를 구해라
NXN 배열을 모두 False로 채운다
그 후 M의 영역을 True로 채운다
True인 개수를 구함!
'''


T = int(input())
for tc in range(1, T+1):
    #NXN배열, M : 칠해질 영역의 개수
    N, M = map(int,input().split())
    arr = [[False for j in range(N)] for i in range(N)]
    #x좌표 y좌표의 차를 구함
    #M개만큼 있으니 M 만큼 돈다
    for m in range(M):
        x1,y1,x2,y2 = map(int,input().split())
        #좌상부터 우하까지니까 x1,y1은 x2,y2보다 작다
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                arr[x][y] = True
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == True:
                cnt += 1
    print('#{} {}'.format(tc,cnt))
```



## 최대 사각 테두리 합 구하기

- 테두리 idx를 구하는데 조금 시간이 들었는데 이 방법밖에 생각이 안남...
  - KXK배열을 돌면서 ik가 처음이나 끝일때 jk는 모두 돌고
  - 그외엔, jk가 처음이나 끝일 때  더하게 했다!!

```python
'''
크기가 NXM인 사각 모양의 배열에 자연수가 적여져 있음
크기 K의 사각형 테두리의 숫자 합 중 최대값을 구하려함
'''

T = int(input())
for tc in range(1,T+1):
    #배열 행의 개수 N 배열 열의 개수M, 테두리 한 변의 크기 K
    N, M, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)

    MAX = 0
    for i in range(N-K+1): #행 끝idx에서 K만큼 제외
        for j in range(M-K+1):#열 끝 idx에서 K만큼 제외
            #k만큼 돌거야
            SUM = 0
            for ik in range(K):
                for jk in range(K):
               #크기 K만큼 돌건데 idx가 테두리만 볼거야
                    #ki = 처음과 끝일때 kj만 돈다
                    if ik == 0 or ik == K-1:
                        SUM += arr[i+ik][j+jk]
                    #ki = 중간일때 kj 처음과 끝만
                    else:
                        if jk == 0 or jk == K-1:
                            SUM += arr[i+ik][j+jk]
                        # print(arr[i+ik][j+jk])
            if SUM > MAX:
                MAX = SUM
    print('#{} {}'.format(tc,MAX))
```

- 채린이 코드
  - 아...이러면 좀 더 간단하게 된당ㅠ
  - `total_s += sum(board[r + k][c:c + K])`
  - 각 행마다 c부터 c+K까지 값을 슬라이싱한 것을 더해주고 그걸 total_s에 더해줄거야!

```python
for tc in range(1,int(input())+1):
    N,M,K=map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]

    result=[]
    for r in range(N-K+1):
        for c in range(M-K+1):
            total_s = 0
            minus_s = 0
            #KxK배열을 다 더해줄거야
            for k in range(K):
                total_s += sum(board[r + k][c:c + K])
				#더하지않을 테두리 안쪽값을 다 더해줄거야
                #행이 처음과 끝이 아니고, 열이 처음과 끝을 제외한채로 슬라이싱해줄거야
                if k != 0  and k != K-1:
                    minus_s += sum(board[r + k][c+1:c+K-1])

            result.append(total_s-minus_s)
    print('#{} {}'.format(tc,max(result)))
```

- 주아언니 코드

```python
import sys
sys.stdin = open("tedoori.txt","r")

for T in range(1, int(input())+1):
    N, M, K = list(map(int, input().split()))
    rec = [list(map(int, input().split())) for _ in range(N)]


    MAX = 0
    for i in range(N - K + 1):
        for j in range(M - K + 1):
            total = 0
            #KxK배열 모두 더함
            for a in range(K):
                for b in range(K):
                    #[i+a][j+b] a행b열만큼 위치이동
                    total += rec[i+a][j+b]
			#테두리 안 빼줄 배열
            #K-2배열을 돌건데 행,열위치를 1씩더해줌(그위치에서 시작하기 때문)
            for c in range(K-2):
                for d in range(K-2):
                    total -= rec[i+1+c][j+1+d]

            if total > MAX:
                MAX = total

    print("#{} {}".format(T, MAX))
```



## 섬의 개수 구하기

```python
'''
크기가 N인 정사각형 모양의 배열에 0 이상의 값이 주어짐
0은 바다 1이상의 자연수는 지면
주어진 배열에서 섬의 개수를 구하라
DFS로 구함
방문배열로 갔던 곳 표시하고
배열의 값이 방문하지 않았고, 0이 아닐때 그 개수를 세도록 함
'''
di = [0,0,1,-1,-1,1,-1,1] #우좌하상 우상대 우하대 좌상대 좌하대
dj = [1,-1,0,0,1,1,-1,-1]

def DFS(i,j):
    # global cnt
    visited[i][j] = True
    # cnt += 1 #개수 세줌
    # print(i,j)
    for d in range(8):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if island[ni][nj] == 0:
            continue
        if visited[ni][nj] == True:
            continue
        DFS(ni,nj)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    island = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False for j in range(N)] for i in range(N)]
    num = 0 #섬들의 개수
    for i in range(N):
        for j in range(N):
            # cnt = 0
            if island[i][j] != 0 and visited[i][j] == False:
                num += 1
                DFS(i,j)
                # print(num,'섬 수')

    print('#{} {}'.format(tc,num))
```



## 전기버스

```python
'''
0번에서 출발해 종점인 N번 정류장까지 이동, 한번 충전으로 최대 이동할 수 있는 정류장 수 K
충전기가 설치된 M개의 정류장 번호가 주어짐
최소한 몇 번의 충전을 해야 종점에 도착하는가
충전기 설치가 잘못돼 종점에 도착못하면 0
출발지의 충전횟수는 세지 않음
충전소가 있는 list를 만듦(+출발점, 끝점 추가)
K만큼 이동하는데 그 위치에 충전소가 있으면 cnt += 1을 하고
만약 없다면 뒤로 이동해서 충전소를 찾을거야
그런데도 없다면 도착을 못하니 0 출력
'''

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    #K만큼 이동가능, N : 종점, M :정류장 번호
    K,N,M = map(int,input().split())
    M_list = [0] + list(map(int,input().split())) + [N]
    # print(M_list)
    cnt = -1
    # for i in range(0,N+1,K):
    i = 0 #출발점은 안세주기 때문에 K만큼 이동한 지점에서 시작
    while True:
        if i == N:
            break
        else:
            i += K
            if i in M_list: #정류소가 있는 i면 cnt += 1
                cnt += 1
            else: #만약 아니라면 i를 1씩 빼주면서 정류소를 찾기
                for k in range(i,i-K,-1): #이동한 i값에서 i-K만큼 뒤로 갈건데 그 사이에 충전소를 찾는다면 위치(i)를 k로 갱신해주고 for문을 나감
                    if k in M_list:
                        cnt += 1
                        i = k
                        break
                else: #만약에 충전소를 찾지 못하면 cnt=0으로 출력하고 while문을 나감
                    cnt = 0
                    break
    print('#{} {}'.format(tc,cnt))
```

- 다른코드

```python
import sys
sys.stdin = open("4831.txt","r")

for T in range(1, int(input())+1):
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))
    now = 0
    count = 0

    while now < N - K:
        move = []
        for i in range(1, K+1):
            #K만큼 갈때 충전소가 있는 i값을 모두 저장
            if now + i in charge:
                move.append(i)
		#여기서 i값이 최대인것을 a로 하고 위치 갱신!
        if len(move)>0:
            a = max(move)
            now += a
            count += 1
        #만약 충전소가 없다면 cnt = 0하고 break
        else:
            count = 0
            break


    print("#{} {}".format(T, count))
```



## 스도쿠

- 이거도...결국...생각ㄱ...안나서...채린이 도움 받음ㅠ

```python
'''
한줄(가로, 세로)에 1~9까지 다 들어가고
한 칸(3의배수)에 1~9까지 다 들어있어야됨
해당 칸들을 뽑아서 set()에 넣은 뒤 그 길이가 9인지 확인!
모두 맞다면 1을, 아니라면 0을 출력하라
'''
import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    Z_arr = list(zip(*arr))
    # print(arr)
    # print(Z_arr)
    result = 1

    #가로
    for i in range(9):
        row_set = set()
        for j in range(9):
            row_set.add(arr[i][j])
        if len(row_set) != 9:
            result = 0
            break
    #세로
    for i in range(9):
        col_set = set()
        for j in range(9):
            col_set.add(Z_arr[i][j])
        if len(col_set) != 9:
            result = 0
            break
    #3*3 보기
    for i in range(0,9,3):
        thr_set = set()
        for j in range(0,9,3):
            for r in range(3):
                for c in range(3):
                    thr_set.add(arr[r+i][c+j])
            if len(thr_set) != 9:
                result = 0
                break
    print('#{} {}'.format(tc,result))
```



## 행렬찾기

- MIN과 MAX를 갱신할때 전부 if로 줘서 전부 확인할 수 있게 한다!!!
- `temp = sorted(temp,key=lambda x : (x[0],x[1]))`
  - lambda를 사용하는데 x는 temp의 각요소인데 (x[0],x[1])은 첫번째 x[0]을 기준으로 오름차순으로 정렬하고 만약 값이 같다면 두번째 정렬 기준인 x[1]을 사용해서 정렬! 이때 두개는 `()`로 묶어줌!
  - 만약 내림차순을 하고 싶다면 조건 앞에 -를 붙여주면됨
- 오타좀 내지말장....

```python
'''
화학물질이 NXN으로 배열되어 있음
화학물질이 담긴 용기들 사격형, 내부에는 빈 용기 없음
각 차원(가로용기수 x세로의 용기 수)
A와 B사이와 B와 C사이 빈 용기를 나타내는 '0'원소들
2차원배열에서 찾은 행렬들의 행과 열을 곱한 값 중 크기가 작은 순서대로 출력
행 열 출력
방문배열 이용, DFS이용해서
값이 0이 아닐때 그 행렬의 행과 열을 세고 반복
크기가 같을 경우 행의 크기가 작은 순으로 출력
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,1,0,-1] #우,하,좌 상
dj = [1,0,-1,0]
def DFS(i,j):
    # print(i,j)
    global MAXi,MAXj,MINi,MINj
    visited[i][j] = True
    #MAX와 MIN값이라면 갱신해줘서 row와 col을 구한다
    if i > MAXi:
        # print('MAXi = {}'.format(i))
        MAXi = i
    if j > MAXj:
        # print('MAXj = {}'.format(j))
        MAXj = j
    if i < MINi:
        # print('MINi = {}'.format(i))
        MINi = i
    if j < MINj:
        # print('MINj = {}'.format(j))
        MINj = j

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if arr[ni][nj] == 0:
            continue
        if visited[ni][nj] ==True:
            continue
        DFS(ni,nj)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False for j in range(N)] for i in range(N)]
    temp = []
    for i in range(N):
        for j in range(N):
            # row,col =0,0
            if arr[i][j] != 0 and visited[i][j] == False:
                MAXi, MAXj = 0, 0
                MINi, MINj = 987654321, 987654321
                DFS(i,j)
                # print(MAXi,MAXj,MINi,MINj)
                row = MAXi-MINi+1
                col = MAXj-MINj+1
                # print(row,col)
                temp.append((row*col,row,col))
    # print(temp)
    #내림차순
    temp = sorted(temp,key=lambda x : (x[0],x[1]))
    # print(temp)
    print('#{} {}'.format(tc,len(temp)),end = ' ')
    for i in range(len(temp)):
        print(temp[i][1],temp[i][2], end = ' ')
    print()
```



## 미로

```python
'''
16*16행렬
1은 벽
2는 출발점, 3은 도착점
방문배열 DFS 델타 이용
시작점 (1,1)
1이 아니고, 방문하지 않은 곳에서 DFS(i,j) 적용
3이되면 찾음! 1, 못찾으면 0
'''
import sys
sys.stdin = open('input.txt','r')
di = [0,0,1,-1] #우좌하상
dj = [1,-1,0,0]
def DFS(i,j):
    global result
    visited[i][j] = True

    if arr[i][j] == 3:
        result = 1
        return
    else:
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if ni < 0 or ni >= 16 or nj < 0 or nj >= 16:
                continue
            if visited[ni][nj] == True:
                continue
            #만약 1이면 안간다!! 왜냐면 2나3이면 가야되니까!!
            if arr[ni][nj] == 1:
                continue
            DFS(ni,nj)


for tc in range(1,11):
    T =int(input())
    arr = [list(map(int,input())) for _ in range(16)]
    visited = [[False for j in range(16)] for i in range(16)]
    result = 0 #찾았는지 결과값 초기화
    for i in range(16):
        for j in range(16):
            if arr[i][j] != 0 and visited[i][j] == False:
                DFS(1,1)
    print('#{} {}'.format(tc,result))
```



## 반복되는 단어 제거

```python
'''
스택...이용
문자열을 볼건데
하나씩 stack에 넣고 만약에 stack[-1]값이랑 같은 것이 들어온다면
pop()으로 없애줌
그렇게 들어온 stack을 뽑아줌
'''
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    word = input()
    # print(word)
    stack = []
    for w in word:
        #스택이 비었거나 끝값과 w가 같지 않다면 그걸 append해줌
        if len(stack) == 0 or stack[-1] != w:
            stack.append(w)
            # print(stack)
        #stack에 값이 있고 stack끝값이 w와 같다면 제거
        elif stack and stack[-1] == w:
            stack.pop()
    print(len(stack))
    print(''.join(stack))
```

