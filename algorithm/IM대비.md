# IM대비

## 2309_일곱난쟁이

- 조합으로 풀기

```python
'''
조합으로 하면 되지 않을깡
9개중에 7개를 뽑아서 그 합이 100인것 뽑기
'''
def combination(idx,sidx):
    if sidx == 7:
        if sum(R) == 100:
            for i in sorted(R):
                print(i)
            exit()
            return
        # print('못찾았나')
        return
    if idx == N:
        return
    R[sidx] = height[idx]
    combination(idx+1,sidx+1)
    combination(idx+1,sidx)

height = []
for t in range(9):
    height.append(int(input()))
# print(height)
N = 9
R = [0]*7
combination(0,0)
```

- itertools로 풀기

```python
import sys
from itertools import combinations
input = sys.stdin.readline

def solve(case):
    if sum(case) == 100:
        case = list(case)
        case.sort()
        for old in case:
            print(int(old))
        return True
    return False

if  __name__='__main__':
    child = set()
    for i in range(9):
        nai = int(input().strip())
        if nai <= 100:
            child.add(nai)
    for case in combinations(child,7):
        if solve(case):
            break
```

- 2중 for문으로 풀기(완전탐색)

```python
a = []
for i in range(9):
    a.append(int(input()))
res = sum(a)
a.sort()
for i in range(9):
    for j in range(i+1,9):
        if res-a[i]-a[j] == 100:
            for k in range(9):
                if k==i or k==j:
                    continue
                else:
                    print(a[k])
           	exit()
```

- 스윗...

```python
def combination(idx, sidx):
    global ans
    if ans:#이미 구했다면 수행 x
        return
    if sidx == 7:
        if sum(sel) == 100:
            ans = sel[:]
        return
    if idx == 9:
        return
    sel[sidx] = height[idx]
    combination(idx + 1, sidx + 1)#뽑고가고
    combination(idx + 1, sidx)#안뽑고가고


height = [int(input()) for _ in range(9)]

ans = []
sel = [0] * 7
height.sort()
combination(0, 0)
print("\n".join(map(str, ans)))#출력
```



## 2605_줄세우기

> 나중에 다시 풀기...생각안남...ㅠ

```python
'''
첫번째 ->무조건 0번
2번째-> 0또는 1(0: 그자리그대로, 1: 바로 앞의 학생 앞)
3->0,1,2(뽑은 번호만큼 앞자리로 가서 줄섬)
각자 뽑은 번호는 자기 번호보다 1 작은 범위 내
뽑은 번호를 순서대로 하나씩 보면서 뒤에들어온 수만큼 앞으로 보냄, idx를 순서대로 기록!...
'''

import sys
sys.stdin = open('input.txt','r')

N = int(input())
num = list(map(int,input().split()))
order=[1] #1번은 그자리 그대로니까 미리 넣어두고 시작
for i in range(2,len(num)+1):
    if num[i-1] > 0:
        pass
```



- idx를 다시 정하는 건 알겠는데, 어떻게 리스트에 넣는줄 몰라서 많이 헤맸다.......

- `insert`사용!
- insert : `리스트.insert(입력할index, 값)`

```python
a = [1, 2, 3]
a.insert(1, 5)
a
[1, 5, 2, 3]
```

```python
N = int(input())
choice = list(map(int, input().split()))
ans = []
num = 1
for i in range(N):
    idx = len(ans) - choice[i]
    ans.insert(idx, num)
    num += 1
print(*ans)
```





## 2578_빙고

> ㅎ..이거도 못품 큰일났다아ㅏ아ㅏ....

- 정말....ㅎ 어떻게 풀지..노가다...큰이ㅣㄹ.....ㅠ

