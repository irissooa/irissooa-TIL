# Algorithm

## SWEA_1961_숫자배열회전

> [SWEA_1961_숫자배열회전](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq)
>
> 예전에 풀었던건데........오래걸림.........ㅠㅠㅠㅠㅠㅠㅠㅠㅠ휴ㅠㅠㅠㅠㅠㅠ
>
> 일단 이렇게 풀었는데, 예전풀이보고 좀더 수정해봄

```python
'''
소요시간 2020/10/24/17:25~18:30

'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint

#90도 돌리는 함수
def switch(arr,temp):
    for i in range(N):
        for j in range(N):
            temp[i][N-j-1] = arr[j][i]
    return


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    temp1 = [[0 for j in range(N)] for i in range(N)]
    temp2 = [[0 for j in range(N)] for i in range(N)]
    temp3 = [[0 for j in range(N)] for i in range(N)]

    # 90도를 돌림
    switch(arr,temp1)
    switch(temp1,temp2)
    switch(temp2,temp3)
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(temp1[i][j],end='')
        print(' ',end='')
        for j in range(N):
            print(temp2[i][j],end='')
        print(' ',end='')
        for j in range(N):
            print(temp3[i][j],end='')
        print()

```

- 예전풀이

> 이건 문자열로 수를 받아서 join을 써서 각 회전한 배열들을 한줄씩 붙였다. 이걸 어떻게 생각했을깡....퇴보함....ㅠ왜지...ㅠㅠㅠㅠㅠㅠ흐아ㅏㅏㅠㅠㅠㅠ

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

- 챌's code

```python
import sys
sys.stdin=open('input.txt','r')

def rotate(arr):
    tmp=[['']*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            tmp[c][N-1-r]=arr[r][c]
    return tmp

#각 배열을 돌린 행들을 각 col로 넣어줌!
def result(arr,col):
    for r in range(N):
        for c in range(N):
            ans[r][col]+=arr[r][c]
    return ans



if __name__=='__main__':
    for tc in range(1,int(input())+1):
        N=int(input())
        #왜 문자열로 받냐면, 이걸 나중에 다 하나씩 붙여줄건데, int로 받으면 연산이 됨
        arr=[input().split() for _ in range(N)]

        ans=[['']*3 for _ in range(N)]

        #rotate 3번 돌려야지 90도, 180도, 270도
        #그리고 ans에 하나씩 넣어야 한다.
        for i in range(3):
            arr=rotate(arr)
            ans=result(arr,i)

        print('#{}'.format(tc))
        for r in range(N):
            for c in range(3):
                print(ans[r][c],end=' ')
            print()
```





## BOJ_16926 배열 돌리기1

