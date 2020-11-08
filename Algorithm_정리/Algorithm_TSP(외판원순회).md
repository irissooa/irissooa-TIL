# Algorithm_**외판원 순회(TSP: Traveling Salesperson Problem)**

[toc]

## 메모이제이션과 비트마스크를 이용!!

### SWEA_1865_동철이의일분배

- 다른사람코드(~~근데 이해안됨....나중에 다시 공부해보자~~)

```python
T = int(input())
for t in range(1,2):
    n=int(input())
    m=1<<n
    d=[0]*m
    #입력받은 수들에 각 0.01곱해서 저장
    p=[[*map(lambda x:x*.01,map(int,input().split()))]for _ in range(n)]
    print(p)
    d[0]=1
    for i in range(m):
        #i를 이진법으로 바꾸고 1의 개수를 세어줌
        x=bin(i).count('1')
        # print(x)
        for j in range(n):
            #j만큼1을 shift한 곳과 i의 비트 둘다 1이어야지만 1! 아니면 0
            if(1<<j)&i==0:
                print(j,i)
                #와...진짜......이해안감...0.....대박.이다...이분 천재다...ㅠ
                d[i|(1<<j)]=max(d[i|(1<<j)],d[i]*p[x][j])
    print(d)
    #d마지막 값에 저장된 것을 소수점 6째까지 표신
    print(f'#{t+1} {d[-1]*100:.6f}')
```

- 선생님 코드

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







## BOJ_109711_외판원순회2

