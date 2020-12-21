#최소힙만 지원(heapq)
import heapq
heap1 = [7,2,5,3,4,6] #list
print(heap1)
heapq.heapify(heap1)
print(heap1)
heapq.heappush(heap1,1)
print(heap1)
while heap1:
    print(heapq.heappop(heap1), end = ' ')
print()
temp = [7,2,5,3,4,6]
heap2 = []
for i in range(len(temp)):
    #우선순위 -temp[i]가 먼저, 같다면 temp[i]를 기준으로 정렬
    heapq.heappush(heap2,(-temp[i],temp[i]))
heapq.heappush(heap2,(-1,1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2)[1],end = ' ')
    # print(heapq.heappop(heap2)[0]*(-1),end = ' ')
