def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount #idx번호
    parent = cur // 2
    #루트가 아니고, if 부모노드 값 > 자식노드 값 => swap 두개를 바꿈
    while parent and heap[parent] > heap[cur]:
        heap[parent],heap[cur] = heap[cur],heap[parent]
        cur = parent
        parent = cur // 2


def heappop():
    global heapcount
    retvalue = heap[1] #루트를 반환해야됨
    heap[1] = heap[heapcount]
    #먼저 지우고 count를 줄여야됨
    heap[heapcount] = 0
    heapcount -= 1
    parent = 1
    child = parent * 2
    if child + 1 <= heapcount:#오른쪽 자식 존재
        if heap[child] > heap[child+1]:
            child = child + 1

    #자식노드가 존재하고, 부모노드 > 자식노드 = > swap
    while child  <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:#오른쪽 자식 존재
            if heap[child] > heap[child+1]:
                child = child + 1
    return retValue


#최소합
heapcount = 0
temp = [7,2,5,3,4,6]
N = len(temp)
heap = [0] * (N + 1)
for i in range(N):
    heappush(temp[i])

#삭제
for i in range(N):
    print(heappop(), end = ' ')
print()

