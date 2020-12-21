'''
연결되어 있는 컴퓨터 개수 구하기
dfs로 풀어보쟈
정점을 옮길때마다 +1
'''
def DFS(v):
    global num
    visited[v] = True
    for i in arr[v]:
        if visited[i] == False:
            num += 1
            DFS(i)
#컴퓨터수
N = int(input())
#컴퓨터 쌍
M=int(input())
arr = [[]*(N+1) for _ in range(N+1)]
for i in range(M):
    st,ed = map(int,input().split())
    arr[st].append(ed)
    arr[ed].append(st)
# print(arr)
num = 0
visited = [False for _ in range(N+1)]
DFS(1)
print(num)