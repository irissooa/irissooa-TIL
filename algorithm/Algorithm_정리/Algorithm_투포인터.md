# Algorithm_투포인터

[toc]

## 투 포인터

### 1) 투 포인터란?

> 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘

- 주로 배열 안에 있는 값들을 연속해서 더하거나 연산하는 경우에 사용되며, 인덱스를 가리키는 두 개의 변수(포인터)를 선언하여 사용하는 특징이 있어 **투 포인터**라 불림.

#### 1. '특정한 합을 가지는 부분 연속 수열'문제에 적용가능

```python
n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end 를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
    
print(count) # 3
```

- 투포인터는 시간을 줄이기 위해 하는건데 위에 풀이는 심하면 n^2이 됨! 그래서 아래와 같이 풀어야됨

```python
N, M = map(int,input().split())
arr = list(map(int,input().split()))
start = end = hab = ans = 0
while True:
    if hab == M:
        #print(start,end)
        ans += 1
        
    #end가 N에 가서도 hab이
    if hab >= M:
        hab -= arr[start]
        start += 1
    elif end == N:
        break
    elif hab < M:
        hab += arr[end]
        end += 1
print(ans)
```





#### 2. 부분집합의 합 다른 풀이

예를 들어 N개의 숫자가 들어있는 배열이 주어질 때, 부분 집합의 합이 특정 숫자인 M인 경우의 수를 구하는 문제에 적용한다면, 

배열의 인덱스를 가리키는 startPointer와 endPointer를 생성한 후 특정 규칙에 의해 각 포인터를 움직여 배열을 탐색해 문제를 해결할 수 있으며,

 그 규칙은 다음과 같다.

1. 현재까지의 합이 M보다 크거나 같은 경우 합에서 endPoiner가 가리키고 있는 값을 뺀 후 endPointer를 +1 증가시킴

2. 만약 startPointer의 값이 배열의 길이와 같을 경우 탐색을 종료함

3. 나머지 경우(현재까지의 합이 M보다 작을 경우)에는 합에 startPointer가 가리키고 있는 값을 더한 후 startPointer를 +1 증가시킴



**위의 세 규칙 중 해당하는 연산이 끝난 후 만약 현재까지의 합이 M과 같다면 답을 +1증가 시킴**

**WHY??**

그렇다면, 왜 투 포인터를 사용할까?

만약, 위와 동일한 문제를 완전 탐색을 적용하여 해결할 시 N만큼 반복문 2번을 돌리게 되므로 O(n²)의 시간 복잡도가 걸리게 됨

하지만, 투 포인터를 사용한다면 한 번 답이 될 수 없다고 판명된 이후의 값들을 더 이상 탐색하지 않으므로(어차피 답이 될 수 없기 때문에) 시간 복잡도가 O(n)이 되어 완전 탐색에 비해 효율이 훨씬 좋아짐

따라서, 시간제한이 넉넉하지 않아 완전 탐색을 적용하여 해결하지 못하는 문제일 경우, 투 포인터를 적용하여 해결할 수 있다.

 

다만, 이 경우엔 **배열의 원소가 자연수**여야 하는 제약조건이 따르게 되므로 투 포인터를 사용할 땐 꼭 문제의 조건을 확인하여 알맞은 상황에만 사용해야 하며, 포인터를 움직이는 규칙 또한 문제에 맞추어 변형해야함!!



코드는 위에서 예시로 든 문제를 해결하는 템플릿이며, 백준 2003번 수들의 합 2 문제와도 같다.

 ```python
N, M = 7, 5
arr = [1, 2, 3, 7, 5, 4, 3]
 
# 시작 포인터
startPointer = 0
# 끝 포인터
endPointer = 0
# 현재까지의 합
tot = 0
# 현재까지의 합이 M인 경우의 수
ans = 0
 
while(True):
    # 규칙 1.
    if tot >= M:
        tot -= arr[endPointer]
        endPointer += 1
    # 규칙 2.
    elif startPointer == len(arr):
        break
    # 규칙 3.
    else:
        tot += arr[startPointer]
        startPointer += 1
    
    # 규칙 2)
    if tot == M:
        ans += 1
 
print(ans)  # 출력결과 : 2
 ```







#### 3. 정렬되어 있는 두 리스트의 합집합에도 활용할 수 있다.

- 이는 병렬정렬(Merge Sort)의 Conquer영역의 기초가 되기도 한다.

1. 정렬된 리스트 A와 B를 입력받는다.
2. 리스트 A에서 처리되지 않은 원소 중 가장 작은 원소를 i가 가리키도록 한다.
3. 리스트 B에서 처리되지 않은 원소 중 가장 작은 원소를 j가 가리키도록 한다.
4. A[i]와 B[j]중에서 더 작은 원소를 결과 리스트에 담는다.
5. 리스트 A와 B에서 더 이상 처리할 원소가 없을 때까지 2~4번 과정을 반복한다.

```python
# 사전에 정렬된 리스트 A와 B 선언
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 리스트 A와 B의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화
result = [0] * (n + m)
i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i < n or j < m:
    # 리스트 B의 모든 원소가 처리되었으나,리스트 A의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]):
        # 리스트 A의 원소를 결과 리스트로 옮기기
        result[k] = a[i]
        i += 1
    # 리스트 A의 모든 원소가 처리되었거나, 리스트 B의 원소가 더 작을 때
    else:
        # 리스트 B의 원소를 결과 리스트로 옮기기
        result[k] = b[j]
        j += 1
    k += 1
    
# 결과 리스트 출력
for i in result:
    print(i, end=' ') # 1 2 3 4 5 6 8
```



