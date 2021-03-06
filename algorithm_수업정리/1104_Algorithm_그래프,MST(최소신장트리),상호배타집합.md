# Algorithm

[toc]

## 그래프

- 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현함
- 정점들의 집합과 이들을 연결하는 간선들의 집합으로 구성된 자료 구조
- V : 정점의 개수, E : 그래프에 포함된 간선의 개수
- V개의 정점을 가지는 그래프는 최대 V(V-1)/2 간선이 가능
- 선형 자료구조나 트리 자료구조로 표현하기 어려운 N:N 관계를 가지는 원소들을 표현하기에 용이



### 그래프 유형

- 무향그래프
- 유향그래프
- 가중치그래프
- 사이클 방향이 없는 그래프(DAG)
- 완전그래프
  - 정점들에 대해 가능한 모든 간선들을 가진 그래프
- 부분 그래프
  - 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프



### 인접 정점

- 인접
  - 두개의 정점에 간선이 존재(연결됨)하면 서로 인접해 있다고 한다.
  - 완전 그래프에 속한 임의의 두 정점들은 모두 인접해 있다.



### 그래프 경로

- 경로란 간선들을 순서대로 나열한 것
  - 간선들 : (0,2),(2,4),(4,6)
  - 정점들 : 0 - 2 - 4 - 6

- 경로 중 한 정점을 최대한 한번만 지나는 경로를 **단순경로**라고 함

  - 0-2-4-6, 0-1-6

- 시작 정점에서 끝나는 경로를 **사이클**이라 함
  - 1-3-5-1

  

### 그래프 표현

- 간선의 정보를 저장하는 방식, 메모리나 성능을 고려해서 결정
- 인접 행렬
  - V x V 크기의 2차원 배열을 이용해서 간선 정보를 저장
  - 배열의 배열(포인터 배열)
  - 단점: 노드는 많은데 간선이 적을 때 사용하지 않는 0이 많아 낭비가 심할 수 있음
- 인접리스트
  - 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
  - 각 정점에 대한 인접 정점들을 순차적으로 표현
  - 하나의 정점에 대한 인접 정점들을 각각 노드로 하는 연결리스트로 저장
- 간선의 배열
  - 간선(시작 정점,끝정점)을 배열에 연속적으로 저장

- 두 정점을 연결하는 간선의 유무를 행렬로 표현
  - V x V 정방 행렬
  - 행 번호와 열 번호는 그래프의 정점에 대응
  - 두 정점이 인접되어 있으면 1, 그렇지 않으면 0 으로 표현
  - 무향 그래프
    - i번째 행의 합 = i번째 열의 합 = Vi 의 차수
  - 유향 그래프
    - 행 i의 합 = Vi의 진출 차수
    - 열 i의 합 = Vi의 진입 차수

### 그래프 순회(탐색)

- 비선형구조인 그래프로 표현된 모든 자료(정점)를 빠짐없이 탐색하는 것을 의미
- 깊이 우선 탐색(DFS)
- 너비 우선 탐색(BFS)

#### DFS(깊이 우선 탐색)

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

#### 스택

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 선형구조 : 자료 간의 관계가 1대1의 관계를 갖는다.
  - 비선형구조 : 자료간의 관계가 1:N의 관계를 갖는다.(ex, 트리)
- 마지막에 삽입한 자료를 가장 먼저 꺼낸다.
  - 후입선출(LIFO,Last-In-First-Out)이라고 부름

#### 스택의 구현

- 스택을 구현하기 위해서 필요한 저장소와 연산
  - 자료를 선형으로 저장할 저장소
    - C언어에서는 배열을 사용할 수 있다.
    - 저장소 자체를 스택이라 부르기도 한다
    - 스택에서 마지막 삽입된 원소의 위치를 top이라 부름
- 연산

| push    | 저장소에 자료를 삽입(저장)한다.              |
| ------- | -------------------------------------------- |
| pop     | 저장소에서 자료를 꺼낸다(삽입한 자료의 역순) |
| isEmpty | 스택이 공백인지 아닌지를 확인하는 연산       |
| peek    | 스택의 top에 있는 item(원소)을 반환하는 연산 |



#### 스택의 구현

- 스택의 삽입/삭제 과정
  - 빈 스택에 원소 A,B,C를 차례로 삽입 후 한번 삭제하는 연산과정



#### BFS(너비우선탐색)

- 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함



#### 큐

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
  - 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어진 구조
- 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장 먼저 삽입된 원소는 가장 먼저 삭제된다.
  - 선입선출구조(FIFO:First in First Out)



##### 큐의 구조 및 기본연산

1. 공백 큐 생성 : createQueue()
2. 원소 A삽입 : enQueue(A)
3. 원소 B삽입 : enQueue(B)
4. 원소 반환/삭제 : deQueue()
5. 원소 C삽입 : enQueue(C)
6. 원소 반환/ 삭제 : deQueue()
7. 원소 반환/삭제 : deQueue()



##### 큐의 구현

- 삽입 : deQueue()

  - 가장 앞에 있는 원소를 삭제하기 위해

  1. front 값을 하나 증가시켜 큐에 남아있게 될 첫번째 원소 이동
  2. 새로운 첫번째 원소를 리턴함으로써 삭제와 동일한 기능함

```python
deQueue(Q)
	if isEmpty()
    	QUEUE_EMPTY
    else
    	front <- front +1
        return Q[front]
```

- 공백상태 및 포화상태 검사 : isEmpty(),isFull()
  - 공백상태 : front = rear
  - 포화상태 : rear = n-1(n:배열의 크기, n-1: 배열의 마지막 인덱스)

```python
isEmpty()
	IF front = rear : RETURN TRUE
    ELSE			: RETURN FALSE

isFull()
	IF rear = n-1	: RETURN TRUE
    ELSE			: RETURN FALSE
```





## 서로소 집합들(Disjoint-Sets)

- 서로소 또는 상호배타 집합들은 **서로 중복 포함된 원소가 없는 집합들**이다. 다시말해 교집합이 없다.
  - 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다. 이를 대표자라 한다.



### 서로소 집합(Disjoint-Sets)

- 상호배타 집합을 표현하는 방법
  - 연결 리스트
  - 트리
- 상호배타 집합 연산
  - Make-Set(x)
  - Find-Set(x)
  - Union(x,y)



### Union-Find란?

- Disjoint Set을 표현할 때 사용하는 알고리즘

- 집합을 구현하는 데는 비트 벡텅, 배열, 연결 리스트를 이용할 수 있으나 그 중 가장 효율적인 트리 구조를 이용하여 구현한다.

  

### 상호 배타 집합 표현- 연결리스트

- 같은 집합의 원소들은 하나의 연결리스트로 관리한다.
- 연결리스트의 맨 앞의 원소를 집합의 대표 원소로 삼는다.
- 각 원소는 집합의 대표원소를 가리키는 링크를 갖는다.

![image-20201104110741310](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104110741310.png)



### 상호배타집합(Union-Find) 표현- 트리

> 트리 구조로 구현하는 이유
>
> 1. 배열
>
> - Array[i]: i번 원소가 속하는 집합의 번호(즉, 루트 노드의 번호)
> - make-set(x)
>   - Array[i] = i와 같이 각자 다른 집합 번호로 초기화한다.
> - union(x, y)
>   - 배열의 모든 원소를 순회하면서 y의 집합 번호를 x의 집합 번호로 변경한다.
>   - 시간 복잡도: O(N)
> - find(x)
>   - 한 번만에 x가 속한 집합 번호를 찾는다.
>   - 시간 복잡도: O(1)
>
> 2. 트리
>
> - 같은 집합 = 하나의 트리, 즉 집합 번호 = 루트 노드
> - make-set(x)
>   - 각 노드는 모두 루트 노드이므로 N개의 루트 노드 생성 및 자기 자신으로 초기화한다.
> - union(x, y)
>   - x, y의 루트 노드를 찾고 다르면 y를 x의 자손으로 넣어 두 트리를 합한다.
>   - 시간 복잡도: O(N)보다 작으므로 find 연산이 전체 수행 시간이 지배한다.
> - find(x)
>   - 노드의 집합 번호는 루트 노드이므로, 루트 노드를 확인하여 같은 집합인지 확인한다.
>   - 시간 복잡도: 트리의 높이와 시간 복잡도가 동일하다. (최악: O(N-1))

- 하나의 집합(a disjoint set)을 하나의 트리로 표현한다.
- 자식 노드가 부모 노드를 가리키며 루트 노드가 대표자가 된다.
- d랑 f가 자기자신을 가리키고 있는 것을 끊고 c와 e를 가리킴

![image-20201104111004678](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104111004678.png)

- d가 속한 대표원소(c)에 f가 속한 대표원소(e)가 가리킴
- 자기자신을 가리키는 애 : 대표원소
- `Find-set(원소)` : 원소의 대표원소를 return

![image-20201104111055525](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104111055525.png)

- 상호배타 집합을 표현한 트리의 배열을 이용한 저장된 모습

![image-20201104111338843](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104111338843.png)

> d가 자기자신을 가리키는지 봄 -> 아님 -> d가 가리키는 idx로 감 -> 그 원소는 자기자신을 가리키는지 봄 - > 맞음 -> 대표원소(c)
>
> union(d,f) : d의 대표원소는 c, f의 대표원소는 e! 대표원소를 찾았으니 f의 대표원소를 d의 대표원소로 바꿈! -> 자기자신을 가리키던 e는 c를 가리키게 됨!



### 상호배타 집합에 대한 연산

- Make-Set(x) 
  - 초기화
  - 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산
  - p[x]에 x를 담음 => 을 가리키게 함

```python
Make_Set(x)
	p[x] <- x
```

- Find-Set(x)
  - 찾기
  - x를 포함하는 집합을 찾는 연산
  - x를 대표하는 대표자를 찾는 연산

```python
Find_Set(x)
	IF x == p[x] : RETURN x
    ELSE		 : RETURN Find_set(p[x])
```

- Union(x,y)
  -  x와 y를 포함하는 두 집합을 통합하는 연산
  - 합하기

> find_set(y) : y를 대표하는 대표값을 찾아라
>
> p[y]에 x를 대표하는 대표값을 넣음!!
>
> => y를 대표하는 대표자를 x의 대표자에게 연결시킴 
>
> **반드시 y의 대표자를 x의 대표자에 연결하는게 아니라 둘중 rank(트리높이)가 높은곳에 연결시킴!!!**

```python
Union(x,y)
	p[Find_Set(y)] <- Find_Set(x)
```



#### Union-Find의 과정

![image-20201104210208370](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104210208370.png)



![image-20201104133858879](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104133858879.png)

- make-set(1)~(6)

| index | 1    | 2    | 3    | 4    | 5    | 6    |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- |
| P     | 1    | 2    | 3    | 4    | 5    | 6    |

- union(1,3)

> 3의 대표자 : 3을 1의 대표자(1)로 연결! 3->1로 바꿈

| index | 1    | 2    | 3    | 4    | 5    | 6    |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- |
| P     | 1    | 2    | 1    | 4    | 5    | 6    |

- union(2,3)

> 3의 대표자 :1을 2의 대표자(2)로 연결! 1->2로 바꿈

| index | 1    | 2    | 3    | 4    | 5    | 6    |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- |
| P     | 2    | 2    | 1    | 4    | 5    | 6    |

- union(5,6)

> 6의 대표자 (6)을 5의 대표자(5)에 연결

| index | 1    | 2    | 3    | 4    | 5    | 6    |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- |
| P     | 2    | 2    | 1    | 4    | 5    | 5    |

- findset(6)  = 5



#### 문제점

- 대표원소가 멀리있다면 찾아가는 시간이 오래걸림
- 트리 구조가 완전 비대칭인 경우
- 연결 리스트 형태
- 트리의 높이가 최대가 된다.
- 원소의 개수가 N일 때, 트리의 높이가 N-1이므로 union과 find(x)의 시간 복잡도가 모두 O(N)이 된다.
- 배열로 구현하는 것보다 비효율적이다.
  

![image-20201104112548419](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104112548419.png)

#### 연산의 효율성을 높이는 방법

##### Rank를 이용한 Union

- 각 노드를 자신을 루트로 하는 subtree의 높이를 랭크Rank라는 이름으로 저장
- 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다

