# Algorithm

> Tree, Heap



## Heap

> 최댓값과 최솟값을 빠르게 찾기 위해 고안된 자료구조

- 각 노드의 key값이 해당 노드의 key값보다 작지 않거나 크지 않은 완전 이진트리
- 키 값의 대소관계는 부모-자식 노드 사이 간에만 성립, 형제 노드 사이에는 영향X
- 자식 노드의 최대 개수는 힙의 종류에 따라 다르지만 이진트리에서는 최대 2개
- i번째 노드의 자식 노드가 2개인데, 왼쪽자식노드 :`2i` , 오른쪽 자식노드 `2i+1`, 부모노드 `i//2`



### heapq module

> 파이썬에서 제공하는 모듈, 일반적인 리스트를 min heap처럼 다룰 수 있게 해줌

```python
import heapq

#노드 추가 : heappush메소드를 이용
heap = []
heapq.heappush(heap, 1)



#노드 삭제 : heappop 메소드 이용
'''
가장 작은 원소를 꺼내 리턴, 자동적으로 그 다음으로 작은 원소가 루트노트가 됨
주의!!!! : 인덱스 1이 2번재로 작다는 보장은 없으므로 n번째로 작은 원소를 얻고 싶다면 n-1개의 원소를 빼내야 함.
'''
return heapq.heappop(heap)

#최소값으로 꺼내지 않고 리턴만 하려면 인덱스로 접근하기
print(heap[0])



#기존에 사용한 리스트를 힙으로 변환하기 : heapify 메소드 이용(시간복잡도 O(n))
tmp = [7,5,8,3]
heapq.heapify(tmp)




#최대 힙 만들기 : 우선순위가 포함된 튜플 이용하기
import heapq

nums = [4,1,7,3,8,5]
heap = []

for num in nums:
    heapq.heappush(heap,(-num,num)) #(우선순위, 값)
    
while heap:
    print(heapq.heappop(heap)[1]) #index 1
```

