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
    if R[idx]:
        inOrder(R[idx])





for tc in range(1,11):
    #정점의 총수
    N = int(input())
    #정점(idx-1)에 알파벳을 담을 list
    V = [''] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)
    # P = [0] * (N+1)

    # tree = [[0] * 3 for _ in range(N+1)]
    # print(arr)
    for _ in range(N):
        info = list(input().split())
        # print(info[1],info[0])
        V[int(info[0])] = info[1]
        p = int(info[0])
        for i in range(2,len(info)):
            c = int(info[i])
            # print(c)
            if c%2==0:
                L[p] = c
            else:
                R[p] = c
            # P[c] = p
    # print(L)
    # print(R)
    # print(P)
    print('#{}'.format(tc),end = ' ')
    inOrder(1)
    print()


    #     if len(info) == 4:
    #         L[int(info[2])] = info[2]
    #         R[int(info[3])] = info[3]
    #     elif len(info) == 3:
    #         L[int(info[2])] = info[2]
        #자손과 연결된 것 표시
        # for i in range(2,len(info)):
        #     c = info[i*2]
        #     #왼쪽자식
        #     if tree[p][0] == 0:
        #         tree[p][0] = int(info[2])
        #     #오른쪽자식
        #     else:
        #         tree[p][1] = int(info[3])
        #     tree[]

    # for i in range(N+1):
    # print(V)
    # print(arr)