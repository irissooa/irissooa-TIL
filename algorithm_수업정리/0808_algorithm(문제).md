# SWEA

## 어디에 단어가 들어갈 수 있을까(SWEA_1979)

- 처음에 문제를 잘 못읽고 가로에만 들어갈 수 있는 것을 찾았당.. 문제를 잘읽자!

```python
#N*N을 2차배열로 만든다
#가로의 길이가 k만큼인 것이 몇개인지 구하라
#2차배열을 받고
#가로를 보는데 만약 1이 나왔을 때 그담이 0이면 그사이 수를 세어본다
#그렇게 나온 합들이 K인지 확인, K라면 result += 1을 해라
#세로도 마찬가지로 진행한다

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N, K = map(int,input().split())
    arr = []

    result = 0
    for _ in range(N):
        temp = list(map(int,input().split()))
        arr.append(temp)

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if cnt == K:
                    result += 1
            else:  # 값이 0일때
                cnt = 0
            if cnt > K: #cnt가 K가 넘으면
                result -= 1 #위에서 더해졌던걸 하나 빼주고 cnt를 리셋시켜라
                cnt = 0 #그 뒤에 맞는 단어가 있을 수 있음

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                if cnt == K:
                    result += 1
            else:  # 값이 0일때
                cnt = 0
            if cnt > K: #cnt가 K가 넘으면
                result -= 1 #위에서 더해졌던걸 하나 빼주고 cnt를 리셋시켜라
                cnt = 0


    print(f'#{tc} {result}')
```

- 병훈 천사님이 코드 주석을 달아두셨당👍

```python
# find_row 함수는 행에서 단어가 들어갈 수 있는곳 찾기
# N*N 행렬 
# index 0인  열에서는 1이 K개 나오고 0이 K+1 번째  나와야한다 
# index 마지막 열에서는 1이 K개 나오고 N-1-K 번째 열이 0 
# 나머지는 0 1 1 1 1 ...(K개) 0
# find_col 함수는 입력된 행렬을 90도 시계방향 회전 후 find_row 함수 호출
def find_row(arr,K):
    count = 0
    for i in range(N):
        if sum(arr[i][0:K]) == K and arr[i][K] == 0:
            count += 1
        if sum(arr[i][N-K:N])==K and arr[i][N-K-1]==0:
            count += 1
        for j in range(1,N-K):
            if sum(arr[i][j:j+K]) == K and arr[i][j-1]==0 and arr[i][j+K]==0:
                count+=1
    return count
 
def find_col(arr,K):
    rot_arr = [ [0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rot_arr[i][j]=arr[N-1-j][i]
    return find_row(rot_arr,K)
 
for t in range(1,int(input())+1):
    N,K = map(int,input().split())
    arr = [ list(map(int,input().split())) for _ in range(N)]
    print(f'#{t} {find_row(arr,K)+find_col(arr,K)}')
```



## 시각 덧셈(SWEA_1976)

- 이건 생각했던대로 잘 나왔당
- 코드를 더 줄여보도록 하쟈!!!

```python
#시와 분이 2개씩 주어지고 그값들을 더한값을 출력한다
#시와 분을 입력받는다
#시는 시끼리 분은 분끼리 더하는데 분끼리 더했을 때 60이 넘으면 -60을 하고, 시에+1을 해줌
#시가 12시가 넘으면 -12를 한 값을 출력함

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    h1,m1,h2,m2 = map(int,input().split())
    m_sum = m1 + m2
    h_sum = h1 + h2
    if m_sum >= 60: #분끼리 더했을 때 60이상이면 -60을 하고, 1+시간 더해줌
        m_sum -= 60
        h_sum += 1
    if h_sum >= 12:
        h_sum -= 12
    print(f'#{tc} {h_sum} {m_sum}')
```



## 쉬운 거스름돈(SWEA_1970)

- 이거는 더 줄여서 풀수 있을것같은데... 어떻게..

```python
#거스름돈을 입력받고 거스름돈을 최소한의 개수로 줄 수 있는 방법
#단순하게..생각하면
#5만원, 만원, 5천, 천, 오백, 백, 오십, 십원 이렇게 범위를 정하고 그 사이면 그 값과 나눈몫 만큼 더해주고, 그 값만큼 빼면..되지않을까
#문자열에 그 개수만큼 공백과 함꼐 추가함

import sys
sys.stdin = open("input.txt", "r")



for tc in range(1,int(input())+1):
    N = int(input())
    str_remain = []
    cnt = 0
    if N >=50000:
        cnt = N // 50000
        N -= cnt * 50000
        str_remain.append(cnt)
    else :
        str_remain.append(0)
    if N >= 10000:
        cnt = N // 10000
        N -= cnt * 10000
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N >= 5000:
        cnt = N // 5000
        N -= cnt * 5000
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N>= 1000:
        cnt = N // 1000
        N -= cnt * 1000
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N >= 500:
        cnt = N // 500
        N -= cnt * 500
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N >= 100:
        cnt = N // 100
        N -= cnt * 100
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N >= 50:
        cnt = N // 50
        N -= cnt * 50
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N >= 10 : #10원
        cnt = N // 10
        N -= cnt * 10
        str_remain.append(cnt)
    else:
        str_remain.append(0)

    print(f'#{tc}')
    STR = ''
    for s in str_remain:
        # STR += str(s)
        print(f'{str(s)}',end = ' ')
    print()
```

- #내코드 줄이기

```python
#거스름돈 리스트를 만든다
#리스트를 돌면서 입력된 N을 money에 나눈 몫을 세어주고 그 cnt를 어딘가에 저장함
#그리고 N을 그 나누어진 만큼 빼줌

money = [50000,10000,5000,1000,500,100,50,10]
for tc in range(1,int(input())+1):
    N = int(input())
    remain = ''
    for m in money:
        cnt = N//m #money하나씩 돌면서 몫이 그 거스름돈 개수이다
        remain += str(cnt) + ' ' #그 거스름돈 개수를 str에 공백과 함께 저장해줘라
        N -= cnt * m #N값을 다시 재설정 해줘라
    print(f'#{tc}\n{remain}')
```

