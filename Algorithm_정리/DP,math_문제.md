# 다이나믹프로그래밍 DP

[toc]

## 다이나믹프로그래밍(DP)

> [출처 : 다이나믹 프로그래밍(DP)](https://infinitt.tistory.com/246)

- 개념 : 문제를 더 작은 단위로 쪼개어 해결하는 알고리즘. **(분할 정복 알고리즘과 비슷하다.)**
- 핵심은, **그 작은 단위의 문제들이 반복해서 일어나기 때문에, 그값들을 저장해놓는 식으로 해결해나가는 알고리즘**
- **(다이나믹이라는 이름에는 아무 뜻도 없다고 한다.)** 



### **다이나믹 프로그래밍을 사용하기 위한 조건**

**1. 부분 문제들이 겹치는가 (반복 되는가)**  

  ex ) 피보나치 수 : **N번째 항**(큰 문제) = **N-1번째 항**(작은 문제) + **N-2 번째 항**(작은 문제)

- 피보나치의 특성을 잘 살펴보면 Fibo(10)을 구할때는 `Fibo(9)+Fibo(8)....Fibo(1)` 까지 모두 필요함
-  이때 메모이제이션을 통해 배열에 저장해놓는다면, Fibo(12)를 구할때는 , 1~10번째 항까지 이미 메모가 되어있으므로, 11번째 항만 연산하면 되므로 효율적

> *** 재귀함수로 구현한 피보나치 (Python)**

```python
def fibonacci(n):
	if n<=1 :
		return n
	
	else : return fibonacci(n-1) + fibonacci(n-2)
```

 

> **다이나믹 프로그래밍으로 구현한 피보나치 (memoization)**
>
> **한번 거쳤던 항들은 모두 memo에 저장된다. **
>
> **따라서, 다음에 구할때는 연산없이 리턴이 가능하다.**

```python
memo = [0 for i in range(100)]
def fibonacci(n):
	if n<=1 :
		return n
	
	else :
		if memo[n] > 0 :
			return memo[n] 
		memo[n] = fibonacci(n-1) + fibonacci(n-2)
		return memo[n]
```

​    



**2. 최적 부분 구조** 

> 문제의 정답을 작은 문제의 정답으로부터 구할 수 있는가

- ex ) 최단경로 구하기 :

> **A에서 C**로 가는 최단경로 (큰 문제) = **A에서 B**로가는 최단경로(작은 문제) + **B에서 C**로가는 최단경로(작은 문제)

- 따라서, **정답을 한번 구했으면 Memoization** 하여, 반복연산을 없애는 과정이 중요하다.

 

### 다이나믹 프로그래밍 구현



#### 1. **Top - down : 위에서 아래로 해결한다. (ex : 재귀함수)**

1. **문제를 쪼갠다.**
2. **작은 문제를 푼다.**
3. **작은 문제의 정답으로 큰 문제를 해결한다.**



#### 2. **bottom - up : 아래에서 위로 (ex : 반복문)**

1. **작은 문제부터 풀어나간다.**
2. **문제의 크기를 점점 크게 만들어 푼다.**
3. **작은 문제들을 해결했기 때문에, 한단계 위의 큰 문제를 풀 수 있다.**
4. **최종적인 문제를 해결한다.**

  

**시간복잡도는 비슷한 수준이며, *문제에 따라 구현하기 편한것을 선택*하여 풀면 된다. (즉, 어떤것으로 풀어도 큰 상관은 없다) 다만 파이썬 같은경우는 재귀로 풀게되면 메모리초과가 날 가능성이 타 언어보다 높기 때문에, 반복문(bottom_up)으로 푸는게 낫다고 한다.**



### **문제를 해결할때**

- **점화식**을 정의한다.
- 문제를 어떠한식으로 쪼갤지 (작게 만들지) 생각한다.
- 작은 문제의 답을 통해 어떻게 최종적인 문제를 해결할 수 있을지 생각한다.

 

## DP 관련 문제

### BOJ_1463_1로 만들기