![image-20201104112743997](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104112743997.png)

- 랭크를 이용한 Union에서 랭크가 증가하는 예(Union하는 랭크가 같다면!)

![image-20201104112821527](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104112821527.png)

##### Path compression

![image-20201104210945110](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104210945110.png)

- Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꿔준다.

![image-20201104112912988](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104112912988.png)

- Make_Set() 연산
  - Make_Set(x) : 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

```python
p[x] : 노드 x의 부모 저장
rank[x] : 루트 노드가 x인 트리의 랭크 값 저장
    
Make_Set(x)
	p[x] <- x
    rank[x] <- 0
```

- Find_Set 연산
  - Find_Set(x) : x를 포함하는 집합을 찾는 오퍼레이션
  - 특정 노드에서 루트까지의 경로를 찾아가면서, 노드의 부모 정보를 갱신

```python
Find_Set(x)
	IF x != p[x] // x가 루트가 아닌 경우
    	p[x] <- Find_Set(p[x])
    RETURN p[x]
```

- Union 연산
  - Union(x,y) : x와 y를 포함하는 두 집합을 통합하는 오퍼레이션
  - x와 y중 rank가 높은 곳에 낮은 것을 연결시킴!!!

```python
Union(x,y)
	Link(Find_Set(x), Find_Set(y))
```

```python
Link(x,y)
	IF rank[x] > rank[y]	//rank는 트리의 높이
    	p[y] <- x
    ELSE
    	p[x] <- y
        IF rank[x] == rank[y]
        	rank[y]++
```



### Union-Find의 사용 예시

> 전체 집합이 있을 때 구성 원소들이 겹치지 않도록 **분할(아래 참고*)하는 데 **자주 사용된다.
>
> [참고] 분할(Partition)이란
>
> - 임의의 집합을 분할한다는 것은 각 부분 집합이 아래의 두 가지 조건을 만족하는 Disjoint Set 이 되도록 쪼개는 것이다.
>   1. 분할된 부분 집합을 합치면 원래의 전체 집합이 된다.
>   2. 분할된 부분 집합끼리는 겹치는 원소가 없다.
> - 예를 들어, S = {1, 2, 3, 4}, A = {1, 2}, B = {3, 4}, C = {2, 3, 4}, D = {4}라면
>   - A와 B는 S의 분할 O. A와 B는 Disjoint Set
>   - A와 C는 S의 분할 X. 겹치는 원소가 존재
>   - A와 D는 S의 분할 X. 두 집합을 합해도 S가 되지 않음
>     

- Kruskal MST 알고리즘에서 새로 추가할 간선의 양끝 정점이 같은 집합에 속해 있는지(사이클 형성 여부 확인)에 대해 검사하는 경우
- 초기에 {0}, {1}, {2}, … {n} 이 각각 n+1개의 집합을 이루고 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려는 경우
  - 집합의 표현-백준1717번
- 어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 가입한 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하는 경우
  - 친구 네트워크-백준4195번



#### BOJ_1717_집합의 표현



#### BOJ_4195_친구 네트워크





## 최소신장트리(MST)

### Spanning Tree

> 그래프 내의 모든 정점을 포함하는 트리

- 그래프에서 최소 비용 문제

1. 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
2. 두 정점 사이의 최소 비용의 경로 찾기

- 신장트리
  - n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리
- 최소 신장 트리(Minimum Spanning Tree)
  - 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

- DFS,BFS를 이용하여 그래프에서 신장 트리를 찾을 수 있다.
  - 탐색 도중에 사용된 간선만 모으면 만들 수 있다.
- 하나의 그래프에는 많은 신장 트리가 존재할 수 있다.
- Spanning Tree는 그래프에 있는 n개의 정점을 정확히(n-1)개의 간선으로 연결



### MST

- spanning Tree 중에서 사용된 간선들의 가중치 합이 최소인 트리
- MST = Minimum Spanning Tree = 최소 신장 트리
- 각 간선의 가중치가 동일하지 않을 때 단순히 가장 적은 간선을 사용한다고 해서 최소 비용이 얻어지는 것은 아니다.
- MST는 간선에 가중치를 고려하여 최소 비용의 Spanning Tree를 선택하는 것을 말한다.
- 즉, 네트워크(가중치를 간선에 할당한 그래프)에 있는 모든 정점들을 가장 적은 수의 간선과 비용으로 연결하는 것이다.

#### MST 특징

1. 간선의 가중치의 합이 최소여야 한다.
2. n개의 정점을 가지는 그래프에 대해 반드시 (n-1)개의 간선만을 사용해야 한다.
3. 사이클이 포함되어서는 안된다.



### MST의 구현 방법

#### Prim 알고리즘

> 시작 정점에서 출발하여 신장트리 집합을 **단계적으로 확장** 해나가는 방법

- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식

1. 임의 정점을 하나 선택해서 시작
2. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
3. 모든 정점이 선택될때(트리가 N-1개의 간선을 가질때)까지 `1.,2.`과정을 반복

- 서로소인 2개의 집합(2 disjoint-sets) 정보를 유지
  - 트리 정점들 - MST를 만들기 위해 선택된 정점들
  - 비트리정점들 - 선택되지 않은 정점들

![image-20201104203929816](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104203929816.png)

![image-20201104141457453](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104141457453.png)

```sh
MST_PRIM(G,r) //G:그래프,r:시작정점
	FOR u in G.V
		u.key <- ∞	//u.key : u에 연결된 간선중 최소 가중치
		u.π <-Null	//u.π : 트리에서 u의 부모
    r.key <-0
    Q <-G.V	//우선순의 Q에 모든 정점 넣는다.
    WHILE Q!=0	//빈 Q가 아닐동안 반복
    	u <- Extract_MIN(Q)	//key값이 가장 작은 정점 가져오기
    	FOR v in G.Adj[u]	//u의 인접 정점들
    		IF v ∈Q AND w(u,v) < v.key	//Q에 있는 v의 key값 갱신
    			v.π <- u
    			v.key <- w(u,v)
```

#### Prim 알고리즘의 시간 복잡도

- 주 반복문이 정점의 수 n만큼 반복하고, 내부 반복문이 n번 반복

  - Prim의 알고리즘의 시간 복잡도는 O(n^2)이 된다.