> [BOJ_109711_외판원순회2](https://www.acmicpc.net/problem/10971)
>
> 원래는 순열구하는 함수를 만들려고 했는데, 이렇게 하니까..출력되는 p가 추가되는게 아니라..마지막 p가 여러번 append돼있다..ㅠ(WHY!!!!ㅠㅠㅠ.....)
>
>  **이유 => 얕은복사가 돼있기 때문에 p가 바뀌면 전부다 바뀌는 것! slicing이든 깊은복사로 해줘야됨!!**
>
> ```python
> #순열 구하는 함수
> #cost의 idx, 순열을 담을 list 길이, 방문표시할 리스트 길이
> def perm(nidx,p_len,v_len):
>  global idxLists
>  if nidx == p_len:
>      print(p)
>      idxLists.append(p)
>      print(idxLists)
>      return
>  for i in range(v_len):
>      if not v[i]:
>          v[i] = 1
>          p[nidx] = cost_idx[i]
>          perm(nidx+1,p_len,v_len)
>          v[i] = 0
> ```
>
> 그리고 아래와 같이 풀었으나 답은 다 나오고, 반례도 통과되지만....***메모리초과..ㅠ***

```python
'''
#1. cost배열의 idx(0,1..N-1)까지의 순열을 구함! -> 각 순서를 list에 list로 담음
#2. cost[i][j]는 i도시에서 j도시까지 가는 비용을 나타냄, i,j에 각 순서를 담음
예를들어 [0,1,2,3] 순서면
total = cost[0][1] + cost[1][2] + cost[2][3] + cost[3][0]이다.
여기서 cost값이 0 이면 길이없음! 안됨!!
이렇게 해서 total이 최소값인 것을 구하라!
'''
import sys
sys.stdin = open('input.txt','r')

from itertools import permutations


N = int(input())
cost =[]
for _ in range(N):
    cost.append(list(map(int,input().split())))
cost_idx = [i for i in range(N)]
#순열을 담을 리스트
idxLists = []
for i in list(permutations(cost_idx,N)):
    idxLists.append(i)
# print(idxLists)
#idx 순열 둘러보면서 MIN값 찾기
MIN = 987654321
for idx in idxLists:
    total = 0
    #마지막에 자신한테로 돌아와야됨, 그래서 처음부터 -1,0idx부터 더해줌!
    for i in range(len(idx)):
        if cost[idx[i-1]][idx[i]]:
            total += cost[idx[i-1]][idx[i]]
        #값이 0이면 다음 idx로 넘어가기, MIN갱신못하게 total최대값으로 줌
        else:
            total = 987654321
            break
    if MIN > total:
        MIN = total
print(MIN)
```

- **성공코드**

> 어차피 순환하니까 순열을 구할때 시작점이 0인 idx들만 list에 담으면 됨!!->이걸해줬더니 통과가 됐다!!

```python
'''
#1. cost배열의 idx(0,1..N-1)까지의 순열을 구함! -> 각 순서를 list에 list로 담음
하지만 순회하기 때문에 0으로 시작하는 순열만 구하면 됨!!
#2. cost[i][j]는 i도시에서 j도시까지 가는 비용을 나타냄, i,j에 각 순서를 담음
예를들어 [0,1,2,3] 순서면
total = cost[0][1] + cost[1][2] + cost[2][3] + cost[3][0]이다.
여기서 cost값이 0 이면 길이없음! 안됨!!
이렇게 해서 total이 최소값인 것을 구하라!
'''
import sys
sys.stdin = open('input.txt','r')

from itertools import permutations

N = int(input())
cost =[]
for _ in range(N):
    cost.append(list(map(int,input().split())))
cost_idx = [i for i in range(N)]
#순열을 담을 리스트
idxLists = []
for i in list(permutations(cost_idx,N)):
    #어차피 순환할거니까 앞이 0인 idx만 순열로 뽑기
    if i[0]:
        break
    idxLists.append(i)
# print(idxLists)
#idx 순열 둘러보면서 MIN값 찾기
MIN = 987654321
for idx in idxLists:
    total=0
    #마지막에 자신한테로 돌아와야됨, 그래서 처음부터 -1,0idx부터 더해줌!
    for i in range(len(idx)):
        if cost[idx[i-1]][idx[i]]:
            total += cost[idx[i-1]][idx[i]]
        #값이 0이면 다음 idx로 넘어가기, MIN갱신못하게 total최대값으로 줌
        else:
            total = 987654321
            break
    if MIN > total:
        MIN = total
print(MIN)
```



- [다른사람 풀이 참고](https://suri78.tistory.com/152)

> ![image-20201029014324346](Algorithm_TSP(외판원순회).assets/image-20201029014324346.png)
>
> 23분전 : 이건 내가 푼 방식으로 풀었을때의 메모리와 시간!!
>
> 5초전 : 비트마스크 방식으로 풀었을때!!
>
> 확실히 비트마스크를 이용한 방법이 메모리와 시간을 적게 차지한다!! 비트마스크에 익숙해지도록 연습해야겠다.😂

### 1.첫번째 방법 : 완전탐색

주어진 조건 중에서 주어지는 입력은 **반드시 순회**가 생긴다고 했기 때문에 출발점은 아무거나 하나를 선택 가능, 어디를 선택을 하던지 결국 사이클이 형성되면 출발점은 의미가 없어지기 때문이다.

그냥 0을 시작점으로 잡고 연결되어 있는 지점으로 반복해서 연결을 하며 사이클이 완성되면 비용을 갱신해주었다.

```python
import sys
#순열 함수를 만들어줌
def move(now, depth):
    global charge, ans
    #끝idx까지 돌았다면,
    if depth == n:
        #비용이 있다면, 갱신해주는데, 최소값을 ans에 담음
        if path[now][0] > 0:
            ans = min(ans, charge + path[now][0])
        #비용이 없다면 연결되지 않았으니 return
        return
    #방문표시,순열고를때 고른걸 안고르기 위해
    visit[now] = 1
    #이동할 수 있는 도시들을 둘러보면서
    for l in link[now]:
        #그 도시를 가지 않았다면
        if not visit[l]:
            #비용을 더해줌
            charge += path[now][l]
            #현재 위치를 갖고 다음idx로 재귀,
            move(l, depth+1)
            #비용을 빼줌, 그 위치는 빠졌기 때문
            charge -= path[now][l]
    #방문표시 다시 리셋, 순열은 다시 뽑혀야되기 때문
    visit[now] = 0

n = int(sys.stdin.readline())
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [0] * n
link = {}
charge, ans = 0, 10**7

#딕셔너리에 도시idx를 key값으로 주고, value에 이동할 수 있는 도시 idx를 담음, 0이면 안됨
for i in range(n):
    link[i] = []
    for j in range(n):
        if path[i][j] > 0:
            link[i].append(j)

move(0, 1)

print(ans)
```





### **2. ⭐두 번째 방법 : 비트마스크**

> 비트마스크를 사용한 방법은 아래 블로그를 참고함
>
> https://suri78.tistory.com/152
>
> https://withhamit.tistory.com/246

비트마스크를 사용해서 문제를 풀 수 있는 대표적인 문제가 **외판원 순회문제(TSP: Traveling Salesperson Problem)**라고 한다.

> (참고)
>
> **외판원 순회(TSP: Traveling Salesperson Problem)**
>
> 도시들이 있고 특정 도시에서 도시로 이동할 때 드는 비용이 주어졌을 때 불특정한 도시에서 출발해서 모든 도시를 돌고 다시 출발 도시로 돌아왔을 때 드는 최소 비용을 구하는 문제

 

비트마스크를 이용한 풀이 방법도 앞선 방법과 거의 유사하지만 **DP**를 통해서 문제를 해결하며, **메모이제이션**의 개념이 사용되기 때문에 완전 탐색보다 시간을 더 줄일 수 있는 방법이다.

 

이번 문제에서는 N의 범위가 작았기 때문에 충분히 완전 탐색으로 해결 가능하지만, N이 커질 경우에는 비트마스크를 사용한 풀이가 필수적!

 

간단하게 DP를 이용하는 방법만 설명하자면 다음과 같다.

A, B, C, D, E 총 5개의 도시가 있다고 하자. A->B->C->**D->E->A**로 연결된 하나의 경로가 존재하고, A->C->B->**D->E->A**로 이어지는 경로가 하나 있다고 하자. 그렇다면 위에 **굵게** 표시한 것처럼 공통된 부분이 생기게 된다.

두 경로에서 모두 현재 D에 위치해 있다고 했을 때 이전에 A, B, C를 지나왔기 때문에 앞으로 E, A를 방문해야 한다는 공통점이 있다. 그렇다면 "D->E->A"를 한 가지 경우로 묶어서 다음에도 D에 도착을 했는데 A, B, C를 지나왔다면 "D->E->A"의 비용만 추가로 계산을 해주면 되는 것이다.

이렇게 비트마스크를 이용한 방법은 **"D->E->A"처럼 중복해서 계산할 부분을 줄여줄 수 있는 방법(메모이제이션)**을 제시한다.



아래의 코드를 살펴보면 before가 여태까지 방문했던 노드들을 가리키고 있는 것을 알 수 있다.

before는 실제로 비트를 넘겨주는 것은 아니지만 비트 연산을 통해 방문했던 점들을 확인하는 용도로 사용되고 있다.

예를 들어 bit가 *11111*라고 하면, before는 *31*인 상태이다. 또 bit가 *11111*이라 하면 앞에서부터 순서대로 *4, 3, 2, 1, 0*번째의 노드를 가리키며 모든 비트가 *1*이기 때문에 현재 *4, 3, 2, 1, 0*번째 노드는 방문을 했다는 것을 의미한다.

마찬가지로 *11001*의 비트라고 한다면 before는 *25*인 상태이다. 그리고 *4, 3, 0*번째 노드는 이미 방문을 했고, *2, 1*번째 노드는 아직 방문을 안 한 상태이다.

 

이것을 이용해 *before == (1<<n) - 1로* 모든 지점을 방문했는지 알 수 있다.

n이 5라면 *1<<5 = 100000(2) = 32*이다. *32-1 = 31 = 11111(2)* 이기 때문에 *0, 1, 2, 3, 4*번째 노드 총 5개가 이미 방문한 상태라는 것을 알 수 있다.

 

따라서 find()를 호출할 때 넘겨주는 인자로는 현재 지점의 노드 번호와 현재 지점까지 포함된 방문했던 지점들이며, 반복문을 통해서 새로운 지점으로 이동을 하기 위해서는 *before | (1<<i)* 를 통해서 이동하려는 지점까지 포함된 비트마스크를 넘겨준다.

 

```python
import sys

def find(now, before):
    # 남아있는 경로를 이미 방문한 적이 있음
    if dp[now][before]:
        return dp[now][before]
    
    # 모두 방문한 경우
    if before == (1<<n) - 1:
        #만약 값이 0보다 크면 값을 return하고 아니라면 최댓값을 리턴
        return path[now][0] if path[now][0] > 0 else sys.maxsize

    # 현재 지점에서 이동할 수 있는 지점들을 탐색
    cost = sys.maxsize
    for i in range(1, n):
        if not (before>>i)%2 and path[now][i]:
            # i부터 0까지 순회를 만든 최소 비용
            tmp = find(i, before|(1<<i)) # before | (1<<i) == before + (1<<i)
            # (now~i), (i~0)의 합과 현재까지의 최소 비용과 비교
            cost = min(cost, tmp + path[now][i])

    # 메모이제이션, 중복되는 값들의 합을 저장!->시간,메모리 단축
    dp[now][before] = cost
    return cost

n = int(sys.stdin.readline())
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*(1<<n) for _ in range(n)]

print(find(0, 1))
```

- 익숙해지기 위해 따라써봄!!!

> 아직 이해하기 어려운 부분이 있다.
>
> ```python
> for i in range(1,n):
>  #before>>i는 0이고 path값이 0이아니면
>  if not (before >> i)%2 and path[now][i]:
>      #i부터 0까지 순회를 만든 최소 비용
>      tmp = find(i,before|(1<<i)) #before|(1<<i) == before + (1<<i)
>      #(now~i),(i~0)의 합과 현재까지의 최소 비용과 비교
>      cost = min(cost,tmp + path[now][i])
> ```
>
> 이부분은 아직 이해가 안된다....더 공부 필요함....ㅠ

```python
'''
외판원순회2를 비트마스크로 풀어보자!
일단 따라쓰기부터...!!!!ㅠㅠ
'''
import sys
sys.stdin = open('input.txt','r')

#idx들을 인자로 넘겨줌
def find(now,before):
    #순회!! 남아있는 경로를 이미 방문한 적 있음
    if dp[now][before]:
        return dp[now][before]

    #모두 방문한 경우 값 출력,dp가 1<<n개의 list가 있으니 idx는 -1
    if before == (1<<n)-1:
        #만약 값이 0보다 크면 값을 return, 아니라면 갈 수없으니 최댓값을 줘서 min갱신 못하게하자
        return path[now][0] if path[now][0] > 0 else sys.maxsize

    #현재 지점에서 이동할 수 있는 지점들을 탐색
    cost = sys.maxsize
    for i in range(1,n):
        #before>>i는 0이고 path값이 0이아니면
        if not (before >> i)%2 and path[now][i]:
            #i부터 0까지 순회를 만든 최소 비용
            tmp = find(i,before|(1<<i)) #before|(1<<i) == before + (1<<i)
            #(now~i),(i~0)의 합과 현재까지의 최소 비용과 비교
            cost = min(cost,tmp + path[now][i])

    #메모이제이션, 중복되는 값들의 합 저장
    dp[now][before] = cost
    return cost


n = int(input())
path = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
#메모이제이션 담을 리스트
dp = [[0]*(1<<n) for _ in range(n)]
print(find(0,1))
```





## Reference

https://suri78.tistory.com/152

https://withhamit.tistory.com/246