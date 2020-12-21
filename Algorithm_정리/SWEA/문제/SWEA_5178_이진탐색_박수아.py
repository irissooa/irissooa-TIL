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
    # print(node,end = ' ')
    if R[node]:
        inOrder(R[node])
    # R[node] = num
    # num += 1

for tc in range(1,T+1):
    N = int(input())
    arr = [i for i in range(1,N+1)]
    L = [0] * (N+1)
    R = [0] * (N+1)
    # P = [0] * (N+1)
    # tree=[[0] *3 for _ in range(N+1)]
    tree = [0] * (N+1)
    num = 1
    for i in range(1,N//2+1):
        # P[i] = i//2
        L[i] = 2*i
        if 2*i+1 <= N:
            R[i] = 2*i+1
    # print(N,'L',L,'P',P,'R',R)
    inOrder(1)
    # print(tree)
    print('#{} {} {}'.format(tc,tree[1],tree[N//2]))
    # print()

#유튜브 선생님 풀이

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