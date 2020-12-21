'''
node의 idx -> arr[idx]으로 그래프가 이어짐
dfs로  이어진 node들의 개수를 구하기!
'''

import sys
sys.stdin = open('input.txt','r')


def DFS(s):
    visited[s] = True
    e = node[s]
    if not visited[e]:
        DFS(e)


T =int(input())
for tc in range(1,T+1):
    #순열의크기N
    N = int(input())
    #순열, index맞춰줌
    node = [0]+ list(map(int,input().split()))
    visited = [False for _ in range(N+1)]
    cnt = 0
    for idx in range(1,N+1):
        if not visited[idx]:
            DFS(idx)
            cnt+=1
    print(cnt)