> [1463_1로만들기](https://www.acmicpc.net/problem/1463)문제
>
> 풀다가....결국 구글링 😂😂 찾아보니 점화식, bfs로 푼 플이들을 찾았다.

#### 1. 점화식으로 풀기

- N이라는 수는 N//3을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.
- N이라는 수는 N//2을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.
- N이라는 수는 N-1을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.

따라서 !!! **점화식 : dp(N) = min ( dp(N//3) +1, dp(N//2)+1 , dp(N-1)+1 )**

```python
n = int(input())

#n+1개만큼의 0으로 이루어진 배열을 만들어줌
dp = [0 for _ in range(n+1)]

#dp라는 배열의 index는 문제의 입력nr과 대응하고, index의 값은 연산최솟값(문제의 출력)에 대응
for i in range(2, n+1):
    #1.
    dp[i] = dp[i-1] + 1  
    
    #2.
    if i%2 == 0 and dp[i] > dp[i//2] + 1 :
        dp[i] = dp[i//2]+1
        
    if i%3 == 0 and dp[i] > dp[i//3] + 1 :
        dp[i] = dp[i//3] + 1
        
print(dp[n])
```

**#1.**

dp[i] 현재 값의 배열에 들어갈 수는 현재값에서 1을 뺀 수의 배열값에 1을 더한 수

WHY??

dp배열의 현재 index에 앞으로 할 행동(1빼기)을 한 뒤의 index dp배열값에  +1(연산추가:행동을 했기 때문!)을 한 값을 넣어줌!

n에서부터 시작하는 것이 아니라 작은수부터 n으로  for문을 돌면서 연산 수를 셀것이기 때문



**#2.**

만약 2로 나누어떨어지는데 

`dp[i] > dp[i//2] + 1` 이 조건이 True라면,

dp[i] 자리에 넣을 더 작은 값을 찾았다는 뜻!

그럼 그 배열의 값을 더 작은 값으로 갱신해줌!

3으로 나눠떨어지는 것도 마찬가지!





**+ 시간복잡도**

배열의 크기 * O(1)이다. (배열 하나당 O(1)의 시간복잡도를 가지므로)

배열은 n+1이므로 **시간복잡도는 O(n)**

 

#### 2. BFS로 풀기

> [출처:poorman.tistory](https://poorman.tistory.com/421)

1. 너비우선탐색(BFS) 알고리즘을 이용하여 N 값이 1이 될때까지 탐색한다.

2. FIFO 큐를 사용하기 위해서 collections.deque를 이용하여 popleft로 값을 꺼낸 후에 새로운 노드를 append한다.

3. 노드 값은 [value, count] 형태로 사용하고 너비 우선 탐색이므로 value가 1이 되는 순간의 count를 리턴한다.

```python
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

def BFS(x):
    cnt = 0
    Q = deque([(x,cnt)])
    while(Q):
        x,cnt = Q.popleft()
        if x == 1:
            return cnt
        if x % 3 == 0:
            Q.append([x//3,cnt+1])
        if x % 2 == 0:
            Q.append([x//2,cnt+1])
        Q.append([x-1,cnt+1])
    return -1

print(BFS(N))
```

수행시간 : 2372ms



* 여기서 궁금한점!

cnt가 최소인지는...bfs라서 아는걸까....bfs는 최솟값을 구하는데 쓰기 때문에...





#### 3. DFS

> [출처:poorman.tistory](https://poorman.tistory.com/421)

1. 깊이우선탐색(DFS) 알고리즘을 이용하여 N 값이 1이 될때까지 탐색한다.

2. LIFO 스택을 사용하여 pop으로 값을 꺼낸 후에 새로운 노드를 append한다.

3. 노드 값은 [value, count] 형태로 사용하고 value 값이 1이 되는 순간의 count값으로 min_count의 최소 값을 갱신한다.

4. 최소 count 값만 구하면 되기 때문에 min_count보다는 더 깊게 탐색하지 않는다.

5. 깊이 우선 탐색이 모두 끝났을 때 min_count값을 리턴한다.

```python
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
def DFS(x):
    min_cnt = x
    cnt = 0
    Q = deque([(x,cnt)])
    while(Q):
        x,cnt = Q.pop()
        if cnt >= min_cnt:
            continue
        if x == 1:
            min_cnt = min(min_cnt, cnt)
        Q.append([x-1,cnt+1])
        if x % 2 == 0:
            Q.append([x//2,cnt+1])
        if x % 3 == 0:
            Q.append([x//3,cnt+1])
    return min_cnt

print(DFS(N))
```

수행시간 : 1272ms

*** 해당 문제는 BFS/DFS의 탐색에 시간이 많이 소요되어 비효율적이다.**



#### 4. 재귀함수

1. 재귀함수를 이용하여 현재 위치에 도달하는 최소 코스트를 리턴한다.

2. 현재 위치의 최소 코스트에 도달하기 위해서는 2,3으로 나누어 떨어지는 거리(x//2,x//3) + 나머지 거리(x%2,x%3) + 1이다. f(x) = min( f(x//3) + x%3 + 1, f(x//2) + x%2 + 1)

3. 거리가 1일때는 0, 거리가 2,3일때는 1의 코스트가 든다. f(1) = 0, f(2) = 1, f(3) = 1

```python
import sys
input = sys.stdin.readline

N = int(input())
def fnc(x):
    if x == 1:
        return 0
    elif x <= 3:
        return 1
    return min(fnc(x//3) + x%3 + 1, fnc(x//2) + x%2 + 1)
print(fnc(N))
```

수행시간 : 72ms



### BOJ_11726_2xn 타일링

> [11726_2xn 타일링 문제](https://www.acmicpc.net/problem/11726)

2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하시오
규칙을 찾아보니 n이 1일때 1, 2일때 2, 3일때 3, 4일때 5, 5일때 8 등의 경우의 수가 나온다.

| **입력 N**    | **1** | **2** | **3** | **4** | **5** | **6**  |
| ------------- | ----- | ----- | ----- | ----- | ----- | ------ |
| **방법의 수** | **1** | **2** | **3** | **5** | **8** | **13** |

n>=3일때 `f(n) = f(n-1) + f(n-2)`가 나옴!!
여기서 출력으로 10007로 나눈 나머지를 출력하면 됨!

점화식을 찾았다! 그런데 처음 답을 제출했을 때 `print(dp[n]%10007)`이렇게 제출했을때는 답이 틀리다고 나왔다. 그리고 저 식을 ans라는 변수에 따로 넣어주고 print를 했더니 성공! 왜지???

```python
'''
2020/10/24/09:35~09:55
'''
n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    if i < 3:
        dp[i] = i
    else:
        dp[i] = dp[i-1] + dp[i-2]
ans = dp[n]%10007
print(ans)
```



### BOJ_s11727_2xn타일링2

> [11727_2xn타일링2](https://www.acmicpc.net/problem/11727)

2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성
이건.....규칙을 못찾겠어서 힌트를 봤다..ㅠ

이전에 풀었던11726_2xn타일링 문제와 다른점! : **2를 채울 때에는 두가지 방법이 있기 때문에 2를 채울때마다 2를 곱해주어야 한다.**



n

1 - 1가지

2 - 3가지

3 - 5가지

4 - 11가지

이 코드의 아이디어는 간단하다. 2xN의 타일링을 위해서는 **총 세 가지 경우**가 존재하게 된다.

**1.** 2x(N-1)만큼 타일링하고 2x1 타일을 붙인다.

**2-1.** 2x(N-2)만큼 타일링하고 1x2 타일을 두 개 붙인다.

**2-2.** 2x(N-2)만큼 타일링하고 2x2 타일을 한 개 붙인다.

 

따라서 2xN에 타일링할 수 있는 경우의 수를 dp(N)이라 할 때, *dp(N) = dp(N-1) + dp(N-2) \* 2* 가 된다. 코드는 아래와 같이 작성을 했으며 첫 번째 방법을 이해 못 했다면 이 방법을 이해하고 보면 이해가 될 것 같다.



> 여기서 처음에 dp[1]=1,dp[2]=3 이라고 주니까 런타임 에러뜸! n=1일때 dp[2]가 없기 때문!

```python
n=int(input())
dp=[0 for _ in range(n+1)]

for i in range(1,n+1):
    if i == 1:
        dp[i] = 1
    elif i ==2:
        dp[i] = 3
    else:
        dp[i] = dp[i-1] + dp[i-2] *2
ans = dp[n] %10007
print(ans)
```



### BOJ_9095_1,2,3더하기

>[BOJ_9095_1,2,3더하기](https://www.acmicpc.net/problem/9095)

``` python
'''
규칙을 살펴보자.
1 = (1)
2 = (1 + 1), (2)
3 = (1 + 1 + 1), (1 + 2), (2 + 1), (3)
4 = (1 + 1 + 1 + 1), (1 + 1 + 2), (1 + 2 + 1), (1 + 3), (2 + 1 + 1), (2 + 2), (3 + 1)
4에서 맨처음 더해지는 숫자들 4개를 보자.
1에 위의 3에서 더해졌던 숫자들이 더해지는것을 볼 수 있다.
그 다음 2에 2에서 더해졌던 숫자들이 더해진다.
3은 1에서 더해졌던 숫자들이 더해진다.
4는
1 + 3
2 + 2
3 + 1로 나타낼 수 있는데, 3의 개수, 2의 개수, 1의 개수를 다 더해주면 4의 개수가 된다.
'''
import sys
sys.stdin = open('input.txt','r')

#N이 1일때 1가지, 2일때 2가지 3일때 4가지, 점화식은 N >3일떄부터!
dp = [1,2,4]
for n in range(3,12):
    dp.append(dp[n-1] + dp[n-2] + dp[n-3])
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(dp[N-1])

```



### BOJ_10610_30

> [10610_30](https://www.acmicpc.net/problem/10610)

```python
'''
30의 배수가 되는 가장 큰 수 조합
1. 0을 포함해야됨
2. 다 더했을 때 3의 배수
3. 내림차순 정렬! 가장 큰수
'''
import sys
sys.stdin = open('input.txt','r')

#문자열로 받아야 따로 분리가능
# N = sorted(input(),reverse=True)
N = input()
numbers = sorted(N,reverse=True)
LEN = len(N)
#0을 포함해야됨
if '0' in numbers:
    total = 0
    result = ''
    for i in range(LEN):
        total += int(numbers[i])
        # result += numbers[i]
    if total %3 ==0:
        # print(*numbers,sep='')
        # print(result)
        ans = ''.join(numbers)
        print(ans)
    #여기에 else를 안적어줘서 답이 계속 틀렸다고 나옴!!! 3의배수가 아닐때 값을 지정해주지 않음..
    else:
        print(-1)
else:
    print(-1)
```

- 아래와 같이 줄일수도 있음

```python
'''
30의 배수가 되는 가장 큰 수 조합
1. 0을 포함해야됨
2. 다 더했을 때 3의 배수
3. 내림차순 정렬! 가장 큰수
'''


#문자열로 받아야 따로 분리가능
N = sorted(input(),reverse=True)
LEN = len(N)
#0을 포함해야됨
if '0' in N:
    total = 0
    
    for i in range(LEN):
        total += int(N[i])
    if total %3 ==0:
        print(*N,sep='')
    else:
        print(-1)
else:
    print(-1)
```



### BOJ_11729_하노이 탑 이동순서

> [BOJ_11729_하노이 탑 이동순서](https://www.acmicpc.net/problem/11729)

```python
'''
모르겠어서 보고 풀었다ㅠㅠㅠ
#1. n개의 원판이 있을 때, n-1개의 원판 즉, 맨 밑의 원판을 제외하고 나머지 원판을 1->2번으로 옮긴뒤
맨 밑의 원판을 1번에서 3번으로 옮김
#2. n-1개의 원판들을 다시 2번에서 3번으로 옮김

이해는 하겠는데...넘 어렵....ㅠㅠㅠㅠㅠㅠ다시짤수있을까아아ㅏ...헣....
'''
def move(n,one,two,three):
    #종료 n이 1이되면 맨 밑의 원판을 1번에서 3번으로 옮기니 one,three출력
    if n == 1:
        # print(n,'11',one,three,two)
        print(one,three)
    else:
        #n-1(맨밑원판 제외)의 원판을 1번에서 2번으로 옮김
        move(n-1,one,three,two)
        print(one,three)
        # print(n,'22',one,three,two)
        move(n-1,two,one,three)

N = int(input())
one = [i for i in range(1,N+1)[::-1]]
SUM = 1
for i in range(N-1):
    SUM = SUM*2 + 1
print(SUM)
move(N,1,2,3)
```



- 챌's code

```python
def hanoi(n,from_pos,to_pos,aux_pos):
    if n==1:
        print(from_pos,to_pos)
        return

    #원반 n-1개를 auxpos로 이동
    hanoi(n-1,from_pos,aux_pos,to_pos)
    print(from_pos,to_pos)
    hanoi(n-1,aux_pos,to_pos,from_pos)

n=int(input())
print((2**n)-1)
hanoi(n,1,3,2)
```



### SWEA_1865_동철이의일분배

```python
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = 1 << N
    dp = [[0.0 for _ in range(M)] for _ in range(N)]

    G = []
    for i in range(N):
        G.append(list(map(float, input().split())))
        for j in range(N):
            G[i][j] = G[i][j] / 100

    for i in range(N):
        dp[0][1 << i] = G[0][i]

    for i in range(1, N):
        for cur in range(1, M):
            if dp[i - 1][cur] == 0:
                continue

            for j in range(N):
                if cur & (1 << j) != 0 or G[i][j] == 0:
                    continue
                next = cur | (1 << j)

                dp[i][next] = max(dp[i][next], dp[i - 1][cur] * G[i][j])
    print("#%d %.6f" % (test_case, dp[N - 1][M - 1] * 100))
```





-------

## Reference

[출처 : 다이나믹 프로그래밍(DP)](https://infinitt.tistory.com/246)

[출처: [poorman]]( https://poorman.tistory.com/421)