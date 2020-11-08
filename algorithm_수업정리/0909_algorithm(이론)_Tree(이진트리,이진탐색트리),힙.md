# Algorithm

> - Tree -> 개념 종류
> - 이진트리 -> 표현방법, 순회
> - 이진탐색 트리
> - 힙(완전 이진 트리) -> 우선순위 큐를 힙으로 구현

- 선형구조(1:1)
  - 표현방법 : list
  - 순회 : for문
- 비선형구조
  - 그래프(N:N) : 정점과 간선으로 이루어짐
    - DFS :재귀로 만들 시 stack overflow를 생각해야됨!
    - BFS 
    - 만야 둘다 풀 수 있다면 BFS로 푸는 것이 더 유리함
  - 트리(1:N) : 계층관계, 사이클,방향성이 없는 그래프
  - 이진트리 (1:N)
    - 자식이 두개 이하(왼쪽자식, 오른쪽자식..), 이진트리가 아니면 그래프에서 하는 방식으로 처리함
    - 표현방법(저장) : 자식이 적기 때문에 들어올 곳을 미리 만들어놓음
    - 순회에 DFS,BFS를 쓰는건 소잡는 칼로 닭잡는 격...

|   비선형구조   |                           이진트리                           |                       그래프                        |
| :------------: | :----------------------------------------------------------: | :-------------------------------------------------: |
| 표현방법(저장) |           1차원배열, 2차원배열(인접리스트와 유사)            |           인접행렬, 인접리스트, 간선배열            |
|      순회      | 전위, 중위,후위 -visit도 체크 안해줘도 됨, 그래프보다 순회가 쉬움 | **DFS(stack)**, **BFS(Queue)** - visit체크 해줘야됨 |

## Tree

- 비선형 구조
- 원소들 간에 1 : n 관계를 가지는 자료구조
- 원소들 간에 계층 관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조
- 한 개 이상의 노드(정점)로 이루어진 유한 집합
  - 노드 중 최상위 노드를 *루트(root)*라 함
  - 나머지 노드들은 n(>=0)개의 분리 집합 T1,...TN으로 분리될 수 있음
- T1,...TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 *부트리(subtree)*라 함

#### 트리 용어 정리

- 노드: 트리의 원소
- 간선: 노드를 연결하는 선, 부모 노드와  자식노드를 연결
- 루트 노드 : 트리의 시작노드
- 형제 노드 : 같은 부모 노드의 자식 노드들
- 조상 노드 : 간선을 따라 루트 노드까지 이르는 경로의 모든 노드들
- 서브트리 : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손노드 : 서브 트리에 있는 하위 레벨의 노드들
- 단말노드(터미널노드,잎(leaf)노드): 자식이 없는 노드, 제일 끝에 달린 노드
- 가지노드 : 단말노드가 아닌 노드, 루트도 가지노드 중 하나 이런식으로 부름..ㅎ

![image-20200909101724675](0909_algorithm(이론)_Tree(이진트리,이진탐색트리),힙.assets/image-20200909101724675.png)

- 차수(degree)
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
  - 단말 노드(리프노드) : 차수가 0인 노드, 자식 노드가 없는 노드
- 높이 
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수, 노드의 레벨
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값, 최대 레벨



### 이진트리

- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리
  - 왼쪽 자식 노드
  - 오른쪽 자식 노드

#### 이진트리_특성

- 레벨 i에서의 노드의 최대 개수2^i개
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수(h+1)개가 되며, 최대 개수는 (2^(h+1)-1)개가 됨

#### 이진트리_종류

- 포화 이진 트리(Full Binary Tree)
  - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
  - 높이가 h일때, 최대의 노드 개수인 (2^(h+1)-1)의 노드를 가진 이진 트리
  - 루트를 1번으로 하여 2^(h+1)-1까지 정해진 위치에 대한 노드 번호를 가짐
- **완전 이진 트리(Complete Binary Tree)** 자주 나옴!(힙도 완전이진트리)
  - 높이가 h이고 노드 수가 n개일 때 (단, h+1 <= n <= 2^(h+1)-1),포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진트리
- 편향 이진 트리(Skewed Binary Tree)
  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 바향의 자식 노드만을 가진 이진 트리
  - 트리의 가치가 없음
    - 왼쪽 편향 이진트리
    - 오른쪽 편향 이진트리

#### 이진트리 _ 순회

