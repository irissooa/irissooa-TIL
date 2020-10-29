# BAEKJOON_DFS,BFS

[toc]

## 11724_연결요소의 개수

> 처음에  DFS로 풀었을 떄 런타임 에러가 났다ㅠㅠㅠ 그래서 bfs로도 풀어봤는데 런타임에러가 났다
>
> 질문검색으로 찾아보니까 `sys.setrecursionlimit(10**6)`를 써서 재귀 깊이를 늘려주는게 하나의 방법이라고 했다!

```python
'''
소요시간 : 2020/10/25/10:05
방향없는 그래프 -> 인접리스트에 표시
첫째줄부터 연결 요소의 개수를 출력!
dfs하면 될듯
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
sys.setrecursionlimit(10**6)

#근데...런타임에러ㅠ하..bfs로도 해보자
def DFS(s):
    #방문했으니 방문표시
    visited[s] = True
    #인접리스트에 있고, 방문하지 않은 정점이라면
    for e in arr[s]:
        if not visited[e]:
            DFS(e)

def BFS(s):
    q=[s]
    while q:
        p = q.pop()
        for e in arr[p]:
            if not visited[e]:
                visited[e] = True
                q.append(e)


#정점의 개수N,간선의 개수M
N,M = map(int,sys.stdin.readline().split())
#인접리스트
arr = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    #간선의 양 끝점 u,v주어짐
    u,v = map(int,sys.stdin.readline().split())
    #무방향이니까 둘다 표시해줌
    arr[u].append(v)
    arr[v].append(u)
cnt = 0 #연결요소를 세어줌
for s in range(1,N+1):
    if not visited[s]:
        DFS(s)
        # BFS(s)
        cnt += 1
# pprint(arr)
print(cnt)
```



## 5667_결혼식

```python
'''
6
5
1 2
1 3
3 4
2 3
4 5

#1.입력받고, 인접리스트를 만듦.

#2.BFS(1)로 출발
    이 프로그램은 친구 한명한명당 상근이와 얼마나 떨어져있는지 dist를 계산해줌
    => dist[] 있어야함
#3.그리고 프로그램 끝나면 dist에 다 추가 되있어야 함. dist의 value가 2인것만그 개수를 세줌
'''

import sys
sys.stdin = open('input.txt','r')
from collections import deque

def BFS(s):
    invite.append(s)
    while invite:
        ps = invite.popleft()
        for pe in friends[ps]:
            #0이아니면 방문!
            if dist[pe]:
                continue
            #아니라면 invite에 넣어줌
            dist[pe] = dist[ps] +1
            invite.append(pe)

#상근이 동기의 수n,
n = int(input())
#m 리스트 길이
m = int(input())
friends = [[]*(n+1) for _ in range(n+1)]
dist = [0]*(n+1)
invite = deque()
for _ in range(m):
    #친구관계
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)
BFS(1)
# print(dist)
cnt = 0
for i in range(2,n+1):
    if 0 < dist[i] <=2:
        cnt+=1
print(cnt)
```



## 2644_촌수계산

```python
'''
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
부모와 자식 사이 1촌
주어진사람들 촌수 구하기
#1. parent idx list에 child를 append(양방향으로!!)
#2. BFS(s)를 한뒤 구하고자하는 e까지 bfs돌리고 dist+=1추가해서 몇촌인지 구하기
'''
from collections import deque
def BFS(start):
    R.append(start)
    while R:
        ps = R.popleft()
        if ps == e:
            return
        for pe in family[ps]:
            if dist[pe]:
                continue
            dist[pe] = dist[ps] + 1
            R.append(pe)

#전체 사람 수
n = int(input())
#촌수 계싼해야되는 두 사람의 번호
s,e = map(int,input().split())
#부모 자식들 간의 관계의 개수
m = int(input())
family = [[0]*(n+1) for _ in range(n+1)]
dist = [0]*(n+1)
R = deque()
for _ in range(m):
    parent, child = map(int,input().split())
    family[parent].append(child)
    family[child].append(parent)
BFS(s)
if dist[e]:
    print(dist[e])
else:
    print(-1)
```