- Kruskal 알고리즘의 시간복잡도는 O(elog2e)이므로

  - 그래프 내에 적은 숫자의 간선만을 가지는 'Sparse Graph'의 경우 Kruskal 알고리즘이 적합
  - 그래프에 간선이 많은 'Dense Graph'의 경우는 Prime 알고리즘이 적합


##### heapq라이프러리 활용을 통해 우선순위큐사용하기

```python
import heapq

queue = []
graph_data = [[2,'A'],[5,'B'],[3,'C']]

for edge in graph_data:
    heapq.heappush(queue,edge)

for index in range(len(queue)):
    print(heapq.heappop(queue))
    
print(queue)

'''
[2,'A']
[3,'C']
[5,'B']
'''
```

##### collections라이브러리의 defaultdict함수 활용

> defaultdict함수를 사용해서 key에 대한 value를 지정하지 않았을 시, 빈 리스트로 초기화

```python
from collections import defaultdict

list_dict = defaultdict(list)
print(list_dict)
print(['key1'])

'''
defaultdict(<class 'list'>, {})
[]
'''
```

##### prim 알고리즘 코드

1. 모든 간선 정보를 저장(adjacent_edges)
2. 임의의 정점을 선택, '연결된 노드 집합(connected_nodes)'에 삽입
3. 선택된 정점에 연결된 간선들을 간선 리스트(candidate_edge_list)에 삽입
4. 간선 리스트에서 최소 가중치를 가지는 간선부터 추출해서,
   - 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 이미 들어있다면, 스킵함(cycle발생을 막기 위함)
   - 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 들어 있지 않으면, 해당 간선을 선택하고, 해당 간선 정보를 '최소신장트리(MST)'에 삽입
     - 해당 간선에 연결된 인접 정점의 간선들 중, '연결된 노드 집합'에 없는 노드와 연결된 간선리스트에 삽입
       - '연결된 노드 집합'에 있는 노드와 연결된 간선들을 간선 리스트에 삽입해도, 해당 간선은 스킵될 것이기 때문
       - 어차피 스킵될 간선을 간선리스트에 넣지 않아서, 간선 리스트에서 최소 가중치를 가지는 간선부터 추출하기 위한 자료 구조 유지를 위한 effort를 줄일 수 있음
5.  선택된 간선은 간선 리스트에서 제거
6. 간선 리스트에 더 이상의 간선이 없을때까지 3~4번을 반복

```python
from collections import defaultdict
from heapq import *


def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    return mst


myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

print(prim('A',myedges))

'''
[(5, 'A', 'D'), (6, 'D', 'F'), (7, 'A', 'B'), (7, 'B', 'E'), (5, 'E', 'C'), (9, 'E', 'G')]
'''
```

##### 개선된 프림 알고리즘

> 근데 이건 heapdict깔아야돼서.....안됨...ㅎ

- 간선이 아닌 노드를 중심으로 우선순위 큐를 적용하는 방식
  - 초기화-정점:key 구조를 만들어놓고, 특정 정점의 key값은 0, 이외의 정점들의 key값은 무한대로 놓음. 모든 정점:key 값은 우선순위 큐에 넣음
  - 가장 key값이 적은 정점:key를 추출한 후(pop하므로 해당 정점:key 정보는 우선순위 큐에서 삭제됨),(extract min 로직이라고 부름)
  - 해당 정점의 인접한 정점들에 대해 key값과 연결된 가중치 값을 비교하여 key값이 작으면 해당 정점:key값을 갱신
    - 정점:key값 갱신시, 우선순위 큐는 최소 key값을 가지는 정점:key를 루트노드로 올려놓도록 재구성함(decrease key로직이라고 부름)
- 개선된 프림 알고리즘 구현시 고려 사항
  - 우선순위 큐(최소힙)구조에서, 이미 들어가 있는 데이터의 값 변경시, 최소값을 가지는 데이터를 루트노드로 올려놓도록 재구성하는 기능이 필요함
  - 구현 복잡도를 줄이기 위해, heapdict 라이브러리를 통해, 해당 기능을 간단히 구현

```python
from heapdict import heapdict


def prim(graph,start):
    mst,keys,pi,total_weight = list(),heapdict(),dict(),0
    
    for node in graph.keys():
        keys[node] = float('inf')
        pi[node] = None
    keys[start],pi[start] = 0,start
    
    while keys:
        current_node,current_key = keys.popitem()
        mst.append([pi[current_node],current_node,current_key])
        total_weight += current_key
        for adjacent,weight in mygraph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_node
    return mst,total_weight
    


myedges = {
    'A' : {'B':7,'D':5},
    'B' : {'A':7,'D':9,'C':8,'E':7},
    'C':{'B':8,'E':5},
    'D' : {'A':5,'B':9,'E':7,'F':6},
    'E':{'B':7,'C':5,'D':7,'F':8,'G':9},
    'F':{'D':6,'E':8,'G':11},
    'G':{'E':9,'F':11}
}
mst,total_weight = prim(mygraph,'A')
print('MST:',mst)
print('Total Weight:',total_weight)
    

'''
MST: [['A', 'A', 0], ['A', 'D', 5], ['D', 'F', 6], ['A', 'B', 7], ['D', 'E', 7], ['E', 'C', 5], ['E', 'G', 9]]
Total Weight: 39
'''
```



#### KRUSKAL 알고리즘

> 탐욕적인 방법을 이용하여 네트워크(가중치를 간선에 할당한 그래프)의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 것
>
> 탐욕적인 방법
>
> - 결정을 해야 할 때마다 그 순간에 가장 좋다고 생각되는 것을 선택함으로써 최종적인 해답에 도달하는 것
> - 탐욕적인 방법은 그 순간에는 최적이지만, 전체적인 관점에서 최적이라는 보장이 없기 때문에 반드시 검증해야 한다.
> - 다행히 Kruskal 알고리즘은 최적의 해답을 주는 것으로 증명되어 있다.
>
> MST(최소 비용 신장 트리)가 
>
> 1. 최소 비요의 간선으로 구성됨
> 2. 사이클을 포함하지 않음
>
> 의 조건에 근거하여 각 단계에서 사이클을 이루지 않는 최소 비용 간선을 선택

