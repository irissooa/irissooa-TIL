# Algorithm(2020-08-05)

> List
>
> 알고리즘은 종이에 써봐야 된다!! 직접 쳐봐야 된다!! 머리로만 생각하면 안된다. 시행착오를 다 겪어봐야 한다.
>
> 시험때 계산기 사용가능 프로그래머용은 진수도 표현됨

- 버블 소트 : 교환을 하는 것
- 카운팅 정렬 
  - index값을 갖고 들어온 데이터를 체크함
  - 정수로 표현할 수 있는 자료들이 와야 된다.
  - 선형이라 빠르다

- 완전 검색
  - 모든 경우의 수를 나열
- 탐욕 알고리즘
  - 한 큐에 한번에 해결하려고 하는것
  - 되도록이면 완전 검색으로 하세요



## 배열 : 2차 배열

- 2차원 입력받는 방법(골라쓰기!)

```python
'''
입력값
3 3
1 2 3 
4 5 6 
7 8 9
'''
#1방법
N, M = map(int,input().split())
mylist = [0 for _ in range(N)]
#mylist = [0] * N
for i in range(N):
    mylist[i] = list(map(int,input().split()))
print(mylist) #[[1,2,3],[4,5,6],[7,8,9]]

#2방법
N, M = map(int,input().split())
mylist = []
for i in range(N):
    mylist.append(list(map(int,input().split())))
print(mylist) #[[1,2,3],[4,5,6],[7,8,9]]

#3방법
N, M = map(int,input().split())
mylist = list(map(int,input().split())) for _ in range(N)
print(mylist) #[[1,2,3],[4,5,6],[7,8,9]]

#0으로 초기화 하는 방법 : visited 초기화
v = [0] * 3 #1차원 0으로 초기화
#2차원은?
N = 3 #행
M = 4 #열
#열을 먼저 쓰고!! 행을 만들어야됨!!
#**M을 N번 만든다!
#1
v = [[0 for _in range(M)] for _ in range(N)] #2차원 0으로 초기화
#2
v = [[0] * M for _ in range(N)]
print(v) #[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
```

- 2차원 배열의 선언
- 세로길이(행의 개수), 가로길이(열의 개수)로 필요로 함
- 파이썬은 데이터 초기화를 통해 변수선언과 초기화가 가능
- arr = [[1,2,3],[4,5,6]]

| 0(0,0) | 1(0,1) | 2(0,2) | 3(0,3) |
| :----: | :----: | :----: | :----: |
| 4(1,0) | 5(1,1) | 6(1,2) | 7(1,3) |

- 배열순회
  - nXm 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법

- 행 우선 순회
  - i 행의 좌표 -> i는 제어변수(tmi : `포트란`과학계산용프로그래밍언어 정수를 표현 할 때 묵시적으로 i, j, k, l, m, n...)
  - C나 다른 언어는 직사각형밖에 안되는데 파이썬은 가능함

```python
#i 행의 좌표
#j 행의 좌표
#ex)구구단
for i in range(len(Array)): #row 행 가로
    for j in range(len(Array[i])): #column 열 세로
        Array[i][j] #필요한 연산 수행
```

- 열 우선 순회

```python
#i 행의 좌표
#j 열의 좌표
for j in range(len(Array[0])):#i
    for i in range(len(Array)):#j
        Array[i][j] #->아니면 이걸 [j][i]로 바꿈
#(0,0)->(1,0)->(2,0)->...
```

```python
arr = [[1,2,3],[4,5,6],[7,8,9]]
N = len(arr) #행의 길이
M = len(arr[0]) #열의 길이
#행우선
for i in range(N):
    for j in range(M):
        print(arr[i][j], end = ' ')
        print()
print()
#열우선
for j in range(M): #열
    for i in range(N): #행
    	print(arr([i][j]),end = ' ')
    print()
print()
```

- 지그재그 순회(이건 참고.. 행우선 열우선을 알아두기!)

```python
#i 행의 좌표
#j 열의 좌표
for i in range(len(Array)):
    for j in range(len(Array[0])):
        Array[i][j+(m-1-2*j)*(i%2)]
```

