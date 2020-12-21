'''
이진 최소힙
항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드 추가
부모 노드 값 < 자식 노드 값 유지
새로 추가된 노드 값이 조건에 맞지 않는 경우, 조건을 만족할때까지 부모노드와 값을 바꿈
N개 서로 다른 자연수 주어짐, 입력 순서대로 이진 최소힙에 저장,
마지막 노드의 조상 노드에 저장된 정수의 합을 알아냄
'''
import sys
sys.stdin = open('input.txt','r')

def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount #idx번호
    parent = cur // 2
    #루트가 아니고, if부모노드 값 > 자식노드 값 => swap
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    temp = list(map(int,input().split()))
    heapcount = 0
    heap = [0] * (N+1)
    for i in range(N):
        heappush(temp[i])

    result = 0
    i = N
    while True:
        if i == 0:
            break
        result += heap[i//2]
        i //= 2

    print('#{} {}'.format(tc,result))



#유튜브 선생님 풀이

def push(item):
    global hsize
    hsize += 1
    H[hsize] = item

    c = hsize
    p = hsize // 2

    #1.
    while p:
        if H[p] > H[c]:
            H[p],H[c] = H[c],H[p]
            c = p
            p = c//2
        else:
            break
    #2.
    while p and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c // 2

for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))

    H = [0] * (N+1)
    #스택의 top과 같이 마지막을 가리키는 것
    hsize = 0

    for val in arr:
        hsize += 1
        H[hsize] = val

        c = hsize
        p = hsize // 2

        # 2.
        while p and H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2

    ans = 0
    v = N //2
    while v:
        ans += H[v]
        v = v//2
    print(ans)