```python
'''
25개 칸 빙고
사회자가 부르는 수 차례로 지워감
만약 가로,세로, 대각선 줄이 다 지워진 것이 3개이상 있다면 빙고!
사회자가 몇번쨰수를 부른 후 빙고를 외치는가
사회자가 부른 수를 0으로 바꿈!
for문을 돌면서 i가 같은데 다 0 이거나, j가 같은데 전부 0이거나, i==j인데 전부 0이거나, i==4-j 인데 전부0인것이
3개이상 있다면 빙고!
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint

bingo = [list(map(int,input().split())) for _ in range(5)]
num = [list(map(int,input().split())) for _ in range(5)]
# print(bingo)
# print(num)
#빙고조건에 맞다면 cnt += 1
cnt = 0
for r in range(5):
    for c in range(5):
        dae_l = 0 #대각선 수 셈
        dae_r = 0
        for i in range(5):
            zero_r=0
            zero_c=0
            for j in range(5):
                #num에서 차례대로 나오는 수와 빙고와 일치하는게 있다면 그거 0으로 바꿈
                if num[r][c] == bingo[i][j]:
                    bingo[i][j] = 0

                #for문을 돌면서 i가 같은데 다 0 이거나,
                if bingo[i][j] == 0:
                    # print(zero_r)
                    zero_r+=1

                # j(열)가 같은데 전부 0이거나,
                if bingo[j][i] == 0:
                    zero_c += 1

                # i==j인데 전부 0이거나,
                if i == j and bingo[i][j] == 0:
                    dae_l += 1

                # i==4-j 인데 전부0인것이
                if i == 4-j and bingo[i][j] == 0:
                    dae_r += 1

                if zero_r == 5:
                    print(i,'행 빙고')
                    pprint(bingo)
                    cnt += 1
                    zero_r=0

                if zero_c == 5:
                    print(i,'열 빙고')
                    pprint(bingo)
                    cnt += 1
                    zero_c=0

                if dae_l == 5:
                    print('왼대각선빙고')
                    pprint(bingo)
                    cnt += 1
                    dae_l=0

                if dae_r == 5:
                    print('오대각선빙고')
                    pprint(bingo)
                    cnt += 1
                    dae_r = 0

                #종료조건
                if cnt == 3:
                    print('빙고')
                    pprint(bingo)
                    print(zero_r,zero_c,dae_l,dae_r)
                    print(r*5+c,r,c)
                    exit()

```



- 

```python
#선생님 풀이
def check():
    cnt = 0
    # 가로세로 확인
    for i in range(N):
        cnt_row = 0
        cnt_col = 0
        for j in range(N):
            if bingo[i][j] == 0: cnt_col += 1
            if bingo[j][i] == 0: cnt_row += 1

        if cnt_row == N: cnt += 1
        if cnt_col == N: cnt += 1

    # 대각선, 역대각선 확인
    cnt_l = 0
    cnt_r = 0
    for i in range(N):
        if bingo[i][i] == 0: cnt_l += 1
        if bingo[i][N - 1 - i] == 0: cnt_r += 1

    if cnt_l == N: cnt += 1
    if cnt_r == N: cnt += 1

    if cnt >= 3: return True
    return False


N = 5
bingo = [list(map(int, input().split())) for _ in range(N)]

pos = [0] * 26
#해당 번호 좌표 담기
for i in range(N):
    for j in range(N):
        pos[bingo[i][j]] = (i, j)

call = []

#사회자가 호출하는 번호 한줄로 만들기
for i in range(N):
    call += list(map(int, input().split()))

ans = 0

while not check():
    r, c = pos[call[ans]]
    bingo[r][c] = 0
    ans += 1
print(ans)

```



- 주아언니

```python
def countbingo(v):
    global countList
    a = b = 0
    flag = True
    for i in range(5):
        for j in range(5):
            if arr[i][j] == v:
                a = i
                b = j
                flag = False
                break
        if flag == False: break

    countList[a] += 1
    countList[5+b] += 1
    if a == 2 and b == 2:
        countList[10] += 1
        countList[11] += 1
    if a == b and a!=2 and b!=2:
        countList[10] += 1
    if a + b == 4 and a!=2 and b!=2:
        countList[11] += 1
    return

arr = [list(map(int, input().split())) for _ in range(5)]


countList = [0]*12

given = [list(map(int, input().split())) for _ in range(5)]


count = 0
flag2 = True
for i in range(5):
    for j in range(5):
        count += 1
        a = given[i][j]
        countbingo(a)

        if countList.count(5) >= 3:
            print(count)
            flag2 = False
            break
    if flag2 == False: break
```





