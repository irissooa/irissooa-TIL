# Algorithm BFS, Queue

## BFS

## SWEA_ 5105_미로의 거리

```python
'''
NxN크기 미로
최소 몇 개의 칸을 지나면 출발지 도착?
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수,
경로가 없는 경우 0을 출력
1:벽, 0:통로 2:출발 3:도착
bfs로 품
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,0,1,-1]#우좌하상
dj = [1,-1,0,0]
def BFS(i,j):
    # global dist
    q = []
    q.append([i,j]) #시작점 넣기[i,j]
    visited[i][j] = -1 #방문을 했다는 표시..와 동시에 처음부터 거리를 1빼줌

    while q: #q가 비어있지 않으면 계속 돈다
        temp = q.pop(0) #맨앞의 원소를 담음
        #현재의 i와 j를 변수로 표시
        pi, pj = temp[0],temp[1]
        #종료조건
        if maze[pi][pj] == 3:
            # print(visited[pi][pj],'거ㄹㅣ')
            return visited[pi][pj]

        #4방향 탐색
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            #범위를 벗어났다면 넘어가기
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
                #갈수있는 자리가 아니거나
            if maze[ni][nj] == 1:
                continue
                #이미 거리를 구했다면 넘어가기
            if visited[ni][nj] != 0:
                continue
            #그게아니다!! 거리를 갱신 후 큐에 삽입
            q.append([ni,nj]) #다음 좌표를 추가
            ###제일중요!!!!!방문처리를 여기다가 해줌(최단거리를 구할때 보통 현재위치 pi,pj의 방문배열에다가 1씩 더해줌!-> 다음좌표로 넘어가면서 1씩 더해짐)
            visited[ni][nj] = 1 + visited[pi][pj]
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    visited = [[0 for j in range(N)] for i in range(N)]
    dist = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                result = BFS(i,j)
    print('#{} {}'.format(tc,result))
```



## SWEA_5102_노드의 길이

```python
'''
V개의 노드 개수
방향성 없는 E개 간선
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는가
S와 G가 서로 연결되어 있지 않다면 0 출력
BFS이용, 방문하면 +1을 하여 최단 거리를 기록함
인접리스트도 이용함
'''
import sys
sys.stdin =open('input.txt','r')

def BFS(s):
    q = []
    #시작점을 넣는다
    q.append(s)
    visited[s] = 1

    while q:# q가 있다면
        #queue는 선입선출, 제일 앞 정점을 뽑음
        p = q.pop(0)

        #해당 정점의 인접리스트를 볼거야
        for i in adj_list[p]:
            #그 정점을 방문하지 않았다면
            if not visited[i]:
                #queue에 append를 하고 방문표시
                q.append(i)
                visited[i] = visited[p] + 1 #다음 방문표시를 해주는데, 현 방문표시에+1로 거리를 표현함
            #종료조건(도착한다면)
            if p == G:
                #출발점(0부터시작인데 1이 더해졌으니 빼줌)
                return visited[G]-1
    #도착하지 못한다면
    return 0



T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    #인접 리스트
    adj_list = [[] for _ in range(V+1)]
    #간선수만큼 시작점, 끝점 이어진 것 표시
    for i in range(E):
        st,ed = map(int,input().split())
        #시작점(idx)의 list에 ed를 넣음
        adj_list[st].append(ed)
        #끝점(idx)의 list에 st를 넣음
        adj_list[ed].append(st)
    S, G = map(int,input().split())
    visited = [0] * (V+1) #정점+1개의 방문배열 만듦,0idx는 사용안함
    # BFS(S)

    print('#{} {}'.format(tc,BFS(S)))
```

