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
parent = ['']
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