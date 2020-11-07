# MST_Algorithm

[toc]

## BOJ_1717_집합의표현

> [BOJ1717집합의표현](https://www.acmicpc.net/problem/1717)

```python
import sys
input = sys.stdin.readline

def make_set(x):
    p[x] = x

def find_parent(x):
    if p[x] != x:
        p[x] = find_parent(p[x])
    return p[x]

def union(x,y):
    if find_parent(x) != find_parent(y):
        x = find_parent(x)
        y = find_parent(y)
        p[y] = x

n,m = map(int,input().split())
p = [x for x in range(n+1)]
for _ in range(m):
    #합집합 0 a가 포함된 집합과 b가 포함된 집합을 합침
    #두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산 1
    check, a,b = map(int,input().split())
    #1dlaus find_parent
    if check:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a,b)
```





## BOJ_4195_친구의 네트워크

> [BOJ_4195_친구의 네트워크](https://www.acmicpc.net/problem/4195)

```python
import sys
sys.stdin= open('input.txt','r')
input = sys.stdin.readline

def find_parents(x):
    if p[x] != x:
        p[x] = find_parents(p[x])

    return p[x]

def union(x,y):
    if find_parents(x) != find_parents(y):
        x = find_parents(x)
        y = find_parents(y)
        p[x] = y
        cnts[y] += cnts[x]

T = int(input())
for tc in range(1,T+1):
    F = int(input())
    p = dict()
    cnts = dict()
    for _ in range(F):
        s,e = input().split()
        if s not in p:
            p[s] = s
            cnts[s] = 1
        if e not in p:
            p[e] = e
            cnts[e] = 1
        union(s,e)
        ans = find_parents(s)
        print(cnts[ans])

```