- 간선을 하나씩 선택해서 MST를 찾는 알고리즘
- 이전 단계에서 만들어진 신장트리와는 상관없이 무조건 최소 간선만을 선택하는 방법

##### Kruskal 알고리즘의 동작

1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
   - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
3. n-1개의 간선이 선택될 때까지 `2.`를 반복

##### Krusckal 알고리즘의 구체적인 동작 과정

> Kruskal 알고리즘을 이용하여 MST(최소 비용 신장 트리)를 만드는 과정
>
> - 간선 선택을 기반 으로 하는 알고리즘
> - 이전 단계에서 만들어진 신장 트리와는 상관없이 무조건 최소 간선만을 선택하는 방법
>
> **주의!**
>
> - 다음 간선을 이미 선택된 간선들의 집합에 추가할 때 사이클을 생성하는지를 체크!
>   - 새로운 간선이 이미 다른 경로에 의해 연결되어 있는 정점들을 연결할 때 사이클이 형성된다.
>   - 즉, 추가할 새로운 간선의 양끝 정점이 같은 집합에 속해 있으면 사이클이 형성된다.
> - 사이클 생성 여부를 확인하는 방법
>   - 추가하고자 하는 간선의 양끝 정점이 같은 집합에 속해 있는지를 먼저 검사해야 한다.
>   - ‘union-find 알고리즘’ 이용

![image-20201104205214102](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104205214102.png)

![image-20201104150832054](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104150832054.png)

![image-20201104152154553](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104152154553.png)

```python
MST-KRUSKAL(G,w)
	A <- 0 // 0:공집합
    FOR vertex v in G.V	//G.v :그래프의 정점 집합
        Make_Set(v)	//G.e : 그래프의 간선 집합
   	G.E에 포함된 간선들을 가중치 w에 의해 정렬
    
    FOR 가중치가 가장 낮은 간선 (u,v) ∈ G.e 선택(n-1개)
    	IF Find_Set(u) != Find_Set(v)
        	A <- A U {(u,v)}
            Union(u,v)
    RETURN A
```



##### kruskal's algorithm

```python
#path compression기법
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v,node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    #union-by-rank기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()
    #1.초기화
    for node in graph['vertices']:
        make_set(node)

    #2.간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    #3. 간선 연결(사이클 없는)
    for edge in edges:
        weight,node_v,node_u = edge
        if find(node_v) != find(node_u):
            union(node_v,node_u)
            mst.append(edge)
    return mst

mygraph = {
    'vertices':['A','B','C','D','E','F','G'],
    'edges': [
        (7,'A','B'),
        (5,'A','D'),
        (7,'B','A'),
        (8,'B','C'),
        (9,'B','D'),
        (7,'B','E'),
        (8,'C','B'),
        (5,'C','E'),
        (5,'D','A'),
        (9,'D','B'),
        (7,'D','E'),
        (6,'D','F'),
        (7,'E','B'),
        (5,'E','C'),
        (7,'E','D'),
        (8,'E','F'),
        (9,'E','G'),
        (6,'F','D'),
        (8,'F','E'),
        (11,'F','G'),
        (9,'G','E'),
        (11,'G','F'),
    ]
}
parent = dict()
rank = dict()

print(kruskal(mygraph))

'''
[(5, 'A', 'D'), (5, 'C', 'E'), (6, 'D', 'F'), (7, 'A', 'B'), (7, 'B', 'E'), (9, 'E', 'G')]
'''
```

##### SWEA_5249_최소신장트리

- 명균쌤코드

``` python
def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])

    return p[x]

def union(x,y):
    p[find_set(x)] = find_set(y)



for tc in range(1, int(input())+1):
    V, E = map(int,input().split())

    edges = [list(map(int , input().split())) for _ in range(E)]
    edges = sorted(edges, key=lambda x: x[2])
    p = [-1] * (V+1)

    for i in range(V+1):
        make_set(i)

    ans = 0
    cnt = 0
    idx = 0
    while cnt < V:
        if find_set(edges[idx][0]) != find_set(edges[idx][1]):
            union(edges[idx][0], edges[idx][1])
            cnt += 1
            ans += edges[idx][2]
        idx += 1

    print("#{} {}".format(tc, ans))
```

- 내가 다시 적어봄

```python
'''
kruskal algorithm
'''
import sys
sys.stdin = open('input.txt','r')

def make_set(node):
    parent[node] = node

#path compression기법
def find_set(node):
    if parent[node] != node:
        parent[node] = find_set(parent[node])
    return parent[node]

#path compression기법을 썼기때문에 rank상관없음!
def union(x,y):
    parent[find_set(x)] = find_set(y)


def kruskal(graph):
    global ans
    #1. 초기화
    for node in range(V+1):
        make_set(node)

    #2.간선 weight기반 sorting
    #kruskal은 가중치를 기준으로 정렬한 뒤 사용!!!
    graph = sorted(graph,key = lambda x:x[2])

    #3. 간선 연결(사이클 없는)
    for edge in graph:
        n1,n2,weight = edge
        if find_set(n1) != find_set(n2):
            union(n1,n2)
            ans += weight
    return ans


T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    #양끝노드 n1,n2,가중치w
    edges = [list((map(int,input().split()))) for _ in range(E)]
    parent = [-1]*(V+1)
    ans = 0
    print('#{} {}'.format(tc,kruskal(edges)))
```





## 최단 경로

> **가중치는 가중치 인접 행렬이라고 불리는 2차원 배열에 저장**됨, 가중치 인접 행렬은 기존의 인접행렬과 차이점이 있음, 기존의 인접 행렬에서는 간선이 없는 구간에는 행렬의 값을 0으로 함
>
> 그러나 가중치 인접행렬에서는 간선의 가중치 자체가 0일 수도 있기 때문에 **간선이 없음을 나타낼 때 0이라는 값을 사용할 수가 없다.**
>
> 따라서 0 대신 이론적으로 무한대의 값을 가중치 인접 행렬에 저장함으로써 간선이 없다고 표시할 수 있음
>
> ![image-20201104213038988](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104213038988.png)

