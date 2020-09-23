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



## 2578_빙고

> ㅎ..이거도 못품 큰일났다아ㅏ아ㅏ....





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

