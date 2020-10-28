# Permutation&Combination

[toc]

## 1. itertools 모듈

```python
from itertools import permutations
from itertools import combinations

a = []
b = []
items= [1,2,3,4]
for i in list(combinations(items,2)):
    a.append(i)
print(a)

for i in list(permutations(items,2)):
    b.append(i)
print(b)
```



## 2. 재귀 함수

### 2.1

```python
def comb(lst,n):
	ret = []
	if n > len(lst): return ret
	
	if n == 1:
		for i in lst:
			ret.append([i])
	elif n>1:
		for i in range(len(lst)-n+1):
			for temp in comb(lst[i+1:],n-1):
				ret.append([lst[i]]+temp)

	return ret

def perm(lst,n):
	ret = []
	if n > len(lst): return ret

	if n==1:
		for i in lst:
			ret.append([i])
	elif n>1:
		for i in range(len(lst)):
			temp = [i for i in lst]
			temp.remove(lst[i])
			for p in perm(temp,n-1):
				ret.append([lst[i]]+p)

	return ret
```



### 2-2.순열만들기

```python
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

    
permutation('ABCD', 2)
permutation([1, 2, 3, 4, 5], 3)
```

**#1.**

먼저 사용자가 원하는 *arr* 과 *r* 을 받는다. 그리고 *arr* 을 오름차순 정렬하는데 여기서는 큰 의미가 있지는 않고 단순히 출력을 이쁘게 하기 위해서이다. 그리고 ***used* 변수를 만드는데, 이 변수는 *i* 번째 값을 썼는지 저장하는 데 쓰인다.** 우리는 모든 순열을 하나씩 만들고 출력하는데 당연히 중복값은 저장되어서는 안 된다.

**#2.**

실제 순열을 만들 *generate* 함수를 생성한다. 먼저 ***chosen* 변수는 순열의 원소를 저장되는 변수인데 이 배열에 값을 하나씩 추가하다가 그 개수가 *r* 이 되는 순간 하나의 순열이 만들어진 것이므로 출력 후 종료한다.**

**#3.**

이 함수의 핵심이다. 모든 순열은 *arr* 의 0부터 *i-1* 번째 값으로 시작하기에 *for* 문으로 다 만들어야 한다. 그리고 ***chosen* 에 값 추가 후, *used* 에 해당 변수를 사용했다고 체크한다. 그 다음 다시 *generate* 를 반복한다. 하나가 만들어진 후에는 그 값을 uncheck해줘야 한다.**



#### 중복 피하기

> **중복되는 원소에 등장하는 순서를 정하는 것이다. 예제에서 ‘A’가 두 개면, ‘A’에 보이지 않는 0, 1의 인덱스를 줘서 순서를 지켜서 등장하게 하면 중복이 나오지 않는다.**

```python
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
        for i in range(len(arr)):
	    # 3.
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)


>>> permutation('AABC', 2)


['A', 'B']
['A', 'C']
['B', 'A']
['B', 'C']
['C', 'A']
['C', 'B']
```

**#3.**

어떤 원소에 대해 그 원소가 등장할 순서일 때는 바로 추가하는 것이 아니라 다음과 같은 조건을 만족해야 한다.

1. *i* 가 0일 때,
   - *i* 가 0이면 배열의 첫 원소이기 때문에 바로 쓰면 된다.
2. *arr[i-1] != arr[i]* 일 때
   - 지금은 *arr* 이 정렬되어 있다. 이때 *i* 번째 원소가 *i-1* 번째와 다르면 그냥 ‘B’, ‘C’ 처럼 서로 다른 원소이기 때문에 바로 쓴다.
3. *used[i-1]* 일 때
   - **가령 *i* 번째 원소가 두 번째 ‘A’이면, 중복을 피하기 위해 첫 번째 ‘A’가 사용된 상태여야만 쓸 수 있다.** 그래서 *i-1* 번째 원소가 쓰인 상태인지 확인한다.

이렇게 하면 순열일 때 중복을 피할 수 있다.



### 2.3 조합만들기

```python
def combination(arr, r):
    # 1.
    arr = sorted(arr)

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])


combination('ABCDE', 2)
combination([1, 2, 3, 4, 5], 3)
```

**#1.**

입력은 순열 때와 같다. 배열도 마찬가지로 정렬한다.

**#2.**

조합을 만드는 *generate* 함수를 만든다. 순열과 마찬가지로 *chosen* 에 저장된 아이템 개수가 *r* 개이면 조합이 하나 완성된 것이기 때문에 값을 출력하고 함수를 종료시킨다.

**#3.**

*for* 문을 돌리되, 시작을 *chosen* 에 저장된 마지막 값 다음으로 정한다. 이는 아까 순열함수와 대비되는 부분으로, 조합은 순열과 달리 순서를 고려하지 않고 뽑기 때문에, 가짓수를 제한해줘야 한다. *start* 가 *chosen* 이 비어있을 경우 0이 되는 것도 참고한다. 빈값일 때는 그냥 0을 넣어야 한다.



#### 중복피하기

```python
def combination(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])


>>> combination('ABCDE', 2)
>>> combination([1, 2, 3, 4, 5], 3)
```





## 3. 바이너리 카운팅을 통한 사전적 순서

- 부분집합을 생성하기 위한 가장 자연스러운 방법
- 원소 수에  해당하는 N개의 비트열을 이용
- n번째 비트값이 1이면 n번째 원소가 포함되었음을 의미

```python
arr = [3,6,7,1,5,4]
n = len(arr)

for i in range(0,(1<<n)): # 1<<n : 부분집합의 개수
	for j in range(0,n): #원소의 수만큼 비트를 비교함
        if i & (1<<j): #i의 j번째 비트가 1이면 j번째 원소 출력
            print('%d'%arr[j],end ='')
    print()            
```



### 



## 4. DFS/BFS

```python
def dfs_comb(lst,n):
	ret = []
	idx = [i for i in range(len(lst))]

	stack  = []
	for i in idx[:len(lst)-n+1]:
		stack.append([i])
	
	while len(stack)!=0:
		cur = stack.pop()

		for i in range(cur[-1]+1,len(lst)-n+1+len(cur)):
			temp=cur+[i]
			if len(temp)==n:
				element = []
				for i in temp:
					element.append(lst[i])
				ret.append(element)
			else:
				stack.append(temp)
	return ret

def dfs_perm(lst,n):
	ret = []
	idx = [i for i in range(len(lst))]

	stack  = []
	for i in idx:
		stack.append([i])
	
	while len(stack)!=0:
		cur = stack.pop()

		for i in idx:
			if i not in cur:
				temp=cur+[i]
				if len(temp)==n: 
					element = []
					for i in temp:
						element.append(lst[i])
					ret.append(element)
				else:
					stack.append(temp)
```





## Reference

[python순열,조합구현 출처](https://medium.com/@dltkddud4403/python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%EA%B5%AC%ED%98%84-5e496e74621c)

[shoark7참고](https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations)