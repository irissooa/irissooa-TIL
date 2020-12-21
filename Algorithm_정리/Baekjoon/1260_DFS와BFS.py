'''
정점 여러개인 경우 작은번호부터 방문, 더이상 방문 할 수 없으면 종료
정점번호는 1번부터 N번까지
정점 개수 N 간선개수 M 탐색 시작할 정점 V
M개의 줄 간선 연결하는 두 정점 번호 주어짐
간선 양방향
첫줄에 DFS수행 결과, 다음 줄 BFS수행 결과 방문 V부터 방문된 점을 순서대로 출력
'''
def DFS(v):
    visited[v] = True
    print(v,end = ' ')
    #해당정점의 인접리스트 보기!
    for i in arr[v]:
        if visited[i] == False:
            # print(i,end=' ')
            DFS(i)

def BFS(v):
    q=[]
    q.append(v)
    dist[v] = 1
    while q:
        top=q.pop(0)
        print(top,end= ' ')

        for i in arr[top]:
            if dist[i] == 0:
                # print('i',i)
                dist[i]=dist[top] +1
                q.append(i)






N,M,V = map(int,input().split())
#인접리스트
arr = [[]*(N+1) for _ in range(N+1)]
for m in range(M):
    st,ed = map(int,input().split())
    #양방향
    arr[st].append(ed)
    arr[ed].append(st)
for i in range(N+1):
    arr[i] = sorted(arr[i])
# print(arr)
visited = [False for _ in range(N+1)]
dist = [0 for _ in range(N+1)]
DFS(V)
print()
BFS(V)