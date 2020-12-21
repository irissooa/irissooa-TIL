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


