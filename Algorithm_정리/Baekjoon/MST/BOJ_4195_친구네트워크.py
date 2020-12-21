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
