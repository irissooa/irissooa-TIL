# SWEA

## 숫자를 정렬하자(SWEA_1966)

- 나는 그냥...풀었는데 다음에 풀땐 알고리즘을 이용하자!
- 내장함수는 나중에 사용할줄알면 된다!

```python
#주어진 N길이의 숫자열을 오름차순으로 정렬하여 출력
#N을 입력받는다
#list로 받고, 정렬한 뒤 문자열로 바꿔줌

for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    arr_sorted = sorted(arr)
    str_arr = ''
    for i in arr_sorted:
        str_arr += ' ' + str(i)
    print(f'#{tc}{str_arr}')
```

- 버블정렬, 선택정렬로 푸는 법(병훈님👍👍)

```python
#버블정렬, 선택정렬 이용해서 품....대단해용..
#버블정렬로 푸는법
def bubble_sort():
    for i in range(N - 1):
        for j in range(i + 1, N):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

for t in range(1,int(input())+1):
    N = int(input())
    nums = list(map(int,input().split()))
    bubble_sort()
    print(f'#{t}',end=' ')
    [print(str(num),end=' ') for num in nums]
    print()

#선택정렬로 푸는법
def selection_sort():
    for i in range(N - 1):
        minIndex = i
        for j in range(i + 1, N):
            if nums[minIndex] > nums[j]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]


for t in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    selection_sort()
    print(f'#{t}', end=' ')
    [print(str(num), end=' ') for num in nums]
    print()
```



## 숫자 배열 회전(SWEA_1961)

- 90도씩 돌아가는 배열을 함수로 만들어 보쟈!
- `join`함수는 리스트를 구분자 없이 문자열로 바꿔주는 함수!

```python
#N*N행렬의 N을 입력받는다
#행렬을 입력받는다
#2차원배열을 만든다
#90도씩 돌아가는 함수를 만들수 있을까?
#90도 -> 180도 -> 270도 -> 360도(원점) 모두 90도씩 돌아가니까...
#2차배열을 90도로 전부 재배열
#배열을 계속 90도씩 재배열하며 한줄씩 출력을 함

def turnArr(arr):
    temp = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = arr[N-j-1][i]#90도 돌아가면 원래 위치에 뒤에서부터 행과 열이 바뀐상태로 들어온다
    return temp

for tc in range(1,int(input())+1):
    N = int(input())
    arr = [input().split() for i in range(N)] #2차배열을 숫자들을 문자로 받음
    # 2차배열을 각각 재설정 해줌
    turn90 = turnArr(arr)
    turn180 = turnArr(turn90)
    turn270 = turnArr(turn180)
    print(f'#{tc}')
    for i in range(N):
        #각각 90도로 돌아간 배열들의 각 idx리스트들을 구분자 없이 문자열로 변환시킴
        a = ''.join(turn90[i])
        b = ''.join(turn180[i])
        c = ''.join(turn270[i])
        print(f'{a} {b} {c}')
```



## 두 개의 숫자열(SWEA_1959)

```python
#Aj의 개수인 N개와 Bj의 개수인 M개를 입력받고
#Aj의 idx와 Bj의 idx에서 idx수가 작은것이 큰 idx범위 안에서
#마주보는 곱하고 모두 더한 값이 최대인 것 구하기

for tc in range(1,int(input())+1):
    N, M = map(int, input().split())
    Aj = list(map(int,input().split()))
    Bj = list(map(int,input().split()))
    MAX = []
    if N >= M:
        for i in range(N-M+1):  #큰 범위의 idx에 안 벗어나기 위해
            SUM = 0
            for j in range(M):
                SUM += Aj[i+j]*Bj[j]
            MAX.append(SUM)
    else: #M이 더 크면
        for i in range(M-N+1):  # 큰 범위의 idx에 안 벗어나기 위해
            SUM = 0
            for j in range(N):
                SUM += Aj[j] * Bj[i+j]
            MAX.append(SUM)
    print(f'#{tc} {max(MAX)}')
```

- 반복되는 것 두개를 쓰지 않고, 병훈님 코딩을 보니 Aj와 Bj중 Aj를 짧다고 설정하고 혹시 Aj가 더 길다면 Bj랑 바꿔 for문을 하나만 적어도 원활하게 돌아가게 만들었다

```python
#병훈
for t in range(1, int(input())+1):
    N,M = map(int,input().split())
    shorter = list(map(int, input().split()))
    longer = list(map(int, input().split()))
    if N>M: #짧다고 설정한게 더 길면 두개 위치를 바꿔라
        N, M = M, N
        shorter,longer =longer, shorter
    MAX = 0
    for k in range(M-N+1):
        multi = 0
        for i in range(N):
            multi+=shorter[i]*longer[k+i]
        if MAX < multi: #MAX함수 안쓰고 알고리즘으로!
            MAX = multi
    print(f'#{t} {MAX}')
```