## 2563_색종이

```python
'''
가로, 세로 100 정사각형
크기가 각 10
검은 영역 넓이를 구하는 프로그램
'''
N = int(input())
arr = [[0 for j in range(100)] for i in range(100)]
for i in range(N):
    #x는 열, y는 행
    y,x = map(int,input().split())
    for i in range(10):
        for j in range(10):
            arr[y+i][x+j] = 1
    
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1


print(cnt)
```

- 스윗..

```python
N = int(input())

paper = [[0] * 102 for _ in range(102)]

for i in range(N):
    r, c = map(int, input().split())
    for j in range(r, r + 10):
        for k in range(c, c + 10):
            paper[j][k] = 1

ans = 0
for i in range(102):
    ans += paper[i].count(1)
print(ans)
```





## 2491_수열

```python
'''
수열중에서 다음 수가 연속해서 커지는 것 세고
연속해서 작아지는 것 세고
더 긴것 출력
'''
N = int(input())
# N = 6
arr = list(map(int,input().split()))
# arr = [3, 2, 1, 2, 3, 4]
MAX = 1
MIN = 1
len_list = []
for i in range(1,N):
    #다음수가 크거나 같다면
    if arr[i-1] <= arr[i]:
        # print(arr[i])
        MAX += 1
    #작은수가 나오면 0
    else:
        len_list.append(MAX)
        # print(len_list)
        MAX = 1
len_list.append(MAX)
for i in range(1,N):
    #다음수가 더 작은수가 나온다면
    if arr[i-1] >= arr[i]:
        MIN += 1
    else:
        len_list.append(MIN)
        # print(len_list)
        MIN = 1
len_list.append(MIN)
print(max(len_list))

'''
6
3 2 1 2 3 4
'''
```

- 스윗..

```python
def check(nums):
    global ans
    cnt = 1
    for i in range(1, N):
        if nums[i-1] <= nums[i]: cnt+=1
        else: cnt = 1

        if ans < cnt : ans = cnt


N = int(input())
arr = list(map(int, input().split()))

ans = 1

check(arr)
check(arr[::-1])
print(ans)
```





## 2669_직사각형 네개의 합집합 구하기

```python
'''
좌표가 해당 2차원배열의 idx번호
'''
arr = [[0 for j in range(100)] for i in range(100)]
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)
```

- 스윗..

```python
arr = [[0] * 102 for _ in range(102)]

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1
ans = 0
for i in range(102):
    ans += sum(arr[i])

print(ans)
```





## 13300_방배정

```python
'''
성별이 다르고, 학년이 같아야되고, K명을 넘을 수 없다
방의 최소 개수구하기
'''
N,K = map(int,input().split())
#학생의 성별S(0:여,1:남), 학년 Y
#학년별 idx
G_arr = [0 for _ in range(7)]
B_arr = [0 for _ in range(7)]
for _ in range(N):
    S,Y = map(int,input().split())
    #남자
    if S:
        B_arr[Y] += 1
    #여자
    else:
        G_arr[Y] += 1
# print(B_arr)
# print(G_arr)
#학년이 idx
room = 0
# cnt = 0
for i in range(1,7):
    if B_arr[i] > K:
        if B_arr[i]%K:
            room += B_arr[i]//K + 1
        else:
            room += B_arr[i]//K
    elif B_arr[i]:
        room += 1
    if G_arr[i] > K:
        if G_arr[i] % K:
            room += G_arr[i] // K + 1
        else:
            room += G_arr[i] // K
    elif G_arr[i]:
        room += 1
print(room)

'''
5 2
0 1
0 1
0 1
0 1
0 1
'''
```

