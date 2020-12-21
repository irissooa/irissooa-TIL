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
    def preOrder(index):
        print(tree[index], end = ' ')
        if tree[index*2] != 0:
            preOrder(index*2)
        if tree[index*2+1] != 0:
            preOrder(index*2+1)

    def inOrder(index):
        if tree[index*2] != 0:
            preOrder(index*2)
        print(tree[index], end = ' ')
        if tree[index*2+1] != 0:
            preOrder(index*2+1)

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