> [BOJ_16038 배열 돌리기1](https://www.acmicpc.net/problem/16926)
>
> - 깊은 복사(deep copy)
>
>   - 깊은 복사는 내부에 객체들까지 모두 새롭게 copy 되는 것입니다.
>   - copy.deepcopy메소드가 해결해줍니다.
>
>   ```python
>   import copy
>   a = [[1,2],[3,4]]
>   b = copy.deepcopy(a)
>   a[1].append(5)
>   print(a)
>   #[[1, 2], [3, 4, 5]]
>   print(b)
>   #[[1, 2], [3, 4]]
>   ```

- 풀긴 풀었는데....시간초과ㅠㅠㅠㅠㅠㅠㅠ찾아보니 파이썬으로 푼 사람이 7명...

> 선생님 조언은 for문을 행2개 열2개로 나눠서 이중포문이 아닌 포문 한개씩 4개로 돌려보라고 하셨다....어떻게 할지 생각해보자

```python
'''
배열을 돌릴때 배열의 테두리만 돌리고 N과 M중 작은 값의 2를나눈 몫만큼 돌아가면서 for문의 범위가 줄어든다.
for의 범위를 num(한번돌면 +1해서 돌아가는 배열을 좁힐 변수)~배열의크기-num으로 돌림
그리고 temp라는 배열을 만들어서 
제일 처음 열이고 행이 처음부터 마지막-1행은 아래(행+1)로 이동
행이 마지막이고 열이 처음부터 마지막-1열은 오른쪽(열+1)로 이동
열이 마지막이고 행이 처음+1부터 마지막행은 위쪽(행-1)로 이동
행이 처음이고 열이 처음을 제외하고 왼쪽(열-1)으로 이동

이렇게 하면 한번 회전됨!
이거를 함수로 만들어서 회전 수 R번이 주어지면 그만큼 돌게 만들자!
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
# import copy

def rotate(arr):
    num = 0
    #돌린 arr을 담을 배열
    temp = [[0 for j in range(M)] for i in range(N)]

    while min(N,M)//2 > num:
    # for n in range(min(N,M)//2):
        for i in range(num,N-num):
            for j in range(num,M-num):
                # 제일 처음 열이고 행이 처음부터 마지막-1행은 아래(행+1)로 이동
                if j == num and i != N-num-1:
                    temp[i+1][j] = arr[i][j]
                # 행이 마지막이고 열이 처음부터 마지막-1열은 오른쪽(열+1)로 이동
                elif i == N-num-1 and j !=M-num-1:
                    temp[i][j+1] = arr[i][j]
                # 열이 마지막이고 행이 처음+1부터 마지막행은 위쪽(행-1)로 이동
                elif j == M-num-1 and i != num:
                    temp[i-1][j] = arr[i][j]
                # 행이 처음이고 열이 처음을 제외하고 왼쪽(열-1)으로 이동
                elif i == num and j != num:
                    temp[i][j-1] = arr[i][j]
        #한범위의 테두리를 전부 돌면 num을 +1해서 범위를 좁혀줌
        num += 1
    return temp

#배열의 크기 N,M, 회전수 R
N,M,R = map(int,input().split())

#배열
arr = [list(map(int,input().split())) for _ in range(N)]
# temp = copy.deepcopy(arr)
for r in range(R):
    ans = rotate(arr)
    arr = ans
# print(ans)
for i in range(N):
    for j in range(M):
        print(ans[i][j],end=' ')
    print()


```



## 11724_연결요소의 개수

> [11724_연결요소의 개수](https://www.acmicpc.net/problem/11724)
>
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





## 5639_이진검색트리

이거다음에 다시하기ㅠㅠ

>[5639_이진검색트리](https://www.acmicpc.net/problem/5639)
>
>[이진검색트리개념](https://ratsgo.github.io/data%20structure&algorithm/2017/10/22/bst/)
>
>```python
>class Node:
>    def __init__(self, val):
>        self.val = val
>        self.leftChild = None
>        self.rightChild = None
>    
>    def get(self):
>        return self.val
>    
>    def set(self, val):
>        self.val = val
>        
>    def getChildren(self):
>        children = []
>        if(self.leftChild != None):
>            children.append(self.leftChild)
>        if(self.rightChild != None):
>            children.append(self.rightChild)
>        return children
>        
>class BST:
>    def __init__(self):
>        self.root = None
>
>    def setRoot(self, val):
>        self.root = Node(val)
>
>    def insert(self, val):
>        if(self.root is None):
>            self.setRoot(val)
>        else:
>            self.insertNode(self.root, val)
>
>    def insertNode(self, currentNode, val):
>        if(val <= currentNode.val):
>            if(currentNode.leftChild):
>                self.insertNode(currentNode.leftChild, val)
>            else:
>                currentNode.leftChild = Node(val)
>        elif(val > currentNode.val):
>            if(currentNode.rightChild):
>                self.insertNode(currentNode.rightChild, val)
>            else:
>                currentNode.rightChild = Node(val)
>
>    def find(self, val):
>        return self.findNode(self.root, val)
>
>    def findNode(self, currentNode, val):
>        if(currentNode is None):
>            return False
>        elif(val == currentNode.val):
>            return True
>        elif(val < currentNode.val):
>            return self.findNode(currentNode.leftChild, val)
>        else:
>            return self.findNode(currentNode.rightChild, val)
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



## 1182_부분수열의 합

```python
'''
num_list에서 수의 부분집합 중 더해서 합이 S가 되는 경우의 수 출력!
부분집합 구하는 함수 만들고,
그 sel의 합이 S인 것!
'''

import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('input.txt','r')

def powerset(idx):
    global cnt
    #idx가 끝까지 갔으니 부분집합 조건 확인
    if idx == N:
        #부분집합 합을 구할 변수
        total = 0
        for i in range(N):
            #부분집합 포함 표시가 있다면
            if sel[i]:
                total += num_list[i]
        #해당 부분집합 합이 S라면! 그리고 공집합이 아니라면!(S가 0일수도 있어서)
        if sum(sel) and total == S:
            cnt += 1
        return
    #포함
    sel[idx] = 1
    powerset(idx+1)
    #포함안함
    sel[idx] = 0
    powerset(idx+1)

#정수의 개수, 정수S
N,S = map(int,input().split())

#N개의 정수
num_list = list(map(int,input().split()))

#부분집합을 표시할 변수
sel = [0]*N
#합이 S인 부분집합 개수를 세어줄 변수
cnt = 0
powerset(0)
print(cnt)
```



## 2003_수들의합2

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
>     # end 를 가능한 만큼 이동시키기
>     while interval_sum < m and end < n:
>         interval_sum += data[end]
>         end += 1
>     # 부분합이 m일 때 카운트 증가
>     if interval_sum == m:
>         count += 1
>     interval_sum -= data[start]
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

