'''
dfs 인접리스트를 만듦, 방문표시, 그러고 cnt
'''
import sys
sys.stdin = open('input.txt','r')

def DFS(node):
    visited[node] = True
    for next in linked[node]:
        if not visited[next]:
            DFS(next)


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    # print(arr)
    linked = [[] for j in range(N+1)]
    for i in range(0,len(arr),2):
        # print(arr[i],arr[i+1],i,i+1)
        linked[arr[i]].append(arr[i+1])
        linked[arr[i+1]].append(arr[i])
    # print(linked)
    visited = [False for i in range(N+1)]
    cnt = 0
    for i in range(1,N+1):
        if not visited[i]:
            cnt+=1
            DFS(i)
    print('#{} {}'.format(tc,cnt))