[참고](https://hocheon.tistory.com/70)



### Heap Sort 파이썬 구현

>1. 주어진 원소들로 최대 힙을 구성
>2. 최대 힙의 루트노드(현재 배열의 첫번째 요소, 최댓값)와 말단로드(현재 배열의 마지막 요소)를 교환
>3. 새 루트노드에 대해 최대 힙 구성
>4. 원소의 개수만큼 2.와 3.을 반복



```python
unsorted = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

'''
힙 성질을 만족하도록 하는 연산 heapify
heapify의 계산복잡성 = 트리의 높이(h=log2n)에 의존적
값을 비교하거나 바꾸는 연산은 O(1)이므로 
결과적으로 heapify의 계산복잡성은 O(logn)
'''
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

        
def heap_sort(unsorted):
    n = len(unsorted)
    '''
    BUILD-MAX-HEAP (A) : 위의 1단계
    인덱스 : (n을 2로 나눈 몫-1)~0
    최초 힙 구성시 배열의 중간부터 시작하면
    이진트리 성질에 의해 모든 요소값을 서로 한번씩 비교할 수 있게 됨 : O(n)
    '''
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    
    '''
    Recurrent (B) : 2~4단계
    한번 힙이 구성되면 개별 노드는
    최악의 경우에도 트리의 높이(logn)만큼의 자리 이동을 하게 됨
    이런 노드들이 n개 있으므로 : O(nlogn)
    '''
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted
```

- ` BUILD-MAX-HEAP (A)`의 인덱스(i)에 따른 정렬 과정

|   i    |               data                |
| :----: | :-------------------------------: |
| 초기값 | [16, 4, 10, 14, 7, 9, 3, 2, 8, 1] |
|   4    | [16, 4, 10, 14, 7, 9, 3, 2, 8, 1] |
|   3    | [16, 4, 10, 14, 7, 9, 3, 2, 8, 1] |
|   2    | [16, 4, 10, 14, 7, 9, 3, 2, 8, 1] |
|   1    | [16, 14, 10, 8, 7, 9, 3, 2, 4, 1] |
|   0    | [16, 14, 10, 8, 7, 9, 3, 2, 4, 1] |

- `(B) Recurrent`부분의 인덱스에 따른 정렬 과정

|  i   |               data                |
| :--: | :-------------------------------: |
|  9   | [1, 14, 10, 8, 7, 9, 3, 2, 4, 16] |
|  8   | [1, 8, 10, 4, 7, 9, 3, 2, 14, 16] |
|  7   | [2, 8, 9, 4, 7, 1, 3, 10, 14, 16] |
|  6   | [2, 8, 3, 4, 7, 1, 9, 10, 14, 16] |
|  5   | [1, 7, 3, 4, 2, 8, 9, 10, 14, 16] |
|  4   | [2, 4, 3, 1, 7, 8, 9, 10, 14, 16] |
|  3   | [1, 2, 3, 4, 7, 8, 9, 10, 14, 16] |
|  2   | [1, 2, 3, 4, 7, 8, 9, 10, 14, 16] |
|  1   | [1, 2, 3, 4, 7, 8, 9, 10, 14, 16] |

[참고](https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/)





## SWEA_5174_subtree

> 트리의 노드수 = N
>
> 간선 수  = N-1
>
> 모든 노드는 부모가 하나만 존재
>
> 싸이클이 없다 -> 방문정보 표시할 필요 없음
>
> 방문표시 할 필요 없음, 유향그래프인것 처럼 순회함! 위에서 밑으로.
>
> 전위/중위/후위
>
> 순회 : BFS보다 DFS가 더 간단함
>
> 재귀호출 방식으로 **DFS**로 이진트리를 순회함!(왼쪽자식을 오른쪽 자식보다 먼저 순회!)
>
> 모든 노드를 3번 거쳐감(처음 지나갈 때 방문-전위, 왼쪽에 돌아올 때 방문-중위, 오른쪽으로 갔다가 오면서 다시 방문-후위)



```python
'''
트리의 일부 서브트리라 함
이진트리 노드 N을 루트로 하는 서브트리에 속한 노드의 개수를 알아내는 프로그램
노드 N을 포함한 노드의 개수를 출력!
'''
import sys
sys.stdin = open('input.txt','r')
def preOrder(node):
    # print(node,end = ' ')
    global cnt
    cnt += 1
    if L[node]:
        preOrder(L[node])
    if R[node]:
        preOrder(R[node])

T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    arr = list(map(int,input().split()))
    L = [0] *(E+1+1)
    R = [0]*(E+1+1)
    P = [0]*(E+1+1)
    #두칸씩 자르고 처음칸 부모, 두번째는 자식
    cnt = 0
    for i in range(0,len(arr),2):
        p, c = arr[i], arr[i+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        P[c] = p
    preOrder(N)
    print('#{} {}'.format(tc,cnt))
```



- 유튜브선생님 코드

```python
for tc in range(1,int(input())+1):
    E, N = map(int,input().split()) #E 간선수, 정점수 E+1
    #정점번호 1~E+1

    L = [0] *(E+)
    R = [0] *(E+2)
    P = [0] *(E+2)

    arr = list(map(int,input().split()))
    for i in range(0,E*2,2): #arr[i]-->arr[i+1]
        p,c = arr[i], arr[i+1]
        #p의 왼쪽자식이 차있으면 오른쪽에 채우고
        if L[p]:
            R[p] =c
        #비어있다면 왼쪽에 채우자
        else:
            L[p] = c
        #부모정보는 c의 부모정보를 채우자
        P[c] = p

    ans = 0 #노드셀거야
    def traverse(v):
        global ans
        #단말노드는 왼쪽자식,오른쪽자식 0으로 저장돼있을거니까 끊으면 됨
        if v== 0:
            return
        ans += 1 , 이렇게 쓰는 경우에 함수 내의 어디에 쓰든 똑같음
        #왼쪽 자식 부름
        traverse(L[v])
        #오른쪽자식을 부름
        traverse(R[v])

    traverse(N)
    print(ans)
```

- 

```python
#retuurn value로 답을 줘보자! -> 후위순회 이용
    def traverse(v):
        #공백노드가 되면 어떻게 해줘야 될까? 밑에 아무것도 없으니 0을 리턴해줌
        if v== 0:
            return 0
        #1.
        #왼쪽 자식 부름
        l = traverse(L[v])
        #오른쪽자식을 부름
        r = traverse(R[v])
        #왼쪽 오른쪽 노드수를 구해서 현재 자신v(1)도 더함
        return l + r + 1
        
        
        #2. 아래와 같이 코드를 줄일 수 도 있음
        return traverse(L[v]) + traverse(R[v]) + 1
```

- BFS, 아래 코드 중 1번 2번 둘다 같은 결과 도출 보기 좋게 구현하는 것의 차이 

```python
#BFS으로도 할 수 있음
    ans = 0
    Q = [N]
    while Q:
        v = Q.pop(0)
        if v == 0 : return
        ans += 1
        #1.
        Q.append(L[v])
        Q.append(R[v])
        #2.
        if L[v]:
            Q.append(L[v])
        if R[v]:
            Q.append(R[v])
```





## SWEA_5178_이진탐색

> 완전이진트리 1~N까지 값을 1~N번 idx안에 섞여져서 들어감!
>
> 값은 이진탐색트리의 규칙에 따라 저장이 돼야 함!
>
> 1차원 배열을 쓸 수 있음, 자료가 N개면 1~N idx에 자료를 빈 공간 없이 순서대로 저장해야됨
>
> 이진탐색트리 중위순회 -> 오름차순으로 값을 읽어올 수 있음 (왼쪽, 부모, 오른쪽 크기 순으로 읽어옴)
>
> 방문노드 순서대로 1부터 N까지 맵핑을 하면 됨



- 중위순회로 node들을 읽어주는데, tree에 node idx에 값(num)을 저장해줘야하는데 반대로 적용하고 있어서 오래걸렸당...ㅎ

```python
'''
1~N: 자연수 이진탐색트리에 저장
왼쪽, 현재, 오른쪽 노드 순으로 저장 ->중위??
완전 이진 트리의 노드 번호는 루트1번, 아래로 내려가면서 왼쪽 오른쪽 순 증가
N이 주어졌을 때 완전이진트리로 만든 이진탐색 트리 루트에 저장된값과
N//2번 노드(부모)에 저장된 값 출력
'''
import sys
sys.stdin = open('input.txt','r')
T = int(input())

def inOrder(node):
    global num
    if L[node]:
        inOrder(L[node])
    # print(node, end=' ')
    tree[node] = num
    num += 1
    if R[node]:
        inOrder(R[node])
  

for tc in range(1,T+1):
    N = int(input())
    arr = [i for i in range(1,N+1)]
    L = [0] * (N+1)
    R = [0] * (N+1)
    tree = [0] * (N+1)
    num = 1
    for i in range(1,N//2+1):
        L[i] = 2*i
        if 2*i+1 <= N:
            R[i] = 2*i+1
    # print(N,'L',L,'R',R)
    inOrder(1)
    # print(tree)
    print('#{} {} {}'.format(tc,tree[1],tree[N//2]))
    # print()

```



- 유튜브 선생님 풀이

```python
for tc in range(1,int(input())+1):
    N = int(input())
    T = [0] *(N+1)

    cnt = 1
    def inorder(v):
        global cnt
        #v*2+1값이 N보다 크면 공백노드처럼 간주할 수 있다
        if v > N:
            return

        #왼쪽
        inorder(v*2)
        #매 노드마다 중위순회로 거쳐가는 시점마다 방문노드에 값을 저장함
        T[v] = cnt
        cnt += 1
        # print(v,end = ' ')
        #오른쪽
        inorder(v*2+1)

    inorder(1)
    print(T[1],T[N//2])
```





## SWEA_5178_노드의 합

```python
'''
완전이진 트리의 리프노드 1000이하 자연수 저장
리프 노드를 제외한 노드에는 자식노드에 저장된 값의 합이 들어있음
단말노드 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장, 지정한 노드 번호에 저장된 값을 출력
후위 순회 방식, 재귀호출로 풀어본다
단말노드(공백노드)에서는 0을 올라오게 함
전부 0으로 한 뒤 아래부터 누적돼서 값이 올라오면 되지 않을까...!
'''

for tc in range(1,int(input())+1):
    #노드수, 단말노드 수 , 출력할 노드번호
    N,M,L = map(int,input().split())
    T = [0] * (N+1)
    for _ in range(M):
        num, val = map(int,input().split())
        T[num] = val

    #1.
    def dfs(v):
        #공백노드일때 0을 리턴
        if v > N: return 0
        #왼쪽으로 가라
        l = dfs(v*2)
        #오른쪽으로 가라
        r = dfs(v*2+1)

        #원래 값을 건들이지 않고 더한값을 넣기 위해 누적 함!(왼쪽 오른쪽 더한 값을 원래 값에 더해줌)
        T[v] += l + r
        return T[v]

    dfs(1)
    print(f'#{tc} {T[L]}')

    #2.채워야 될 마지막의 idx(N-M)를 구해서 채우면서 올라가기(N-M부터 1까지 채우기)
    for i in range(N-M.0,-1):
        #i가 배열의 idx이자 노드번호
        # 왼족자식, 오른쪽 자식 더함
        T[i] = T[i*2]
        #오른쪽 자식은 없을 수도 있기 때문에 범위체크하고 더해줌
        if i * 2 + 1 <= N:
            T[i] += T[i*2+1]
    print(T[L])
```





##  SWEA_5177_이진힙

```python
'''
이진 최소힙
항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드 추가
부모 노드 값 < 자식 노드 값 유지
새로 추가된 노드 값이 조건에 맞지 않는 경우, 조건을 만족할때까지 부모노드와 값을 바꿈
N개 서로 다른 자연수 주어짐, 입력 순서대로 이진 최소힙에 저장,
마지막 노드의 조상 노드에 저장된 정수의 합을 알아냄
'''
import sys
sys.stdin = open('input.txt','r')

def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount #idx번호
    parent = cur // 2
    #루트가 아니고, if부모노드 값 > 자식노드 값 => swap
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    temp = list(map(int,input().split()))
    heapcount = 0
    heap = [0] * (N+1)
    for i in range(N):
        heappush(temp[i])

    result = 0
    i = N
    while True:
        if i == 0:
            break
        result += heap[i//2]
        i //= 2

    print('#{} {}'.format(tc,result))
```



- 유튜브 선생님 풀이

![image-20200911142341388](0910_algorithm(문제_Tree,Heap).assets/image-20200911142341388.png)

```python
def push(item):
    global hsize
    hsize += 1
    H[hsize] = item

    c = hsize
    p = hsize // 2

    #1.
    while p:
        if H[p] > H[c]:
            H[p],H[c] = H[c],H[p]
            c = p
            p = c//2
        else:
            break
    #2.1번코드 줄일 수 있다
    while p and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c // 2

for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))

    H = [0] * (N+1)
    #스택의 top과 같이 마지막을 가리키는 것
    hsize = 0

    
    #3. 위 함수 안쓰고 아래와 같이 바로 적어도 됨!
    for val in arr:
        hsize += 1
        H[hsize] = val

        c = hsize
        p = hsize // 2
        while p and H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2

    ans = 0
    v = N //2
    while v:
        ans += H[v]
        v = v//2
    print(ans)

```







## SWEA_1232_사칙연산

```python
'''
사칙연산, 후위로 계산이라고 수업때 그랬는데 중위인것같구.....음...ㅎ몰라..ㅎ
중간과정에서 연산은 실수 연산으로 하되, 최종 결과값이 정수로 떨어지지 않으면 정수부만 출력
정점번호는 1부터 N까지의 정수로 구분, 루트 정점번호는 반드시1
정점번호, 해당 값, 자식노드 주어짐!
출력 답은 항상 정수값
중위로 차례대로 값들을 넣고! 나중에 앞에서부터 계산을 하면 되지 않을까???
-->후위로 입력받고 예전에 배웠던 후위계산기 이용
'''
import sys
sys.stdin = open('input.txt','r')

def postOrder(v):
    global num
    if v == 0:
        return
    postOrder(int(L[v]))
    postOrder(int(R[v]))
    # print(v,end = ' ')
    tree[num] = P[v]
    num += 1


for tc in range(1,11):
    N = int(input())
    tree = ['0']*(N+1)
    L = [0]*(N+1)
    R = [0]*(N+1)
    P = [0]*(N+1)
    num = 1
    for i in range(N):
        info = list(input().split())
        #각노드의 값들을 넣어줌!
        P[int(info[0])] = info[1]
        if len(info) == 4:
            L[int(info[0])] = info[2]
            R[int(info[0])] = info[3]
    # print(P)
    # print(L,R)
    postOrder(1)

    result = 0
    stack = []
    #계산을 후위로 해야되나...?ㅎ......
    for i in tree:
        # print(i)
        if i.isdigit():
            # print(i)
            stack.append(int(i))
        # 연산자이면 꺼내서 연산 후 다시 삽입
        else:
            B = stack.pop()
            A = stack.pop()
            if i == '+':
                stack.append(A + B)
            elif i == '-':
                stack.append(A - B)
            elif i == '*':
                stack.append(A * B)
            elif i == '/':
                stack.append(A / B)
    print('#{} {}'.format(tc,int(stack.pop())))
```



- 유튜브 선생님 풀이

```python
for tc in range(1,11):
    N = int(input())
    T = [[]]

    for i in range(1,N+1):
        #순서가 바뀌어서 뒤죽박죽 들어올수 있어 위험함!,아니면 미리 만들어 놓고, 첫번째 노드 번호 보고 입력받음!
        T.append(list(input().split()))
        if len(T[i]) == 4: #연산자
            T[i][2] = int(T[i][2])
            T[i][3] = int(T[i][3])
        else: #피연산자
            T[i][1] = int(T[i][1])

    def calc(v):
        if len(T[v]) == 2: #피연산자  = 단말노드
            return T[v][1]
        else: #연산자
            l = calc(T[v][2])
            r = calc(T[v][3])
            
            if T[v][1] == '+':
                return l+r
            elif T[v][1] == '-':
                return l-r
            elif T[v][1] == '*':
                return l*r
            else :
                return l/r


    print(int(calc(1)))
```