## 관련문제

### BOJ_2003_수들의합2

> [2003_수들의합2](https://www.acmicpc.net/problem/2003)  
>
> ### **투포인터 알고리즘**
>
> [참고](https://velog.io/@koyo/python-two-pointer)
>
> 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘
>
> 예를 들면, 학생 40명이 순서대로 일렬로 세워져 있는 경우, 1번부터 10번까지 라고 부르듯 시작점과 끝점 2개의 점을 통해 데이터의 범위를 표현할 수 있다.
>
> #### 1. '특정한 합을 가지는 부분 연속 수열'문제에 적용가능
>
> ```python
> n = 5 # 데이터의 개수 N
> m = 5 # 찾고자 하는 부분합 M
> data = [1, 2, 3, 2, 5] # 전체 수열
> 
> count = 0
> interval_sum = 0
> end = 0
> 
> # start를 차례대로 증가시키며 반복
> for start in range(n):
> # end 를 가능한 만큼 이동시키기
> while interval_sum < m and end < n:
>   interval_sum += data[end]
>   end += 1
> # 부분합이 m일 때 카운트 증가
> if interval_sum == m:
>   count += 1
> interval_sum -= data[start]
> 
> print(count) # 3
> ```
>
> #### 2. 정렬되어 있는 두 리스트의 합집합에도 활용할 수 있다.
>
> 이는 병렬정렬(Merge Sort)의 Conquer영역의 기초가 되기도 한다.
>
> 다음과 같다.
>
> 1. 정렬된 리스트 A와 B를 입력받는다.
> 2. 리스트 A에서 처리되지 않은 원소 중 가장 작은 원소를 i가 가리키도록 한다.
> 3. 리스트 B에서 처리되지 않은 원소 중 가장 작은 원소를 j가 가리키도록 한다.
> 4. A[i]와 B[j]중에서 더 작은 원소를 결과 리스트에 담는다.
> 5. 리스트 A와 B에서 더 이상 처리할 원소가 없을 때까지 2~4번 과정을 반복한다.
>
> ```python
> # 사전에 정렬된 리스트 A와 B 선언
> n, m = 3, 4
> a = [1, 3, 5]
> b = [2, 4, 6, 8]
> 
> # 리스트 A와 B의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화
> result = [0] * (n + m)
> i = 0
> j = 0
> k = 0
> 
> # 모든 원소가 결과 리스트에 담길 때까지 반복
> while i < n or j < m:
>     # 리스트 B의 모든 원소가 처리되었으나,리스트 A의 원소가 더 작을 때
>     if j >= m or (i < n and a[i] <= b[j]):
>         # 리스트 A의 원소를 결과 리스트로 옮기기
>         result[k] = a[i]
>         i += 1
>     # 리스트 A의 모든 원소가 처리되었거나, 리스트 B의 원소가 더 작을 때
>     else:
>         # 리스트 B의 원소를 결과 리스트로 옮기기
>         result[k] = b[j]
>         j += 1
>     k += 1
>     
> # 결과 리스트 출력
> for i in result:
>     print(i, end=' ') # 1 2 3 4 5 6 8
> ```

- 처음에는 완전탐색으로 풀었다. -> 시간초과! 하나하나 다 살펴보기엔 너무 시간이 많이든다.

```python
N,M= map(int,input().split())
nums = list(map(int,input().split()))
# print(nums)
cnt = 0
for i in range(N):
    total = 0
    for j in range(i,N):
        # print(j)
        total += nums[j]
        if total == M:
            cnt+=1
            break
print(cnt)
```

- 투포인터 알고리즘으로 풀어봤다.

> 이 알고리즘은 부분합을 구할 때 많이 이용되고 다른 문제에도 응용되니까 잘 익혀두자

```python
'''
처음에는 완전탐색으로 풀었는데 시간초과가 남
찾아보니까 '투포인터 알고리즘'을 이용함!
'''

#수열의 개수N, 찾고자하는 부분합M
N,M= map(int,input().split())
#수열리스트
nums = list(map(int,input().split()))
# print(nums)
cnt = 0
interval_sum=0
end = 0
#start를 차례대로 증가시키며 반복
for start in range(N):
    #end를 가능한만큼 이동시키기
    while interval_sum < M and end < N:
        interval_sum += nums[end]
        end += 1
    #부분집합 M일때 카운트 증가
    if interval_sum == M:
        cnt+=1
    #end가 멀어질때 제일 앞의 수를 뺴면서 합을 구함
    interval_sum -= nums[start]
print(cnt)
```

- 투포인터는 시간을 줄이려고 하는건데 위에 풀이는 심하면 n^2이 됨! 그래서 아래와같이 풀어야됨

```python
N, M = map(int,input().split())
arr = list(map(int,input().split()))
start = end = hab = ans = 0
while True:
    if hab == M:
        #print(start,end)
        ans += 1
    if hab >= M:
        hab -= arr[start]
        start += 1
    elif end == N:
        break
    elif hab < M:
        hab += arr[end]
        end += 1
print(ans)
```



## 카카오 보석





## Reference

[투포인터개념_hellominchan](https://hellominchan.tistory.com/252)

[투포인터_koyo](https://velog.io/@koyo/python-two-pointer)