- 델타(차이)를 이용한 2차 배열 탐색(**많이 쓰임)
  - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법(for문 순회 2번)
  
  - 인덱스체크, 방문체크
  
  - | (x-1,y-1) | (x-1,y) | (x-1,y+1) |
    | --------- | ------- | --------- |
    | (x, y-1)  | (x,y)   | (x,y+1)   |
    | (x+1,y-1) | (x+1,y) | (x+1,y+1) |

```sh
dx = [-1,0,1,0]
dy = [0,-1,0,1]
dx,dy안의 상하좌우 순서는 상관없은 같기만 하면 됨
```



```python
ary[0.....n-1][0...n-1]
dx[]<-[0,0,-1,1] #상하좌우 방향은 먼저 하고안하고 관계없음
dy[]<-[-1,1,0,0] 

for x in range(len(ary)):#2차원순회
    for y in range(len(ary[x])):#2차원순회
        for i in range(4):
            #testX <-x +dx[i]
            #testY <-y+dy[i]
            test(ary[testX][testY])
```

```python
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

N = len(Arr) #3
M = len(arr[0]) #4

dx= [0,0,-1,1] #8방향(대각선 포함)이면 8개로 늘어남
dy = [-1,1,0,0]

for x in range(N): #x=0,1,2
    for y in range(M): #y=0,1,2,3
        for i in range(4): #이건 항상 4, 상하좌우dxdy
            testX = x + dx[i]
            testY = y + dy[i]
            #2중리스트안의 인덱스체크(인덱스 벗어나면 안됨)
            #1)
            if testX > 0 and testX < N and testY >= 0 and testY < M: 
           #2)if 0 <= testX < N and 0 <= testY < M: 파이썬은 이게 가능함
        	#3)if testX < 0 or testX >= N: continue
            #3)if testY<0 or testY >=M: continue
                print(arr[testX][testY], end = ' ')
```

#### 연습문제1

```python
#델타차를 이용한 2차배열
#무작위로 5행 5열 만듦->randint함수 써도됨
#인덱스에 벗어나지 않게 if문 처리
#상하좌우를 보며 요소와의 차를 구함(절댓값 abs함수)
#구한 차를 모두 더함

dx = [-1,0,0,1]
dy = [0,-1,1,0]

arr = [[1,2,3,4,5],
       [5,6,7,8,9],
       [2,3,4,5,6],
       [5,6,7,3,6],
       [20,40,3,4,5]
       ]

N = 5 #행
M = 5 #열

res = 0
for x in range(N): #x=0,1,2,3,4
    for y in range(M): #y=0,1,2,3,4
        for i in range(4): #이건 항상 4, 상하좌우dxdy
            testX = x + dx[i] #새로운좌표 x
            testY = y + dy[i] #새로운 좌표 y
            #2중리스트안의 인덱스체크(인덱스 벗어나면 안됨)
            if testX > 0 and testX < N and testY >= 0 and testY < M:
                res += abs(arr[x][y]-arr[testX][testY])

print(res) #334
```



- 전치행렬
  - 조합을 구한는 데도 사용됨!

```python
#i : 행의 좌표, len(arr)
#j : 열의 좌표, len(arr[0])

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N) :
    for j in range(i+1, M):
        if i < j: #이게 없으면 두번을 swap해서 그대로 돌아옴
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
```

```python
# 조합(전치행렬 활용)
arr = [1,2,3,4]
for i in range(len(arr)-1) :
    for j in range(i+1, len(arr)):
		print((arr[i],arr[j]),end= ' ')
        #(1,2),(1,3),(1,4),(2,3)....
```



#### 부분집합 합 문제(파워셀, 멱집합..)

- 부분집합 빅오 시간계산법으로 `2^n`
- 완전검색기법으로 품
- 집합의 원소가 n개일때, 공집합을 포함한 부분집합의 수는 2^n개

```python
#2진수의 부분집합들이 나옴
def printlist(arr,bit):
    for i in range(len(bit)):
        if bit[i]: #참이면
            print(arr[i], end = ' ')
    print()
    
arr = [1,2,3]
bit = [0,0,0] #공집합
for i in range(2):
    bit[0] = i #0번째 원소
    for j in range(2):
        bit[1] = j #1번째 원소
        for k in range(2):
            bit[2] = k #2번째 원소
            printlist(arr,bit)
```

