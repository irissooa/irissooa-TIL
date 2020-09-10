# Algorithm

> Tree, Heap



## Heap

> 최댓값과 최솟값을 빠르게 찾기 위해 고안된 자료구조

- 각 노드의 key값이 해당 노드의 key값보다 작지 않거나 크지 않은 완전 이진트리
- 키 값의 대소관계는 부모-자식 노드 사이 간에만 성립, 형제 노드 사이에는 영향X
- 자식 노드의 최대 개수는 힙의 종류에 따라 다르지만 이진트리에서는 최대 2개
- i번째 노드의 자식 노드가 2개인데, 왼쪽자식노드 :`2i` , 오른쪽 자식노드 `2i+1`, 부모노드 `i//2`



### heapq module

> 파이썬에서 제공하는 모듈, 일반적인 리스트를 min heap처럼 다룰 수 있게 해줌

```python
import heapq

#노드 추가 : heappush메소드를 이용
heap = []
heapq.heappush(heap, 1)



#노드 삭제 : heappop 메소드 이용
'''
가장 작은 원소를 꺼내 리턴, 자동적으로 그 다음으로 작은 원소가 루트노트가 됨
주의!!!! : 인덱스 1이 2번재로 작다는 보장은 없으므로 n번째로 작은 원소를 얻고 싶다면 n-1개의 원소를 빼내야 함.
'''
return heapq.heappop(heap)

#최소값으로 꺼내지 않고 리턴만 하려면 인덱스로 접근하기
print(heap[0])



#기존에 사용한 리스트를 힙으로 변환하기 : heapify 메소드 이용(시간복잡도 O(n))
tmp = [7,5,8,3]
heapq.heapify(tmp)




#최대 힙 만들기 : 우선순위가 포함된 튜플 이용하기
import heapq

nums = [4,1,7,3,8,5]
heap = []

for num in nums:
    heapq.heappush(heap,(-num,num)) #(우선순위, 값)
    
while heap:
    print(heapq.heappop(heap)[1]) #index 1
```

[참고](https://hocheon.tistory.com/70)



### Heap Sort 파이썬 구현

>1. 주어진 원소들로 최대 힙을 구성
>2. 최대 힙의 루트노드(현재 배열의 첫번째 요소, 최댓값)와 말단로드(현재 배열의 마지막 요소)를 교환
>3. 새 루트노드에 대해 최대 힙 구성
>4. 원소의 개수만큼 2.와 3.을 반복



```python
unsorted = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

'''
힙 성질을 만족하도록 하는 연산 heapify
heapify의 계산복잡성 = 트리의 높이(h=log2n)에 의존적
값을 비교하거나 바꾸는 연산은 O(1)이므로 
결과적으로 heapify의 계산복잡성은 O(logn)
'''
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

        
def heap_sort(unsorted):
    n = len(unsorted)
    '''
    BUILD-MAX-HEAP (A) : 위의 1단계
    인덱스 : (n을 2로 나눈 몫-1)~0
    최초 힙 구성시 배열의 중간부터 시작하면
    이진트리 성질에 의해 모든 요소값을 서로 한번씩 비교할 수 있게 됨 : O(n)
    '''
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    
    '''
    Recurrent (B) : 2~4단계
    한번 힙이 구성되면 개별 노드는
    최악의 경우에도 트리의 높이(logn)만큼의 자리 이동을 하게 됨
    이런 노드들이 n개 있으므로 : O(nlogn)
    '''
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted
```

- ` BUILD-MAX-HEAP (A)`의 인덱스(i)에 따른 정렬 과정

|   i    |               data                |
| :----: | :-------------------------------: |
| 초기값 | [16, 4, 10, 14, 7, 9, 3, 2, 8, 1] |
|   4    | [16, 4, 10, 14, 7, 9, 3, 2, 8, 1] |
|   3    | [16, 4, 10, 14, 7, 9, 3, 2, 8, 1] |
|   2    | [16, 4, 10, 14, 7, 9, 3, 2, 8, 1] |
|   1    | [16, 14, 10, 8, 7, 9, 3, 2, 4, 1] |
|   0    | [16, 14, 10, 8, 7, 9, 3, 2, 4, 1] |

- `(B) Recurrent`부분의 인덱스에 따른 정렬 과정

|  i   |               data                |
| :--: | :-------------------------------: |
|  9   | [1, 14, 10, 8, 7, 9, 3, 2, 4, 16] |
|  8   | [1, 8, 10, 4, 7, 9, 3, 2, 14, 16] |
|  7   | [2, 8, 9, 4, 7, 1, 3, 10, 14, 16] |
|  6   | [2, 8, 3, 4, 7, 1, 9, 10, 14, 16] |
|  5   | [1, 7, 3, 4, 2, 8, 9, 10, 14, 16] |
|  4   | [2, 4, 3, 1, 7, 8, 9, 10, 14, 16] |
|  3   | [1, 2, 3, 4, 7, 8, 9, 10, 14, 16] |
|  2   | [1, 2, 3, 4, 7, 8, 9, 10, 14, 16] |
|  1   | [1, 2, 3, 4, 7, 8, 9, 10, 14, 16] |

[참고](https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/)





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

