# Algorithm

> Tree

## SWEA_5174_subtree

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



## SWEA_5178_이진탐색

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