- 스윗..

```python
N, K = map(int, input().split())

student = [[0] * 7 for _ in range(2)]

for i in range(N):
    gender, grade = map(int, input().split())

    student[gender][grade] += 1

room = 0

for i in range(2):
    for j in range(1, 7):
        room += student[i][j] // K
        if student[i][j] % K:
            room += 1

print(room)
```



## 2564_경비원

- 이거...ㅎ 못품...ㅎ 어떻게 풀지감도 안옴...

```python
'''
블록의 가로, 세로 길이가 주어짐
상점의 개수와 위치, 동근이의 위치도 주어짐(이동할 때 가로지를수 없음)
동근의 위치와 각 상점사이의 최단 거리 합을 구함
'''
import sys
sys.stdin=open('input.txt','r')
from pprint import pprint

#가로와 세로
c,r = map(int,input().split())
arr = [[0 for j in range(c)] for i in range(r)]
#테두리 1로 둘러주기
for i in range(r):
    for j in range(c):
        if i == 0 or i == r-1:
            arr[i][j] = 1
        else:
            if j == 0 or j == c-1:
                arr[i][j] = 1
# pprint(arr)
#상점의 개수
N = int(input())
# 상점의 위치 1은 블록의 북, 2는 블록의 남, 3은 블록의 서, 4는 블록의 동
#마지막 줄 동근이 위치
for n in range(N):
    x, dist = map(int,input().split())
    # print(x,dist)
    #상점의 위치 표시(N으로)
    if x == 1:
        arr[0][dist-1] = N
    if x == 2:
        arr[r-1][dist-1] = N
    if x == 3:
        arr[dist-1][0] = N
    if x == 4:
        arr[dist-1][c-1] = N
dong_x,dong_dist = map(int,input().split())

# pprint(arr)
#동근이의 위치와 각 상점사이의 최단거리 합...구하기
```

- 다시 선생님 코드 보고 품..후

```python
'''
블록의 가로, 세로 길이가 주어짐
상점의 개수와 위치, 동근이의 위치도 주어짐(이동할 때 가로지를수 없음)
동근의 위치와 각 상점사이의 최단 거리 합을 구함
'''
import sys
sys.stdin=open('input.txt','r')
from pprint import pprint

def clockwise(x,pos):
    if x == 1:#북
        return pos
    elif x == 2:#남
        return c+r+c-pos
    elif x == 3: #서
        return c+r+c+r-pos
    else: #동
        return c+pos

#가로와 세로
c,r = map(int,input().split())
N = int(input())
dist = []
for i in range(N+1):
    x,pos = map(int,input().split())
    dist.append(clockwise(x,pos))
my_dist = dist[-1]
cir = (r+c)*2

result = 0
for i in range(N):
    ans =abs(my_dist-dist[i])
    result += min(ans,cir-ans)
print(result)
```



- 

```python
#선생님은 이렇게 풀으셨더라...ㅠ
def dist_calc(idx, pos):
    if idx == 1:  # 북
        return pos
    elif idx == 2:  # 남
        return C + R + C - pos
    elif idx == 3:  # 서
        return C + R + C + R - pos
    else:  # 동
        return C + pos


C, R = map(int, input().split())
circumference= (C+R)*2

N = int(input())

dist = []
for i in range(N+1):
    idx, pos = map(int,input().split())
    dist.append(dist_calc(idx,pos))

my_dist = dist[-1]

ans = 0

for i in range(N):
    clockwise = abs(my_dist-dist[i])
    ans += min(clockwise,circumference-clockwise)
print(ans)

```





## IM대비