- **정점 u와 정점 v**를 연결하는 경로 중 **간선들의 가중치 합이 최소가 되는 경로**를 찾는 문제
- 간선의 가중치(비용,거리,시간 등)가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
- 하나의 시작 정점에서 끝 정점까지의 최단 경로
  - 다익스트라(dijkstra)알고리즘
    - 음의 가중치를 허용하지 않음
  - 벨만-포드(Bellman-Ford)알고리즘
    - 음의 가중치 허용
- 모든 정점들에 대한 최단 경로
  - 플로이드-워샬(Floyd-Warshall) 알고리즘



### Dijkstra 알고리즘

> 네트워크에서 하나의 시작 정점으로부터 모든 다른 정점까지의 최단 경로를 찾는 알고리즘
>
> 최단 경로는 경로의 길이순으로 정해짐
>
> **Dijkstra의 알고리즘**에서는 시작 정점에서 집합 S에 있는 정점만을 거쳐서 다른 정점으로 가는 **최단 거리를 기록하는 배열**이 반드시 있어야 한다.
>
> 최단 거리를 기록하는 1차원 배열을 하나 설정하고 이름을 **distance**로 함
>
> **시작 정점을 v**라고 했을때, **distance[v] = 0**이고 다른 정점에 대한 distance값은 시작 정점 간의 가중치가 됨
>
> 가중치는 인접행렬에 저장되므로 **가중치 인접 행렬을 weight라 했을 때 `distance[w] = weight[v][w]`** 과 같이 사용할 수 있다.
>
> 단, **정점 v에서 정점 w로의 직접 간선이 없을 경우에는 무한대의 값**을 저장한다. 시작 단계에서는 아직 최단 경로를 발견하지 못했으므로 **S = { v }** 와 같을 것이다. 즉 처음에는 시작 정점 v를 제외하고는 최단거리가 알려진 정점이 없다. 알고리즘이 진행되면서 **최단 거리가 발견되는 정점들이 S에 하나씩 추가될 것**이다.
>
>  알고리즘의 매 단계에서 **집합 S 안에 있지 않은 정점 중에서 가장 distance 값이 작은 정점을 S에 추가**한다. **새로운 정점 u가 S에 추가되면, S에 있지 않은 다른 정점들의 distance 값을 수정한다.** 시작 기준점이 **u**로 바뀌었기 때문에, **새로 추가된 정점 u**를 거쳐서 정점까지 가는 거리와 기존의 거리를 비교한다. 그 후 **더 작은 거리값을 기준으로 distance값을 수정**한다. 아래와 같은 수식을 이용하면 될 것이다.
>
>  **`distance[w] = min(distance[w], distance[u] + weight[u][w])`** 
>
> min은 stdlib.h에 선언되어 있는 매크로다. 매개 변수로 들어온 두 값중 더 작은 값을 리턴한다.
>
> ![image-20201104213616945](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104213616945.png)
>
> **시작 정점을 0**으로 잡고, 각 지점까지의 거리를 표시했다. **직접적으로 가는 경로가 없는 경우 무한대**로 표시되어 있다. 표시 되어 있는 거리 중 **가장 짧은 거리는 정점 4까지의 거리인 3이므로 정점 4를 집합 S에 추가시켜준다.**
>
> ![image-20201104213636713](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104213636713.png)
>
>  **새로운 정점이 S에 추가되면 다른 정점들의 distance 값이 변경**된다. 0번 정점에서는 직접적으로 갈 수 없던 정점에 새롭게 들어온 정점 4를 통해 직접적으로 갈 수 있기 때문에 **무한대의 값에서 구체적인 정수거리로 정보가 갱신**됐다.
>
> 정보를 갱신할 때는 4번 정점을 기준으로 하고 있으므로, 4번 정점까지의 거리는 기본옵션으로 더해주는 것이 맞다. 즉, 4번 정점에서 뻗어나가는 각 정점에 3을 더해서 distance 배열에 넣어야 한다는 뜻이다.
>
>  또한 **새로운 정점 4를 통해 갈 때 더 짧은 경로가 발견 된다면 그 정보 또한 갱신**을 해준다. 구체적으로는 위의 0번 정점만을 선택했을 때, 1번 정점까지의 거리가 7이였는데, **4번 정점을 택함으로써 이 거리가 5로 줄어들었다.** **즉 더 짧은 거리가 나타나거나 기존의 무한대에서 직접 경로가 생겼을 때 거리(비용) 값을 갱신해준다.**
>
>  갱신된 정보들을 바탕으로 집합 S에 추가할 다음 정점을 선택해보자. **남은 정점 중 가중치가 가장 적게 표시되어 있는 건 정점 1이다.** **1번 정점을 집합 S에 추가**하고, 갱신할 수 있는 정보가 있다면 갱신해주자.
>
> ![image-20201104213745899](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104213745899.png)
>
>  **갱신된 정보는 2번 정점에 대한 가중치**다. 1번 정점을 추가함으로써 2번 정점까지 직접적으로 갈 수 있게 되었으므로 **무한대의 값에서 구체적인 가중치인 9로 수정해준다.** 다음으로, **현재까지의 distance 배열값을 기준**으로 **가장 작은 값은 6번 정점**의 8이므로, 6번 정점을 택한다. 마찬가지로 갱신할 수 있는 정보는 갱신해준다.
>
> ![image-20201104213803349](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104213803349.png)
>
> **6번 정점을 집합 S에 추가함**으로써 갱신할 수 있는 정보는 **정점 3까지의 거리**다. 기존의 14에서 12로 거리가 **단축**되었으므로, 이 값을 갱신했다. 이제 다음에 택할 정점을 생각해보자. **distance 배열에서 가장 작은 가중치는 9이므로 정점 2를 택한다.**
>
> ![image-20201104213833977](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104213833977.png)
>
>  **정점 2를 집합 S에 추가함**으로써 **정점 3까지의 거리가 갱신**되었다. 남은 두 개의 과정은 그림을 올리지 않아도 유추가 가능하다. **가중치가 가장 적은 5번 정점을 선택**하고, 갱신할 정보가 있다면 갱신한다. 그 다음은 **마지막 정점인 3번 정점을 택한다.** 다익스트라 알고리즘은 위와 같은 순서와 원리로 진행 된다.

#### 시간복잡도

`O(ElogE)`

#### Dijkstra알고리즘 구현