```python
#원소가 3개인 집합의 부분집합
bit = [0,0,0] 
for i in range(2):
    bit[0] = i #0번째 원소
    for j in range(2):
        bit[1] = j #1번째 원소
        for k in range(2):
            bit[2] = k #2번째 원소
            print(bit) #생성된 부분집합 출력
```

- 하지만 bit = [0,0,0] 이런식으로 표현하면 속도가 느려짐
- 비트 연산자를 활용한다.

#### 부분집합 합 문제

- 완전탐색으로 한다면 10중 for문으로 2^10으로 속도가 매우 느려짐..(좋지않음)
- 비트연산활용!

```python
arr = [1,2,3]
n = len(arr) #n:원소의 개수
for i in range(1<<n) : #1<<n:부분집합의 개수 0에서 2^n전까지 움직임
    for j in range(n): #원소의 수만큼 비트를 비교함
        if i & (1<<j): #i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j],end = ',') #0이 아니면 True
        print()
    print()
```

```sh
i j		부분집합{000은 3,2,1순}
0 000 	{}
1 001	{1}
2 010	{2}
3 011	{1,2}
4 100	{3}
5 101	{1,3}
6 110	{2,3}
7 111	{1,2,3}
```

- 오른쪽에서 왼쪽(`i & (1<<j)`을 보기 때문에 arr의 반대순!

- 풀이

```python
# arr = list(map(int,input().split()))
arr = [-1,2,1]
N = len(arr) #n:원소의 개수
cnt = 0

for i in range(1 << N) : #1<<n:부분집합의 개수 0에서 2^n전까지 움직임
    SUM = 0
    sub = []
    for j in range(N): #원소의 수만큼 비트를 비교함
        if i & (1 << j): #i의 j번째 비트가 1이면 j번째 원소 출력
            sub.append(arr[j])
            SUM += arr[j]
    if SUM == 0 :
        cnt += 1
        print(sub)
print('{}'.format(cnt))
```





## 비트연산자

- 비트 : `2진수로 바꿔서 계산`함 결과는 정수로 나옴
- `&` 비트 단위로 AND 연산을 한다.(논리곱 : 둘다1이나 0이어야됨)
- `|` 비트 단위로 OR 연산을 한다. (논리합 : 하나라도 1이면 1)
- `<<` 피연산자의 비트 열을 왼쪽으로 이동 
- `>>` 피연산자의 비트 열을 오른쪽으로 이동
- `<< 연산자`(파이썬은 2**n 이렇게 써도 되지만 보통 다른 언어는 q비트연산자 사용)
  - `1<<n`: `2^n` 즉, 원소가 n개일 경우 모든 부분집합의 수를 의미
- `&연산자`비트 열 확인
  - `i$(1<<j)` : i의 j번째 비트가 1인지 아닌지 리턴

```python
a=5 #2진법 0101
b=3 #0011

print(a&b) #0001 논리곱 (출력1)
print(a|b) #0111 논리합 (출력7)
print(1<<3) #0001-> 1000 2^3 (출력8)
print(a^b) #0110 다르면 1 같으면 0 (출력6)
```

- 0(False)이 아닌값은 모두 참(True)



## 검색

- 저장되어 있는 자료 중 원하는 항목 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾음
  - 탐색 키 : 자료를 구별하여 인식할 수 있는 키
- 순차탐색(sequential search)
- 이진검색(binary search) : 정렬이 되어 있으면 씀
- 해쉬(hash) -> B형시험 볼 때 필요

### 순차검색

- 일렬로 되어 있는 자료를 순서대로 검색
- 가장 간단, 직관적
- 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용
- 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우 수행시간이 급격히 증가하여 비효율적

##### 정렬되어 있지 않은 경우

- 첫번째 원소부터 순서대로 검색, 키값고 같은 원소를 찾음
- 찾으면 그 원소의 인덱스 반환
- 마지막까지 못찾으면 검색 실패

```python
def seq_search(a,n,key):
    i = 0
    while i < n and a[i] != key: #i는 n보다 작고 key값과 같지 않으면 끝남
        i += 1
    if i < n : return i
    else : return -1 #못찾으면 -1 false를 의미


arr = [4,9,11,23,2,19,7]
key = 233
print(seq_search(arr,len(arr),key))
```



##### 정렬된 경우

- 오름차순으로 정렬된 상태, 순차적 키 값 검색, 중간에 멈출 수 있다(끝까지 안가도 된다)

```python
def seq_search(a,n,key):
    i = 0
    while i < n and a[i] < key: #i는 n보다 작고 key값보다 작으면 끝남
        i += 1
    if i < n and a[i]==key : return i
    else : return -1 #못찾으면 -1 false를 의미


arr = [1,2,3,4,5,6,7,8,9]
key = 3
print(seq_search(arr,len(arr),key))
```



### 이진 검색

- 필수조건 : 정렬된 상태
- 검색 범위를 반으로 줄여가면서 보다 빠르게 검색 수행

- 검색과정
  - 자료의 중앙의 원소를 고름
  - 중앙 원소 값과 목표값을 비교
  - 목표값이 더 작으면 자료의 왼쪽, 크면 오른쪽에 위치함
  - 자료의 반을 버림. 찾고자 하는 값을 찾을 때 까지 반복

- 구현

  - 검색 범위의 시작점과 종료점 이용하여 검색을 반복 수행

  - 자료에 삽입이나 삭제가 발생, 배열의 상태를 항상 정렬상태로 유지하는 추가 작업이 필요

```python
def binarySearch(a,key):
    #start=0 end = length(a)-a
    while start <= end: #start보다 end가 앞으로 갈때 검색실패
        middle = (start + end)//2
        if a[middle] == key : #검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else : start = middle + 1
    return False #검색실패
```

- return -1을 적을 때는 idx에 문제가 없는지 확인하고 써야됨.

```python
def bin_search(a,key):
    start = 0
    end = len(a)
    while start <= end:
        middle = (start + end)//2
        #key값과 같은 경우 ==
        if a[middle] == key:
            return True, middle # 튜플로도 나옴
        #key값보다 큰경우 <
        elif a[middle] > key:
            end = middle - 1
        #key값보다 작은경우>
        else:
            start = middle + 1
    return False,-1

arr = [2,4,7,9,11,19,23]
key = 7
print(bin_search(arr,key))
```



## 인덱스

- Database에서 유래, 엑셀 등에서 용어를 사용하기도 함

- 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작다. 왜냐하면 보통 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문

- 배열을 사용한 인덱스

  - 대량의 데이터를 매번 정렬, 프로그램의 반응은 느려질 수 밖에 없음 이러한 대량 데이터의 성능 저하 문제를 해결하기 위해 배열 인덱스를 사용할 수 있음 

  - 원본 데이터에 데이터가 삽입될 경우 상대적으로 크기가 작은 인덱스 배열을 정렬하기 때문에 속도가 빠름



## 선택 정렬

- 가장 작은 값의 원소부터 차례대로 선태하여 위치를 교환
- 시간 복잡도 O(n^2) -> for문 2개
- 비교와 교환, 교환의 회수가 버블, 삽입정렬보다 작다
- 정렬 과정
  - 주어진 리스트 중 최소값을 찾음
  - 그 값을 리스트의 맨 앞에 위치한 값과 교환
  - 맨 처음 위치를 제외한 나머지 리스트 대상으로 위 과정 반복

```python
def Selection sort(a):
    for i in range(0,lena(a-1)):
       # 최소값찾기
    	min = i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min = j
             #최소값과 앞으로 위치 변환(swap)
            a[i], a[min] = a[min], a[i]
```

- 배열은 참조형이라 원본도 바뀜, key값 같은 것은 value라 원본이 바뀌지는 않고 copy함

```python
def selectionSort(a):
    # i : 0 ~ len(a)-1
    for i in range(len(a)-1): #0,1,2,3 
        #최소값 찾기
        min = i
        for j in range(i+1,len(a)): #자기보다 하나 큰거부터 끝까지
            if a[min] > a[j]:
                min = j #min은 idx
        #바꿔치기를 한다
        a[i], a[min] = a[min], a[i]

arr = [64,25,10,22,11]
selectionSort(arr)
print(arr)
```



## 셀렉션 알고리즘

- k번째로 큰 혹은 작은 원소 찾는 방법
- 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미
- 정렬 알고리즘을 이용하여 자료 정렬, 원하는 순서의 원소 가져오기

```python
#seliection 알고리즘
def selection(a,k):
    # i : 0 ~ len(a)-1
    for i in range(len(a)-1): #0,1,2,3 
        #최소값 찾기
        min = i
        for j in range(i+1,len(a)): #자기보다 하나 큰거부터 끝까지
            if a[min] > a[j]: #a[min] < a[i]이거 바꿔주면 내림차순으로 바꿀 수 있음
                min = j #min은 idx
        #바꿔치기를 한다
        a[i], a[min] = a[min], a[i]
    return a[k-1] #0부터시작했기 때문에 -1을 해줌
arr = [64,25,10,22,11]
selectionSort(arr)
print(selection(arr,3))
```



## SWEA 1954. 달팽이 숫자

- 델타검색
- 값, 벽과 만나면 옆으로 꺾기....

```python
cnt=1
arr=[[0]*5 for i in range(5)]

row_start=0
row_end=4
col_start=0
col_end=4

while row_start<=row_end and col_start<=col_end:
    # 왼쪽=> 오른쪽
    for i in range(col_start, col_end+1):
        arr[row_start][i]=cnt
        cnt+=1
    row_start +=1

    # 위=> 아래
    for i in range(row_start, row_end + 1):
        arr[i][col_end] = cnt
        cnt += 1
    col_end -= 1

    # 오른쪽=> 왼쪽
    for i in range(col_end, col_start-1, -1):
        arr[row_end][i]=cnt
        cnt+=1
    row_end -=1

    # 아래=> 위
    for i in range(row_end, row_start - 1, -1):
        arr[i][col_start] = cnt
        cnt += 1
    col_start += 1

print(arr)
```



## 데일리 테스트

- **여기서 -1-x가 아니라 -x만 해도 값이 같음 왜???

```python
import sys
sys.stdin = open("input.txt", "r")
#100X100의 2차원 배열이 주어짐
#각 행의 합, 각열의 합, 각 대각선의 합 중 최댓값을 구함
#각 행의 합은 integer 범위를 넘어가지 않음
#동일한 최댓값이 있을 경우, 하나의 값만 출력
TC = 10
for tc in range(1,TC+1): #100*100
#각 행값을 입력받음
    N_list = []
    T = int(input())#테스트케이스 번호
    for i in range(100):#100*100배열을 list에 한 행씩 담는다
        N = list(map(int,input().split()))
        N_list.append(N)

    SUM = [] #합을 저장할 list

#1)같은 행끼리 합[(열+1씩)을 행 idx개수만큼]=가로
    for x in range(len(N_list)):#한 행이 더해지고 +1씩 행이 넘어감
        sum_row = 0 #한 행당 합 초기화
        for y in range(len(N_list)): #반복될 열 개수
            sum_row += N_list[x][y] #같은 행의 데이터를 더함
        SUM.append(sum_row) #SUM에 합을 추가함

#2)같은 열끼리 합[(행+1씩)을 열 idx개수만큼]=세로
    for y in range(len(N_list)):#한 열이 더해지고 +1씩 열이 넘어감
        sum_col = 0
        for x in range(len(N_list)): #같은 열의 데이터를 더함 원소
           sum_col += N_list[x][y] #행1칸씩 다음으로 넘어가며 합함
        SUM.append(sum_col) #한 행 다 더하면 SUM에 담음

# 3)(행+1씩,열+1씩) 합1개=대각선
    hap1 = 0
    for x in range(len(N_list)):#+1씩늘어나는 행 idx
        for y in range(len(N_list)): #+1씩 늘어나는 열 idx
            if x == y: #(0,0)(1,1) 행 열 idx 같을때
                hap1 += N_list[x][y]
    SUM.append(hap1)

# 4)(행+1씩,열-1씩) 합1개=대각선
    hap2 = 0
    for x in range(len(N_list)):#+1씩 늘어나는 행 idx
        for y in range(len(N_list)): #찾아 볼 열idx
            if y == (len(N_list)-1-x) : #열의 개수-1=idx값에서 행 idx를 뺸 값
                #**여기서 -1-x가 아니라 -x만 해도 값이 같음 왜???
                hap2 += N_list[x][y]
    SUM.append((hap2))
    print('#{} {}'.format(tc,max(SUM)))

#출력
#1 1712
#2 1743
#3 1713
#4 1682
#5 1715
#6 1730
#7 1703
#8 1714
#9 1727
#10 1731

```