- 순회란 트리의 각 노드를 중복되지 않게 전부 방문(visit)하는 것을 말함
- 트리는 비선형구조이기 떄문에 선형구조에서와 같이 선후 연결 관계를 알 수 없음
- 따라서 특별한 방법 필요
- 순회방법
  - 전위순회:VLR
    - 부모노드 방문 후, 자식노드를 좌, 우 순서로 방문
  - 중위순회 : LVR
    - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문
  - 후위순회 : LRV
    - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문

##### 전위 순회

![image-20200909104443520](0909_algorithm(이론)_Tree(이진트리,이진탐색트리),힙.assets/image-20200909104443520.png)

- 수행방법
  1. 현재 노드n을 방문하여 처리 -> V
  2. 현재 노드n의 왼쪽 서브트리로 이동 -> L
  3. 현재 노드n의 오른쪽 서브트리로 이동 -> R
- 전위 순회 알고리즘
  - 가는 곳이 뻔하기 때문에 방문처리를 안해줘도됨!

```python
def preorder_traverse(T): #전위순회 ,T(Node번호)
    if T: #T is not None(0이 아니면)
        visit(T) #방문하라는 얘기지 방문처리 아님!!!
        #print(T.item)
        preorder_traverse(T.left)
        preorder_traverse(T.right)
```

- DFS와 유사하지만 자식이 두개밖에 없음.



##### 중위 순회

![image-20200909105927146](0909_algorithm(이론)_Tree(이진트리,이진탐색트리),힙.assets/image-20200909105927146.png)

- 수행 방법
  1. 현재 노드n의 왼쪽 서브트리로 이동 :L
  2. 현재 노드 n을 방문하여 처리 :V
  3. 현재 노드 n의 오른쪽 서브트리로 이동 : R

- 중위 순회 알고리즘

```python
def inorder_traverse(T): #중위순회
    if T: #T in not None
        inorder_traverse(T.left)
        visit(T) #print(T.item)
        inorder_traverse(T.right)
```



##### 후위 순회-> 자주 씀

![image-20200909105443677](0909_algorithm(이론)_Tree(이진트리,이진탐색트리),힙.assets/image-20200909105443677.png)

- 수행 방법
  1. 현재 노드 n의 왼쪽 서브트리로 이동함 :L
  2. 현재 노드 n의 오른쪽 서브트리로 이동 : R
  3. 현재 노드 n을 방문하여 처리 :V

```python
def postorder_traverse(T): #후위순회
	if T : #T is not None
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T) #print(T.item)
```

#### 이진 트리 순회

![image-20200909110327965](0909_algorithm(이론)_Tree(이진트리,이진탐색트리),힙.assets/image-20200909110327965.png)

- 전위 순회
  - A B D H I E J C F K G L M
- 중위 순회
  - H D I B J E A F K C L G M
- 후외 순회
  - H I D J E B K F L M G C A

#### 이진트리 표현

- 배열을 이용한 이진 트리의 표현
  - 이진 트리에 각 노드 번호를 다음과 같이 부여함
  - 루트의 번호를 1로함
  - 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2^n부터 2^(n+1)-1까지 번호를 차례로 부여
- 아래 그림은 포화이진트리이며 완전이진트리다

![image-20200909110822228](0909_algorithm(이론)_Tree(이진트리,이진탐색트리),힙.assets/image-20200909110822228.png)

- 노드 번호의 성질
  - 노드 번호가 i인 노드의 부모 노드 번호? `[i//2]`
  - 노드 번호가 i인 노드의 왼쪽 자식 노드 번호? `2*i`
  - 노드 번호가 i인 노드의 오른쪽 자식 노드 번호? `2*i + 1`
  - 레벨 n의 노드번호 시작 번호는?`2^n`

![image-20200909111138004](0909_algorithm(이론)_Tree(이진트리,이진탐색트리),힙.assets/image-20200909111138004.png)

- 노드 번호를 배열의 인덱스로 사용(0은 보통 사용하지 않음)

- 높이가 h인 이진 트리를 위한 배열의 크기(`2^(h+1)-1`)

- 파이썬은 배열이라 하지 않고 리스트라고 함, 배열은 크기가 고정되어 있지만 파이썬의 배열은 고정되지 않기 때문(append..하면됨)

- 배열의 단점(C, java) - 파이썬은 상관X

  - 중간이 많이 비어있음(0이 많다), 메모리 낭비
  - 편향 이진트리의 경우 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
  - 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기 변경 어려워 비효율적