## 9466_텀프로젝트

> [9466_텀프로젝트](https://www.acmicpc.net/problem/9466)

- 이렇게 푸니까 재귀로 계속 돌려서 그런지 시간초과가 났다...ㅠ 재귀말고 다르게 풀어야될것 같다...

```python
import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**8)

def DFS(node):
    global cnt
    #q리스트 안에 node값이 이미 있다면 어딘가는 반복된다는 것! 그 값부터 한팀! 그전의 값들은 방문표시안함
    if node in q:
        #q안의 node들 모두 방문표시, 다시 못가게
        for i in q:
            visited[i] = 1
        #어느 위치가 반복되는지 찾고, 그 위치부터는 쭉 cnt를 표시해줌
        idx = q.index(node)
        for p in range(idx,len(q)):
            cnt+=1
        return
    #q안에 node값이 없다면 일단 q에 넣어줌
    q.append(node)
    #그 node의 값이 방문하지 않았다면 info[node]로 DFS돌림
    if not visited[info[node]]:
        DFS(info[node])

T = int(input())
for tc in range(1,T+1):
    #학생의 수
    N = int(input())
    #index를 맞추기 위해 앞에 0 삽입
    info = [0]+list(map(int,input().split()))
    visited = [0 for _ in range(N+1)]
    cnt = 0
    #자기자신을 가리키는 node는 방문처리
    for i in range(1,N+1):
        if i == info[i]:
            visited[i] = 1
            cnt += 1
    for i in range(1,N+1):
        q = []#잠시 팀원들을 담을 리스트
        if not visited[i]:
            DFS(i)
    print(N-cnt)
```



- 쥬아's code

```python
# 전체 - 팀을 이룰 수 있는것 이렇게 구하자

def DFS(v):
    global passed
    global dfsPath

    # 만약에 v가 dfsPath에 있으면 그 위치부터 반복됨
    if v in dfsPath:
        # 팀에 못끼는 애나 팀된애들이나 이제 접근하면 안되므로 방문처리
        for i in dfsPath:
            visited[i] = 1
        # 반복의 시작부터 끝까지 개수 세주기
        # 반복 아닌 부분은 세면 안되니까
        for i in range(len(dfsPath)):
            if dfsPath[i] == v:
                for j in range(i, len(dfsPath)):
                    passed += 1
        # for i in range(p,len(dfsPath)):
        #     passed += 1
        return
    # 일단 넣어주고
    dfsPath.append(v)

    # 다음놈이 접근가능하면 DFS돌리기
    if visited[team[v]] == 0:
        DFS(team[v])

for T in range(1, int(input())+1):
# for T in range(1, 2):
    N = int(input())
    team = [0] + list(map(int, input().split()))
    visited = [0]*(N+1)

    # 팀플가능한애들 수
    passed = 0
    # 혼자 노는 애있으면 팀플가능수에 넣고 접근못하게 하자
    for i in range(1, N+1):
        if team[i] == i:
            visited[i] = 1
            passed += 1
    # for i in range(1, N+1):


    for i in range(1, N+1):
        dfsPath = []
        if visited[i] == 0:
            DFS(i)

    print(N-passed)
```



- DFS로 풀지않고 반복문으로만 푼 사람을 구글링으로 찾았다...

> [jjangsungwon참고](https://jjangsungwon.tistory.com/40)
>
> - 1번부터 N번까지 순서대로 탐색을 시작한다.
> - 해당 번호에서 **DFS 탐색**을 시작한다. (**지나간 부분은 같은 팀으로 가정**)
> - 위에서 탐색한 방향의 역순으로 탐색하면서 사이클을 확인한다. **(-1을 대입)**
> - **역순으로 탐색**하면서 -1로 채워지지 않은 부분은 팀을 이루지 못한 것이라고 생각하면 된다.

```python
import sys

sys.setrecursionlimit(10 ** 6)


if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        N = int(input())
        p = list(map(int, input().split()))
        p.insert(0, 0)  # 인덱스 편의를 위해서 삽입
        team = [0] * (N + 1)

        for i in range(1, N + 1):
            if team[i] == 0:  # 아직 팀이 없는 경우
                team_number = i
                # 팀 구성한다고 가정
                while team[i] == 0:
                    team[i] = team_number
                    i = p[i]
                # 역순으로 순환하면서 사이클 확인
                while team[i] == team_number:
                    team[i] = -1
                    i = p[i]
        result = N - team.count(-1)
        print(result)
```

- DFS로 풀어서 맞은 코드

> 이분깔끔하게 잘 풀었따....부럽...

```python
import sys
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x) #사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]
    
    if visited[number]: #방문가능한 곳이 끝났는지
        if number in cycle: #사이클 가능 여부
            result += cycle[cycle.index(number):] #사이클 되는 구간 부터만 팀을 이룸
        return
    dfs(number)

for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N #방문 여부
    result = []
    
    for i in range(1, N+1):
        if not visited[i]: #방문 안한 곳이라면
            cycle = []
            dfs(i) #DFS 함수 돌림
            
    print(N - len(result)) #팀에 없는 사람 수
```

## 5639_이진검색트리

이거다음에 다시하기ㅠㅠ

>[5639_이진검색트리](https://www.acmicpc.net/problem/5639)
>
>[이진검색트리개념](https://ratsgo.github.io/data%20structure&algorithm/2017/10/22/bst/)
>
>```python
>class Node:
>def __init__(self, val):
>   self.val = val
>   self.leftChild = None
>   self.rightChild = None
>
>def get(self):
>   return self.val
>
>def set(self, val):
>   self.val = val
>   
>def getChildren(self):
>   children = []
>   if(self.leftChild != None):
>       children.append(self.leftChild)
>   if(self.rightChild != None):
>       children.append(self.rightChild)
>   return children
>   
>class BST:
>def __init__(self):
>   self.root = None
>
>def setRoot(self, val):
>   self.root = Node(val)
>
>def insert(self, val):
>   if(self.root is None):
>       self.setRoot(val)
>   else:
>       self.insertNode(self.root, val)
>
>def insertNode(self, currentNode, val):
>   if(val <= currentNode.val):
>       if(currentNode.leftChild):
>           self.insertNode(currentNode.leftChild, val)
>       else:
>           currentNode.leftChild = Node(val)
>   elif(val > currentNode.val):
>       if(currentNode.rightChild):
>           self.insertNode(currentNode.rightChild, val)
>       else:
>           currentNode.rightChild = Node(val)
>
>def find(self, val):
>   return self.findNode(self.root, val)
>
>def findNode(self, currentNode, val):
>   if(currentNode is None):
>       return False
>   elif(val == currentNode.val):
>       return True
>   elif(val < currentNode.val):
>       return self.findNode(currentNode.leftChild, val)
>   else:
>       return self.findNode(currentNode.rightChild, val)
>```
>
>



- [다른 사람 코드](https://developmentdiary.tistory.com/442) -> 트리를 class로 풀었따.. 신기...공부하쟈

> 이렇게 코드를 구현하면 시간초과가 난다.
>
> 이진트리를 만드는데 O(NlogN)
>
> 후위순회를 하는데 O(NlogN)의 시간이 든다.
>
> 트리를 만들지 않고 바로 출력하는 방식으로 만들어야겠다.
>
> 이진트리의 전위순회를 살펴보면
>
> 첫번째 루트 노드를 기준으로 작은값은 왼쪽 큰값은 오른쪽으로 나뉘는것을 볼 수 있다.
>
> 50 / 30 24 5 28 / 45 98 52 60
>
> 이렇게 분할하여 문제를 해결할수있다.

```python
class Node:
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None
 
 
class BinaryTree:
    def __init__(self):
        self.head=Node(None)
 
 
    def insert(self,item):#루트존재여부 확인
        if self.head.val is None:
            self.head.val = item
        else:
            self.addnode(self.head,item)
 
    def addnode(self,cur,item):
        if cur.val>item:#새로운 인자가 현재보다 작다면 왼쪽
            if cur.left!=None:#왼쪽이 비어있지않다면
                self.addnode(cur.left,item)
            else:#비어있다면 넣어준다.
                cur.left=Node(item)
        elif cur.val<item:#새로운 인자가 현재보다 크다면 오른쪽
            if cur.right!=None:
                self.addnode(cur.right,item)
            else:
                cur.right=Node(item)
    def postorder(self,cur):#후위순회
        if cur.left != None:
            self.postorder(cur.left)
        if cur.right != None:
            self.postorder(cur.right)
        print(cur.val)
 
 
import sys
sys.setrecursionlimit(10**9)
 
 
b_tree=BinaryTree()#초기화
count = 0
while count <= 10000:
    try:
        num = int(input())
    except:break
    b_tree.insert(num)
    count += 1
 
b_tree.postorder(b_tree.head)
```

- 이사람이 고친 코드

```python
def postorder(start,end):
    if start>end:
        return
 
    division=end+1#나눌위치
    for i in range(start+1,end+1):
        if post[start]<post[i]:
            division=i
            break
 
    postorder(start+1,division-1)#분할 왼쪽
    postorder(division,end)#분할 오른쪽
    print(post[start])
 
 
 
import sys
sys.setrecursionlimit(10**9)
 
 
post=[]
count = 0
while count <= 10000:
    try:
        num = int(input())
    except:break
    post.append(num)
    count += 1
 
postorder(0,len(post)-1)
```



## 10451_순열사이클

> [10451_순열사이클](https://www.acmicpc.net/problem/10451)

```python
'''
node의 idx -> node[idx]으로 그래프가 이어짐
dfs로  이어진 node들의 개수를 구하기!
'''

import sys
sys.stdin = open('input.txt','r')


def DFS(s):
    visited[s] = True
    e = node[s]
    if not visited[e]:
        DFS(e)


T =int(input())
for tc in range(1,T+1):
    #순열의크기N
    N = int(input())
    #순열, index맞춰줌
    node = [0]+ list(map(int,input().split()))
    visited = [False for _ in range(N+1)]
    cnt = 0
    for idx in range(1,N+1):
        if not visited[idx]:
            DFS(idx)
            cnt+=1
    print(cnt)
```



## 1991_트리순회

> [1991_트리순회](https://www.acmicpc.net/problem/1991)

```python
'''
전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
이거를 함수로 만든 뒤
전위순회
중위순회
후위순회순으로 출력
'''
import sys
sys.stdin = open('input.txt','r')

def preorder(n):
    print(node[n],end='')
    if L[n] != '.':
        preorder(node.index(L[n]))
    if R[n] != '.':
        preorder(node.index(R[n]))


def inorder(n):
    if L[n] != '.':
        inorder(node.index(L[n]))
    print(node[n],end ='')
    if R[n] != '.':
        inorder(node.index(R[n]))


def postorder(n):
    if L[n] !='.':
        postorder(node.index(L[n]))
    if R[n] != '.':
        postorder(node.index(R[n]))
    print(node[n],end='')

#이진트리 노드의 개수
N = int(input())
node = ['']
#왼쪽자식
L = ['']
#오른쪽 자식
R = ['']
for n in range(N):
    alpha,left,right = input().split()
    node.append(alpha)
    L.append(left)
    R.append(right)
# print(node,L,R)
preorder(1)
print()
inorder(1)
print()
postorder(1)
```



## 11725_트리의 부모찾기

> [11725_트리의부모찾기](https://www.acmicpc.net/problem/11725)
>
> 노드의 방향이 정해져 있지 않아서 문제! DFS로 루트번호 1부터 탐색을 하는데 만약 1과 연결돼있고, 방문하지 않은 node라면 자식배열에 1번 idx에 향하는 노드e를 담아주고, e의 부모배열에 s를 넣어줌!
>
> 그리고 출력은 부모만 하면된다
>
> 여기서 문제는 node개수가 10만개까지 주어지기 때문에 `sys.setrecursionlimit(10**10)` 이거를 써줘서 재귀의 깊이를 늘려줌!

```python
'''
노드를 인접리스트로 노드가 향하는 정점에 담는다
그리고 DFS로 루트 1부터 돌림!
'''
import sys
# sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**10)
def DFS(s):
    visited[s] = True
    for e in node[s]:
        if not visited[e]:
            child[s].append(e)
            parent[e] = s
            DFS(e)

#노드의 개수
N = int(input())
node = [[] for _ in range(N+1)]
child = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    s,e = map(int,input().split())
    node[s].append(e)
    node[e].append(s)
# print(node)
visited = [False for _ in range(N+1)]
DFS(1)
for p in range(2,N+1):
    print(parent[p])
# print(parent)
```



## 4963_섬의개수

> [4963_섬의개수](https://www.acmicpc.net/problem/4963)
>
> 이거도 재귀에러!
>
> 계산해서 재귀가 1000번 넘어갈것 같으면 `sys.setrecursionlimit(10**6)`이거 쓰기

```python
'''
정사각형으로 이루어진 섬과 바다
섬의 개수를 세는 프로그램
가로,세로,대각선 방향 이동 가능 -> 8방향델타
dfs로 붙어있는 섬의 개수 출력
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
sys.setrecursionlimit(10**6)

di =[0,1,0,-1,-1,1,-1,1]#우하좌상 우상대 우하대 좌상대 좌하대
dj = [1,0,-1,0,1,1,-1,-1]
def DFS(i,j):
    visited[i][j] = True
    for d in range(8):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= h or nj < 0 or nj >= w:
            continue
        if visited[ni][nj]:
            continue
        if not MAP[ni][nj]:
            continue
        DFS(ni,nj)

while True:
    #지도 너비 w, 높이 h
    w,h = map(int,input().split())
    #입력의 마지막 줄에는 0 두개가 주어짐
    if w == 0 and h == 0:
        break
    MAP = []
    visited = [[False for j in range(w)] for i in range(h)]
    #h개 줄 지도 1:땅,0은바다
    for _ in range(h):
        MAP.append(list(map(int,input().split())))
    print(h,w)
    pprint(MAP)
    num = 0
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1 and not visited[i][j]:
                DFS(i,j)
                num +=1
    print(num)
```



## 2331_반복수열

> [2331_반복수열](https://www.acmicpc.net/problem/2331)

```python
'''
D에 D[0]=A를 넣고 시작
D[n] = D[n-1]의 각 자리 숫자에 P를 곱한뒤 더한 값을 넣고
while문을 돌리는데
종료조건으로 D에 이미 들어간 숫자가 들어가면 break한 뒤 그 숫자의 앞에 있는 숫자들 개수 출력!
'''
import sys
sys.stdin = open('input.txt','r')
A,P = map(int,input().split())
D = [A]
num = 1
flag=False
while True:
    SUM = 0
    #문자열로 바꿔서 각 자리수를 분리시킴
    for n in range(len(str(D[num-1]))):
        SUM += int(str(D[num-1])[n])**P
        # print(SUM)
    #종료조건
    #D에 이미 들어간 숫자가 있다면 break!
    if SUM in D:
        # print(D)
        #D[num]이 D에 들어있는 수 중 앞에 있는걸 찾아서 그 앞의 수 개수를 출력
        for d in range(len(D)):
            if D[d] == SUM:
                print(len(D[:d]))
                flag=True
                break
        if flag:
            break
    #D[n] = D[n-1]의 각 자리 숫자에 P를 곱한뒤 더한값
    D.append(SUM)
    num+=1

```



## SWEA_5188_최소합

> dfs로 풀어야되는데 굳이 bfs로 풀어서.....ㅠ ㅎ ......ㅠ

```python
'''
방문하지 않은, 주변을 보면서 맨 왼쪽에서 오른쪽 아래로 도착하게함! bfs(최소)
dist에 합을 넣음
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,1]#우하
dj = [1,0]
def BFS(i,j):
    dist[i][j] = numbers[i][j]
    q = [(i,j)]
    while q:
        pi,pj = q.pop(0)
        for d in range(2):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            #다음값에 들어갈 합이 현재까지 누적합 + 현재값보다 크다면 굳이 갈필요 없음, pass
            if dist[ni][nj] < dist[pi][pj] + numbers[ni][nj]:
                continue
            
            #누적합 갱신
            dist[ni][nj] = dist[pi][pj] + numbers[ni][nj]
            q.append((ni,nj))



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = []
    dist = [[987654321 for j in range(N)] for i in range(N)]
    for n in range(N):
        numbers.append(list(map(int,input().split())))

    # print(numbers)
    BFS(0,0)
    # print(dist)
    print('#{} {}'.format(tc,dist[N-1][N-1]))

```



## BOJ_2668_숫자고르기

- 처음에는 조합으로 풀었다가 값이 너무 커서 시간초과...

```python
'''
조합! 함수사용
#1. first_numbers에서 K를 N에서부터 뒤로 내려오면서 NCk 만큼 뽑고 second_numbers에서도 NCk만큼 뽑는데 두 집합이 같으면 출력!
'''
from itertools import combinations


N = int(input())
first_numbers = [i for i in range(1,N+1)]
second_numbers = []
for n in range(N):
    second_numbers.append(int(input()))
# print(first_numbers)
# print(second_numbers)
flag = False
MAX = 0
for k in range(N,0,-1):
    first = []
    second = []
    cnt = 0
    for i in list(combinations(first_numbers,k)):
        first.append(i)
    for j in list(combinations(second_numbers,k)):
        second.append(j)
    # print(k,first,second)
    for f in first:
        for s in second:
            if set(f) == set(s):
                MAX = k
                flag = True
                print(MAX)
                print(*f,sep='\n')
                break
        if flag:
            break
    if flag:
        break
```

- 그래서 dfs로 풀었더니 됐따! 텀프로젝트와 똑같이 풀었따...

```python
'''
조합! 함수사용
#1. first_numbers에서 K를 N에서부터 뒤로 내려오면서 NCk 만큼 뽑고 second_numbers에서도 NCk만큼 뽑는데 두 집합이 같으면 출력!

#DFS로 풀기
#1.인접리스트를 만드는데, 유향으로 first->second로 만듦! 여기서 만약 양방향이 된다면 cnt!

#idea
#상대배열에 값이 똑같으면 result 넣고, 만약에 N까지 갔는데 내값이 상대 배열에없으면 둘다 지움...
'''
from itertools import combinations

import sys
sys.stdin = open('input.txt','r')

def DFS(num):
    global result
    visited[num] = True
    cycle.append(num)
    next = linked[num]
    # print(num,next)
    if visited[next]:
        if next in cycle:
            result += cycle[cycle.index(next):]
        return
    DFS(next)

#DFS로 풀기
N = int(input())
linked = [0 for _ in range(N+1)]

for n in range(1,N+1):
    linked[n]=int(input())
# print(linked)


result = []
visited = [False for j in range(N+1)]
for i in range(1,N+1):
    if not visited[i]:
        cycle = []
        DFS(i)
        # print(i,visited)
print(len(result))
# print(*result,sep='\n')
for i in sorted(result):
    print(i)

```

