'''
전위순회 node가 주어짐
노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.
여기서  node를 받고
node의 L,R list를 채워나가는데 L은 바로 앞 노드값보다 작으면 왼쪽에 해당 node부모노드 idx에 넣음
그리고 큰 값이 나왔다면 앞의 노드들중 큰값보다 더큰 값을 찾으면 그 node idx의 오른쪽list에 넣음
'''
import sys
sys.stdin=open('input.txt','r')
sys.setrecursionlimit(10**8)

#Node를 입력받을 class
class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

#전위순회된 것을 이진트리로 만드는함수
def tree(r,n):
    # if r > n
    pass

def postorder(n):
    pass


cnt = 0
while True:
    try:
        val = int(input())
        node = Node(val)
        cnt+=1
        #루트를 표시해줌
        if cnt == 1:
            root = node
        # print(node.val)
        # print(root.val)
    except:
        break
print(node.val)