- 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식
- 시작정점(s)에서 끝정점(t)까지의 최단 경로에 정점 x가 존재한다.
- 이때, 최단경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단경로 구성된다.
- 탐욕기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사하다.

```sh
s: 시작정점, A: 인접행렬, D:거리
V : 정점 집합, U: 선택된 정점 집합

Dijkstra(s,A,D)
	U = {s}
	
	FOR 모든 정점 v
		D[v] <- A[s][v]
		
    WHILE U !=V
    	D[w]가 최소인 정점 w ∈ V-U를 선택
    	U <- U U {w}
    	
    	FOR w에 인접한 모든 정점 v
    		D[v] <- min(D[v],D[w]+A[w][v])
```



#### 우선순위 큐를 활용한 다익스트라 알고리즘

> 장점
>
> 지금까지 발견된 가장 짧은 거리의 노드에 대해서 먼저 계산
>
> 더 긴 거리로 계산된 루트에 대해서는 계산을 스킵할 수 있음

![image-20201104214456923](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104214456923.png)

- 우선순위 큐는 MinHeap방식을 활용해서, 현재 가장 짧은 거리를 가진 노드 정보를 먼저 꺼내게 됨

##### 1단계 : 초기화

- 첫 정점을 기준으로 배열을 선언하여 첫 정점에서 각 정점까지의 거리를 저장

- 초기에는 첫 정점의 거리는 0, 나머지는 무한대로 저장함(`inf`라고 표현)
- 우선순위 큐에 (거리0,첫정점)만 먼저 넣음

![image-20201104214640926](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104214640926.png)

##### 2단계 : 우선순위 큐에서 추출한(0,A)[첫 노드와의 거리,노드]를 기반으로 인접한 노드와의 거리 계산

- 우선순위 큐에서 노드를 꺼냄

- 처음에는 첫 정점만 저장되어 있으므로, 첫 정점이 꺼내짐
- 첫 정점에 인접한 노드들 각각에 대해, 첫 정점에서 각 노드로 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지의 거리를 비교
- 배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧은 경우, 배열에 해당 노드의 거리를 업데이트
- 배열에 해당 노드의 거리가 업데이트된 경우, 우선순위 큐에 넣음
  - 결과적으로 너비우선탐색 방식과 유사하게, 첫 정점에 인접한 노드들을 순차적으로 방문하게 됨
  - 만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다, 더 긴 거리(루트)를 가진 (노드, 거리)의 경우에는 해당 노드와 인접한 노드간의 거리 계산을 하지 않음
- 이전 표에서 보듯이, 첫 정점 이외에 모두 inf였으므로, 첫 정점에 인접한 노드들은 모두 우선순위 큐에 들어가고, 첫 정점과 인접한 노드간의 거리가 배열에 업데이트됨

![image-20201104214802068](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104214802068.png)

##### 3단계 : 우선순위 큐에서 (1,C) [첫노드와의 거리,노드]를 기반으로 인접한 노드와의 거리 계산

- 우선순위 큐가 MinHeap(최소 힙) 방식이므로, 위 표에서 넣어진 (1,C), (2,D), (8,B) 중  (1,C)이 먼저 추출됨(`pop`)
- 위 표에서 보듯이 1단계까지의 A-B 최단거리는 8인 상황
  - A-C까지의 거리는 1,C에 인접한 B,D에서 C-B는 5, 즉 A-C-B는 1+5 = 6이므로, A-B최단 거리 8보다 더 작은 거리를 발견, 이를 배열에 업데이트
    - 배열에 업데이트했으므로 6,B(즉, A에서 B까지의 현재까지 발견한 최단 거리) 값이 우선순위 큐에 넣어짐
  - C-D의 거리는 2, 즉 A-C-D는 1+2 = 3이므로, A-D의 현재 최단 거리인 2보다 긴 거리, 그래서 D의 거리는 업데이트 되지 않음

![image-20201104215242640](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104215242640.png)



##### 4단계 : 우선순위 큐에서 (2,D) [첫노드와의 거리,노드]를 기반으로 인접한 노드와의 거리 계산

- 지금까지 접근하지 못했던 E와 F거리가 계산됨
  - A-D까지의 거리인 2에 D-E가 3이므로 이를 더해서 E,5
  - A-D까지의 거리인 2에 D-F가 5이므로 이를 더해서 F,7

![image-20201104215429565](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104215429565.png)



##### 5단계 : 우선순위 큐에서 (5,E)[첫 노드와의 거리,노드]를 기반으로 인접한 노드와의 거리 계산

- A-E 거리가 5인 상태에서, E에 인접한 F를 가는 거리는 1, 즉 A-E-F는 5+1=6, 현재 배열에 A-F 최단거리가 7로 기록되어 있으므로, 6,F으로 업데이트
  - 우선순위 큐에 6,F 추가

![image-20201104215626017](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104215626017.png)

##### 6-1단계 : 우선순위 큐에서 (6,B),(6,F)를 순차적으로 추출해 각 노드 기반으로 인접한 노드와의 거리 계산

- 예제의 방향 그래프에서 B노드는 다른 노드로 가는 루트가 없음
- F노드는 A노드로 가는 루트가 잇으나, 현재 A-A가 0인 반면에 A-F-A는 6+5=11, 즉 더 긴 거리이므로 업데이트되지 않음

![image-20201104215750538](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104215750538.png)

##### 6-2단계 : 우선순위 큐에서 (7,F),(8,B)를 순차적으로 추출해 각 노드 기반으로 인접한 노드와의 거리 계산

- A-F로 가는 하나의 루트의 거리가 7인 상황이나, 배열에서 이미 A-F로 가는 현재의 최단 거리가 6인 루트의 값이 있는 상황이므로, 더 긴 거리인 7,F루트 기반 인접 노드까지의 거리는 계산할 필요가 없으므로 스킵
  - 계산하더라도 A-F거리가 6인 루트보다 무조건 더 긴거리가 나옴
- B,8도 현재 A-B 거리가 6이므로, 인접 노드 거리 계산이 필요 없음

- 우선순위 큐를 사용하면 불필요한 계산 과정을 줄임

![image-20201104220007086](1104_Algorithm_그래프,MST(최소신장트리),상호배타집합.assets/image-20201104220007086.png)



