'''
임의의 이진트리 주어짐, 두 정잠의 공통 조상 중 가장 가까운 정점 찾고, 그 정점을 루트로 하는 서브 트리의 크기를 알아내라
입력에서 주어지는 두 정점이 서로 조상과 자손 관계인 경우는 없음
부모 정점이 자식정점보다 항상 작은 것은 아니며, 자식이 왼쪽에 있는지 오른쪽에 있는지는 중요하지 않다

각 정점의 조상들의 조상들을 계속 탐색->조상들을 리스트에 담고 공통조상 중 최댓값 출력

그 조상의 서브트리 개수 구하기
'''
import sys
sys.stdin = open('input.txt','r')

def DFS(node):
    global num
    # print(node)
    num += 1
    visited[node] = True
    for i in G[node]:
        DFS(i)

T = int(input())
for tc in range(1,T+1):
    #V 트리의 정점 총 수, E간선 총수, 공통 조상 찾는 두 정점 번호 a,b
    V,E,a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    #인접리스트에 담기
    G = [[] for _ in range(V+1)]
    for i in range(0,len(arr),2):
        st,ed = arr[i],arr[i+1]
        G[st].append(ed)
    # print(G)
    A = []
    B = []
    parent = 0
    while True:
        #공통조상을 찾음!
        if a == b:
            break
        for i in range(1,V+1):
            #a정점의 조상을 찾으면 a를 그 조상으로 바꿔줌
            if a in G[i]:
                A.append(i)
                a = i
                # print(i,'a')
            if b in G[i]:
                B.append(i)
                b = i
                # print(b,'b')

    for k in A:
        for l in B:
            #같은 공통조상 중 제일 먼저 나오는 것이 가장 가까운 조상!
            if k==l:
                parent = k
                break
        #for문에서 나오기위..
        if parent == k:
            break
    # print(A,B)

    # print(parent,'공통조상')
    #공통조상을 찾았으니 해당 정점의 서브트리 개수 구하기
    #dfs로...풀어보래....ㅎ
    num = 0
    visited = [False for _ in range(V+1)]
    # print(visited)
    DFS(parent)
    print('#{} {} {}'.format(tc,parent,num))