- 트리의 표현_연결리스트(배열 보안을 위해 사용)

  - 배열을 이용한 이진 트리의 표현의 단점을 보완하기 위해 연결리스트를 이용하여 트리를 표현

  - 연결 자료구조를 이용한 이진트리의 표현

    - 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결 리스트 노드를 사용하여 구현

    |      left      | 데이터 |      right       |
    | :------------: | :----: | :--------------: |
    | 왼쪽 자식 노드 |        | 오른쪽 자식 노드 |

#### 연습문제

- 트리 정점의 개수 V, 간선 V-1개
- 이진트리 전위,중위,후위 순회 하여 정점의 번호를 출력해라!

```python
#정점 V, 간선 V-1
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
#전위
#정점의 개수
V = int(input())
arr = list(map(int,input().split()))
tree = [0] *100
#두칸씩 자르고 처음칸 부모, 두번째는 자식
for i in range(0,len(arr),2):
    p = arr[i]
    c = arr[i+1]
    if p not in tree:
        idx = -1
    else:
        idx = tree.index(p)
    if idx == -1:
        tree[1] = p
        tree[2] = c
    else:
        #왼쪽 자식이 비었으면 거기
        if tree[idx*2] == 0:
            tree[idx*2] = c
        #아니라면 오른쪽
        else:
            tree[idx*2+1] = c
    # print(tree)
    #전위
    def preOrder(index):
        print(tree[index], end = ' ')
        if tree[index*2] != 0:
            preOrder(index*2)
        if tree[index*2+1] != 0:
            preOrder(index*2+1)
	#중위
    def inOrder(index):
        if tree[index*2] != 0:
            preOrder(index*2)
        print(tree[index], end = ' ')
        if tree[index*2+1] != 0:
            preOrder(index*2+1)
	#후위
    def postOrder(index):
        if tree[index*2] != 0:
            preOrder(index*2)
        if tree[index*2+1] != 0:
            preOrder(index*2+1)
        print(tree[index], end = ' ')
preOrder(1)
print()
inOrder(1)
print()
postOrder(1)
```

- 다른풀이

```python
#의수
# 전위
def PLR(x):
    print(x, end=' ')
    if L[x]:
        PLR(L[x])
    if R[x]:
        PLR(R[x])

# 중위
def LPR(x):
    if L[x]:
        LPR(L[x])
    print(x, end=' ')
    if R[x]:
        LPR(R[x])

# 후위
def LRP(x):
    if L[x]:
        LRP(L[x])
    if R[x]:
        LRP(R[x])
    print(x, end=' ')

N = int(input())
arr = list(map(int, input().split()))
L = [0] * (N + 1)
R = [0] * (N + 1)
P = [0] * (N + 1)
for i in range(0, len(arr), 2):
    p = arr[i]
    c = arr[i + 1]
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p

print('전위 순회')
PLR(1)
print()

print('중위 순회')
LPR(1)
print()

print('후위 순회')
LRP(1)
print()
```

- 유튜브교수님 풀이

```python
#유튜브교수님 풀이

def preorder(node):
    if node:
        print(node,end = ' ')
        preorder(tree[node][0])
        preOrder(tree[node][1])

V = int(input()) #정점
E = V-1 #간선

tree = [[0] * 3 for _ in range(V+1)] #14(13+1)*3 0 2차원배열 만들기
temp = list(map(int,input().split()))
#tree에 저장
for i in range(E):
    p,c = temp[i*2],temp[i*2+1]
    if tree[p][0] == 0:
        tree[p][0] = c #왼쪽자식
    else:
        tree[p][1] = c :#오른쪽 자식
    tree[c][2] = p #부모 넣기
print(tree)

```



## SWEA_1231_중위순회

```python
'''
중위순회 이용하여 풀기
총 노드의 개수는 100개를 넘어가지 않음
루트 정점의 번호는 반드시 1
정점 번호와 알파벳이 함께 주어짐, 알파벳 뒤의 숫자는 정점과 연결된 자식노드들
중위순회는 왼쪽을보고 오른쪽을 보기전 중간에 print를 함

각 정점 idx대로 알파벳을 담을 list
연결된 것을 인접행렬로 표시
중위순회를 함수로 만들어 정점을 print하고 그 인덱스값을 토대로 문자를 출력
'''
import sys
sys.stdin = open('input.txt','r')

def inOrder(idx):
    #자손이 몇개 들어있는지 나눔
    if L[idx]: #왼쪽이면
        inOrder(L[idx])
    print(V[idx],end = '')
    if R[idx]:#오른쪽이면
        inOrder(R[idx])

for tc in range(1,11):
    #정점의 총수
    N = int(input())
    #정점(idx-1)에 알파벳을 담을 list
    V = [''] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)

    for _ in range(N):
        info = list(input().split())
        #정점의 단어를 정점idx에 넣어둠
        V[int(info[0])] = info[1]
        #부모idx
        p = int(info[0])
        for i in range(2,len(info)):
            c = int(info[i])
            #왼쪽자식idx
            if c%2==0:
                L[p] = c
            else:#오른쪽 자식idx
                R[p] = c
    print('#{}'.format(tc),end = ' ')
    inOrder(1)
    print()
```

