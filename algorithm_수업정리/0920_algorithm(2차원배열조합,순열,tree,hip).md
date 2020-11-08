# Algorithm

> 2차원배열 조합, 순열, 트리, 힙



## 2차원배열 조합

> 6개의 원소가 있는 2차원 배열 탐색

```python
n = 2, m = 3
for i in range(0,n*m):
    x = i // 3
    y = i % 3
    print((x,y))
'''
(output)
(0,0)
(0,1)
(0,2)
(1,0)
(1,1)
(1,2)
'''
```

- 재귀와 itertools로 2차원 배열에서 N개 만큼의 원소 선택

```python
import itertools
import copy

arr = [[0, 0], [0, 0]]


def combi():
    arr = ['a', 'a', 'b', 'c']
    print((list(itertools.permutations(arr, 2))))
    print((list(itertools.combinations(arr, 2))))


'''
#순열(permutation)
[('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'a'), ('c', 'b')]

#조합(combination)
[('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'b'), ('a', 'c'), ('b', 'c')]
'''


# itertools를 활용한 구현
def itertoolsSetOne():
    posList = []

    # 모든 원소를 담은 리스트를 생성
    for i in range(0, 2 * 2):
        posList.append((i // 2, i % 2))

    # itertools를 활용하여 조합 구하기
    for pos1, pos2, pos3 in itertools.combinations(posList, 3):
        temp = copy.deepcopy(arr)
        temp[pos1[0]][pos1[1]] = 1
        temp[pos2[0]][pos2[1]] = 1
        temp[pos3[0]][pos3[1]] = 1

        for j in range(0,2):
            print(temp[j])
        print()

#재귀를 활용한 구현
def recursionSetOne(start,count):
    #원소를 모두 골랐을 경우 출력
    if count == 0:
        for j in range(0,2):
            print(arr[j])
        print()
        return

    #n번째 원소부터 원소를 선택
    #n개*m(가로길이)
    #2*2는 전체 원소의 개수
    for i in range(start,2*2):
        x = i // 2 #2는m
        y = i % 2 #2는 m

        #원소 선택
        arr[x][y] = 1

        #나머지 배열의 원소들 중에서 count -1만큼을 선택
        recursionSetOne(i+1,count-1)

        #선택한 원소를 초기화
        arr[x][y] = 0


if __name__=='__main__':
    #2차원 배열 arr에서 2가지 원소를 선택하여 1을 삽입하는 조합
    #start:0(시작idx) 갯수 : n(뽑을 원소 수)
    recursionSetOne(0,3)
    itertoolsSetOne()

    #intertools를 활용한 순열과 조합->output 위에 있음
    combi()
    
'''
output
[1, 1]
[1, 0]

[1, 1]
[0, 1]

[1, 0]
[1, 1]

[0, 1]
[1, 1]

[1, 1]
[1, 0]

[1, 1]
[0, 1]

[1, 0]
[1, 1]

[0, 1]
[1, 1]
'''
```



## SWEA_4881_배열최소합

```python
'''
NxN배열 숫자 들어있음
한 줄에 하나씩 N개의 숫자를 골라 합이 최소가 되도록 함
세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없음
최소합을 구하라
'''
import sys
sys.stdin = open('input.txt','r')

def powerset(idx,SUM):
    global MIN
    #더한값이 이미 최소값보다 크다면 멈춤!(가지치기)
    if SUM >= MIN:
        return
    if idx == N:
        if MIN > SUM:
            MIN = SUM
            return
    for k in range(N):
        #방문한 열은 건너뛰기!
        if visited[k]:
            continue
        visited[k] = True
        powerset(idx+1,SUM+arr[idx][k])
        visited[k] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)
    sel = [0]*N
    #방문한 열은 못가도록 방문표시!!
    visited = [False for _ in range(N)]
    MIN = 987654321
    powerset(0,0)
    print('#{} {}'.format(tc,MIN))
```





## 중위순회

```python
'''
중위순회
'''
import sys
sys.stdin = open('input.txt','r')
def LPR(x):
    if L[x]:
        LPR(L[x])
    print(P[x],end='')
    if R[x]:
        LPR(R[x])
for tc in range(1,11):
    N = int(input())
    P = [0]*(N+1)
    L = [0]*(N+1)
    R = [0]*(N+1)
    for i in range(N):
        temp = list(input().split())
        if len(temp) == 4:
            P[int(temp[0])] = temp[1]
            L[int(temp[0])] = int(temp[2])
            R[int(temp[0])] = int(temp[3])
        elif len(temp) == 3:
            P[int(temp[0])] = temp[1]
            L[int(temp[0])] = int(temp[2])
        else:
            P[int(temp[0])] = temp[1]
    # print(P,L,R)
    LPR(1)
    print()
```



## 이진탐색

```python
'''
이진탐색
중위탐색

'''
def middle(x):
    global num
    if L[x]:
        middle(L[x])
    # print(x,end=' ')
    tree[x] = num
    num+= 1
    if R[x]:
        middle(R[x])
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr= [i for i in range(1,N+1)]
    L = [0]*(N+1)
    R = [0]*(N+1)
    tree = [0]*(N+1)
    num = 1
    for i in range(1,len(arr)//2+1):
        L[i] =2*i
        if 2*i+1 <= N:
            R[i] = 2*i+1
    # print(L,R)
    middle(1)
    print('#{} {} {}'.format(tc,tree[1],tree[N//2]))
```





## 이진힙

```python
'''
이진힙
부모 노드 값 < 자식 노드 값 유지
이진 최소 힙
마지막 노드의 조상노드에 저장된 정수 합 알기
'''
import sys
sys.stdin = open('input.txt','r')

def push(x):
    global hsize
    hsize += 1
    H[hsize]= x
    c = hsize
    p = c//2
    while p and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c//2


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    H = [0]*(N+1)
    hsize = 0
    for i in range(N):
        push(arr[i])
    # print(H)
    ans = 0
    v = N //2
    while v:
        ans += H[v]
        v //= 2
    print('#{} {}'.format(tc,ans))
```





## 노드의 합

```python
'''
후위 순회를 통해 왼쪽 오른쪽 노드 값을 더한 값이 부모노드가 됨!
'''
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    #노드의 개수N, 리프노드의 개수M, 값을 출력할 노드번호L_node
    N,M,L_node = map(int,input().split())
    #M개의 줄 리프노드 번호, 1000이하 자연수 주어짐
    tree = [0]*(N+1)
    for m in range(M):
        temp = list(map(int,input().split()))
        tree[temp[0]] = temp[1]
    l,r=0,0
    for i in range(N//2,0,-1):
        l = tree[i*2]
        if i*2 + 1 <= N:
            r =tree[i*2+1]
        tree[i] += l+r
        # print(i,l,r)
    print('#{} {}'.format(tc,tree[L_node]))
```





## 부분집합의 합

> 알고리즘 거의 초반에 비트로 부분집합 구하는 것 배워서 풀었던 문제를 주아언니랑 같이 조합으로 풀었다!(뿌듯!)

```python
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
M = len(numberList)

def com(idx,sidx):
    global count
    if sidx == N:
        if sum(sel) == K:
            print(sel)
            count +=1
        return
    if idx == M:
        return

    sel[sidx] = numberList[idx]
    # 뽑고가고
    com(idx + 1, sidx + 1)
    # 안뽑고가고
    com(idx + 1, sidx)

    
T = int(input())
for T in range(1, T+1):


    N, K = map(int, input().split())

    sel = [0]*N
    count = 0

    com(0,0)



    print("#{} {}".format(T, count))
```

