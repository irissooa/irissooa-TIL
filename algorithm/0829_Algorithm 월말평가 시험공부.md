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

