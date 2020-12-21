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