- 선생님코드

```python
def inOrder(v):
    #왼쪽자식이 있을 때
    if len(arr[v]) >= 3:
        inOrder(int(arr[v][2]))
    #출력
    print(arr[v][1], end='')
    #오른쪽자식이 있을 떄
    if len(arr[v]) == 4:
        inOrder(int(arr[v][3]))
    
    
for tc in range(1,11):
    N = int(input())
    
    #2차원리스트로 인접리스트느낌으로 처리
    arr = [[]] #0번 idx 버리기
    
    for i in range(N):
        arr.append(input().split())
    
    print('#{}'.format(tc), end = ' ')
    inOrder(1)
    print()
```



- 다른코드

```python
#병훈
def inorder(idx):
    if idx > N:
        return
    inorder(idx*2)
    print(tree[idx],end='')
    inorder(idx*2+1)
 
for t in range(1,11):
    N = int(input())
    tree = [0]*(N+1)
    for i in range(1,N+1):
        element = input().split()
        tree[i] = element[1]
    print("#{} ".format(t),end='')
    inorder(1)
    print()
```

- 

```python
#의수
def LPR(x):
    if L[x]:
        LPR(L[x])
    print(P[x], end='')
    if R[x]:
        LPR(R[x])
 
for tc in range(1, 11):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    P = [0] * (N + 1)
    for _ in range(N):
        data = list(input().split())
        if len(data) == 4:
            L[int(data[0])] = int(data[2])
            R[int(data[0])] = int(data[3])
            P[int(data[0])] = data[1]
        elif len(data) == 3:
            L[int(data[0])] = int(data[2])
            P[int(data[0])] = data[1]
        else:
            P[int(data[0])] = data[1]
 
    print('#{}'.format(tc), end=' ')
    LPR(1)
    print()
```

- 

```python
def inOrder(index):
    if tree[index * 2] != 0:
        inOrder(index * 2)
    print(tree[index], end="")
    if tree[index * 2 + 1] != 0:
        inOrder(index * 2 + 1)
 
 
#도균
for test_case in range(1, 11):
    N = int(input())
    tree = [0] * 400
    for _ in range(N):
        i = list(input().split())
        n = int(i[0])
        w = i[1]
        tree[int(n)] = w
    print('#{}'.format(test_case), end=' ')
    inOrder(1)
    print()
```



## 수식 트리 : 후위순회로 풀어야됨!

- 수식을 표현하는 이진 트리
- 수식 이진 트리(Expression Binary Tree)라고 부르기도 함
- 연산자는 루트 노드이거나 가지 노드
- 피연산자는 모두 잎 노드



## 이진 탐색 트리(BST) : 개념정도..

- 탐색작업을 효율적으로 하기 위한 자료구조
- 모든 원소는 서로 다른 유일한 키를 가짐
- key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
- 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리
- 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있음

#### 이진탐색 트리 _연산

- 탐색 연산
  - 루트에서 시작됨
  - 탐색할 키 값x를 루트 노드의 키값과 비교
    - (키값x = 루트노드의 키값)인 경우 : 원하는 원소를 찾았으므로 탐색 연산 성공
    - (키값x < 루트노드의 키값)인 경우 : 루트노드의 왼쪽 서브트리에 대해서 탐색연산 수행
    - (키값x > 루트노드의 키값)인 경우 :  루트노드의 오른쪽 서브트리에 대해서 탐색연산 수행
  - 서브트리에 대해서 순환적으로 반복



- 삽입연산
  - 먼저 탐색 연산을 수행
    - 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없으므로, 같은 원소가 트리에 있는지 탐색하여 확인
    - 탐색 실패한 위치가 삽입위치가 됨

- 삭제 연산
  - 개인적으로공부....



#### 이진탐색 트리_성능