#### heapq라이브러리 활용해 구현

> 데이터가 리스트 형태일 경우, 0번 인덱스를 우선순위로 인지, 우선순위가 낮은 순서대로 pop

```python
import heapq

queue = []

heapq.heappush(queue,[2,'A'])
heapq.heappush(queue,[5,'B'])
heapq.heappush(queue,[1,'C'])
heapq.heappush(queue,[7,'D'])
print(queue)
for index in range(len(queue)):
    print(heapq.heappop(queue))
    
'''
[[1,'C'],[5,'B'],[2,'A'],[7,'D']]
[1,'C']
[2,'A']
[5,'B']
[7,'D']
'''
```

##### 탐색할 그래프의 시작정점과 다른 정점들간의 최단거리 구하기

```python
import heapq

mygraph = {
    'A':{'B':8,'C':1,'D':2},
    'B':{},
    'C':{'B':5,'D':2},
    'D':{'E':3,'F':5},
    'E':{'F':1},
    'F':{'A':5}
}

#탐색할 그래프와 시작 정점을 인자로 전달받음
def dijkstra(graph,start):
    #시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성, 무한대(inf)로 초기화
    distances = {node:float('inf') for node in graph}
    #그래프의 시작 정점의 거리는 0으로 초기화해줌
    distances[start] = 0
    #모든 정점이 저장될 큐를 생성
    queue = []
    #그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue,[distances[start],start])
   
    while queue:
        #큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트
        current_distance,current_node = heapq.heappop(queue)
        #이미 방문한 정점을 다시방문, 시간복잡도때문에 시간줄여주기 위해 적어두는 코드
        if distances[current_node] < current_distance:
            continue
        
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            #만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우
            if distance < distances[adjacent]:
                #거리를 업데이트
                distances[adjacent] = distance
                heapq.heappush(queue, [distance,adjacent])
    return distances

dijkstra(mygraph,'A')

'''
{'A':0,'B':6,'C':1,'D':2,'E':5,'F':6}
'''
```



##### 탐색할 그래프의 시작정점과 다른 정점들간의 최단경로 출력하기

```python
import heapq

#방향그래프
mygraph = {
    'A':{'B':8,'C':1,'D':2},
    'B':{},
    'C':{'B':5,'D':2},
    'D':{'E':3,'F':5},
    'E':{'F':1},
    'F':{'A':5}
}

#탐색할 그래프와 시작 정점을 인자로 전달받음
def dijkstra(graph,start,end):
    #시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성, 무한대(inf)로 초기화
    distances = {vertex:[float('inf'),start] for vertex in graph}
    #그래프의 시작 정점의 거리는 0으로 초기화해줌
    distances[start] = [0,start]
    #모든 정점이 저장될 큐를 생성
    queue = []
    #그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue,[distances[start][0],start])
    
    while queue:
        #큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트
        current_distance,current_vertex = heapq.heappop(queue)
        #더짧은 경로가 있다면 무시
        if distances[current_vertex] < current_distance:
            continue
        
        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            #만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우
            if distance < distances[adjacent][0]:
                #거리를 업데이트
                distances[adjacent] = [distance,current_vertex]
                heapq.heappush(queue, [distance,adjacent])
                
    path = end
    path_output = end + '->'
    while distances[path][1]!= start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print(path_output)
    return distances

print(dijkstra(mygraph,'A','F'))

'''
F->E->D->A
{'A':[0,'A'],'B':[6,'C'],'C':[1,'A'],'D':[2,'A'],'E':[5,'D'],'F':[6,'E']}
'''
```



### Dijstra관련문제

#### SWEA_5251_최소이동거리

- 배열이용

```python
'''
다익스트라 이용
1. 인접행렬을 만드는데 초기값으로 값으로 올수 없는 큰값으로 초기화
2. 인접행렬에 s행 e열에(유향그래프) 가중치(w) 입력
3. dist와 visited 배열을 node수만큼 만듦
4. MIN값 갱신과 MIN방문표시
5. 갱신된 MIN값에서 모든 노드들을 둘러보면서 최소값으로 dist를 갱신
'''
import sys
sys.stdin = open('input.txt','r')

#다익스트라로 풀기
def dijkstra():
    dist = [987654321]*(N+1)
    visited = [False] * (N+1)
    #시작 node 거리표시
    dist[0] = 0

    for _ in range(N):
        minIdx = -1
        MIN = 987654321
        #방문표시와 MIN값 갱신
        for i in range(N+1):
            #방문하지 않았고, MIN보다 더 짧다면 MIN값 갱신
            if not visited[i] and MIN > dist[i]:
                MIN = dist[i]
                minIdx = i
        #min값 방문표시
        visited[minIdx] = True
        
        #갱신한 MIN에서 j로 향할때 더 작은 값이 있으면 dist를 더 작은값으로 바꿔줌
        for j in range(N+1):
            #방문하지 않았고, min에서 j로 향하는 값이 더 작은게 있다면 dist[j] 갱신
            if not visited[j] and dist[j] > adj[minIdx][j] + dist[minIdx]:
                dist[j] = adj[minIdx][j] + dist[minIdx]
    return dist[N]

T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())
    adj = [[987654321] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        adj[s][e] = w
    print('#{} {}'.format(tc,dijkstra()))
```

- heapq이용

```python
import heapq

def dijstra():
    # p = [None] * (V+1)
    dist = [987654321] * (V + 1)
    visited = [False] * (V + 1)
    heap = []
    #가중치와 인덱스
    heapq.heappush(heap,(0,0))
    dist[0] = 0

    while heap:
        w, v = heapq.heappop(heap)

        if not visited[v]:
            visited[v] = True
            dist[v] = w
            for i in range(V+1):
                if not visited[i] and (dist[i] > dist[v]+adj[v][i]):
                    heapq.heappush(heap, (dist[v]+adj[v][i], i))


    return dist[V]

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj = [[987654321] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        st, ed, w = map(int, input().split())
        adj[st][ed] = w

    print("#{} {}".format(tc, dijstra()))
```







--------------

## Reference

https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html

https://mattlee.tistory.com/50

https://www.fun-coding.org/Chapter20-shortest-live.html

https://www.fun-coding.org/Chapter20-prim-live.html