```python
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
'''
5개 항목 중 정답인 항목 고름
오지선다 형식 객관식 총 M개 문제 주어짐
맞힌 문제 하나당 1점, 연속으로 맞출 경우 1점 가산
가장 높은 점수 받은 학생과 가장 낮은 점수를 받은 학생의 점수차를 출력
정답 list를 받음
N명의 학생들이 제출한 답지를 훑어보면서 답이 맞다면 +1 
그다음 것도 맞다면 연속으로 맞은 개수만큼 곱한값을 더해주다가
틀리면  점수0, cnt도 0
'''

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    score = list(map(int,input().split()))
    # print(score)
    students=[]
    for j in range(N):
        students.append(list(map(int,input().split())))
    # pprint(students)
    students_score=[]
    for student in students:
        S = 0#점수
        cnt = 0
        for i in range(M):
            #정답이라면
            if score[i] == student[i]:
                cnt += 1
                S += 1 *cnt
                # print(S,'정딥',end=' ')
            #오답이라면
            else:
                cnt=0
                # S = 0
                # print(S,'오답',end=' ')
        students_score.append(S)
        # print()
    # print(students_score)
    print('#{} {}'.format(tc,max(students_score)-min(students_score)))
```





## 2628_종이자르기

> 이거 DFS로 풀었는데,,,,테케는 맞았지만 틀렷따!
>
> 아마 idx+1에서 문제가 생긴 것 같은데 IM끝나고 다시 해봐야갰다!

```python
import sys
sys.stdin=open('input.txt','r')
from pprint import pprint

di = [0,0,1,-1]#우좌하상
dj = [1,-1,0,0]
def DFS(i,j):
    global cnt
    visited[i][j] = True

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if arr[ni][nj] == 0:
            continue
        if visited[ni][nj]:
            continue
        cnt += 1
        DFS(ni,nj)

C,R=map(int,input().split())
N=int(input())
arr=[[1]*C for _ in range(R)]
arr.insert(0,[0]*C)
arr.append([0]*C)

for x in arr:
    x.insert(0,0)
    x.append(0)
# pprint(arr)
for _ in range(N):
    dir, idx = map(int,input().split())

    if dir==0:
        arr.insert(idx+1,[0]*(len(arr[0])))
        # print('가로추가')
        # pprint(arr)
    else:
        for x in arr:
            x.insert(idx+1,0)
        # print('세로추가')
        # pprint(arr)
# print()
# pprint(arr)
#dfs돌리기
visited = [[False for j in range(len(arr[0]))] for i in range(len(arr))]
ans = []#넓이 값을 받을 리스트
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 1 and visited[i][j] == False:
            cnt = 1
            DFS(i,j)
            ans.append(cnt)
print(max(ans))
```

- 띠를 둘러주는 법

```python
#1. 방법
#0이면 멈춰야되니까 전체 띠를 두름
# 제일 위와 제일 밑에 띠를 두른것처럼 0으로 만들어줌
arr = [0] * (N+2)
arr[0] = arr[N+1] = [0] * (N+2)
for i in range(N):
    #왼쪽 오른쪽에도 띠를 만들어줌
    arr[i+1] = [0]+list(map(int,input().split()))+[0]
    
    
    
#2. insert,append사용
arr = [[1,1,1],[1,1,1],[1,1,1]]
#위, 아래 배열에 0으로 채워줌
arr.insert(0,[0]*len(arr[0])) #3을곱한 배열을 0idx에 삽입해서 앞에 0으로 채움
arr.append([0]*len(arr[0])) #뒤에도 마찬가지로 그만큼 삽입
#오른쪽, 왼쪽 idx에도 0으로 채워줌
#for문을 돌면서 각 배열에 앞 뒤로 0삽입
for x in arr:
    #x배열 0idx에 0채우기
    x.insert(0,0)
    #x배열 제일 뒤에 0채우기
    x.append(0)
print(arr)
'''
[[0, 0, 0, 0, 0],
 [0, 1, 1, 1, 0],
 [0, 1, 1, 1, 0],
 [0, 1, 1, 1, 0],
 [0, 0, 0, 0, 0]]
'''

```