- 탐색, 삽입, 삭제 시간은 트리의 높이만큼 시간이 걸림
  - O(h), h : BST의 깊이(height)
- 평균의 경우
  - 이진 트리가 균형적으로 생성되어 있는 경우
  - O(log n)
- 최악의 경우
  - 한쪽으로 치우친 경사 이진트리의 경우
  - O(n)
  - 순차탐색과 시간복잡도가 같음



- 검색알고리즘의 비교

- 배열에서의 순차 검색 : O(N)
- 정렬된 배열에서의 순차 검색 : O(N)
- 정렬된 배열에서의 이진탐색 : O(logN)
  - 고정 배열 크기와 삽입, 삭제 시 추가 연산 필요
- 이진 탐색트리에서의 평균 :  O(logN)
  - 최악의 경우 : O(1)
  - 완전 이진 트리 또는 균형트리로 바꿀 수 있다면 최악의 경우를 없앨 수 있음
  - 새로운 원소를 삽입할 때 삽입 시간을 줄임
  - 평균과 최악의 시간이 길다 O(logn)
- 해쉬 검색: O(1)
  - 추가 저장 공간이 필요



## 힙(heap)

> 우선순위 큐 사용
>
> 힙의 키를 우선순위로 활용하여 우선순위 큐를 구현할 수 있음

- `완전 이진 트리`에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해서 만든 자료구조
- 최대 힙(max heap)
  - 키값이 가장 큰 노드를 찾기 위한 **완전 이진 트리**
  - {부모노드의 키값 > 자식노드의 키값}
  - 루트 노드 : 키값이 가장 큰 노드
- 최소 합(min heap)
  - 키값이 가장 작은 노드를 찾기 위한 **완전 이진 트리**
  - {부모노드의 키값  < 자식노드의 키값}
  - 루트노드 : 키값이 가장 작은 노드

![image-20200909151602043](0909_algorithm(이론)_Tree(이진트리,이진탐색트리),힙.assets/image-20200909151602043.png)

![image-20200909151631271](0909_algorithm(이론)_Tree(이진트리,이진탐색트리),힙.assets/image-20200909151631271.png)

- 힙에서의 삭제 예

![image-20200909151821218](0909_algorithm(이론)_Tree(이진트리,이진탐색트리),힙.assets/image-20200909151821218.png)

- 힙에서는 루트 노드의 원소만을 삭제 할 수 있음
- 루트 노드의 원소를 삭제하여 반환
- 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있음

```python
def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount #idx번호
    parent = cur // 2
    #루트가 아니고, if 부모노드 값 > 자식노드 값 => swap 두개를 바꿈
    while parent and heap[parent] > heap[cur]:
        heap[parent],heap[cur] = heap[cur],heap[parent]
        cur = parent
        parent = cur // 2


def heappop():
    global heapcount
    retvalue = heap[1] #루트를 반환해야됨
    heap[1] = heap[heapcount]
    #먼저 지우고 count를 줄여야됨
    heap[heapcount] = 0
    heapcount -= 1
    parent = 1
    child = parent * 2
    #오른쪽자식 idx는 홀수, 왼쪽자식은 짝수
    if child + 1 <= heapcount:#오른쪽 자식 존재
        if heap[child] > heap[child+1]:
            child = child + 1

    #자식노드가 존재하고, 부모노드 > 자식노드 = > swap
    while child  <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:#오른쪽 자식 존재
            if heap[child] > heap[child+1]:
                child = child + 1
    return retValue


#최소합
heapcount = 0
temp = [7,2,5,3,4,6]
N = len(temp)
heap = [0] * (N + 1)
for i in range(N):
    heappush(temp[i])

#삭제
for i in range(N):
    print(heappop(), end = ' ')
print()


```

- `heapq`모듈

```python
#최소힙만 지원(heapq)
import heapq
heap1 = [7,2,5,3,4,6] #list
print(heap1)
heapq.heapify(heap1)
print(heap1)
heapq.heappush(heap1,1)
print(heap1)
while heap1:
    print(heapq.heappop(heap1), end = ' ')
print()
temp = [7,2,5,3,4,6]
heap2 = []
for i in range(len(temp)):
    #우선순위 -temp[i]가 먼저, 같다면 temp[i]를 기준으로 정렬
    heapq.heappush(heap2,(-temp[i],temp[i]))
heapq.heappush(heap2,(-1,1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2)[1],end = ' ')
    # print(heapq.heappop(heap2)[0]*(-1),end = ' ')

```

