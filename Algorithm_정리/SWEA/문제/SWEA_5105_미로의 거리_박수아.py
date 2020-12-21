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
            # print(visited[pi][pj],'거리')
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













#선생님 풀이
dx = [0,0,1,-1]#우좌하상
dy = [1,-1,0,0]
for tc in range(1,int(input())+1):
    N = int(input())
    #문자열로 받음
    maze = [input() for _ in range(N)]
    #정수로 받음
    # maze = [lsit(map(int,input())) for _ in range(N)]

    sx = sy = ex= ey = 0
    for i in range(N):
        for j in range(N):
            #문자열로 받았으니 ''해줘야됨
            if maze[i][j] == '2':
                sx,sy = i,j
            elif maxe[i][j] == '3':
                ex,ey = i,j
    visit = [[0] * N for _ in range(N)]
    Q = [[sx,sy]] #시작점 행과 열을 같이 묶어 넣음
    visit[sx][sy] = 1

    while Q:
        x, y = Q.pop(0)
        #종료조건
        if x == ex and y == ey:
            break
        for i in range(4):
            tx,ty = x + dx[i], y + dy[i]

            #경계 체크(가장먼저!!해야됨), 통로인지, 방문정보 체크해야됨
            #N보다 클수 없기 떄문에 ==로 표시
            if tx < 0 or tx == N or ty < 0  or ty ==N:
                continue
                #벽인경우 못감, 또는 이미 방문을 했다면
            if maze[tx][ty] == '1' or visit[tx][ty]:
                continue
            visit[tx][ty]  = visit[x][y] +1
            # #종료조건
            # if tx == ex and ty ==ey:
            #     Q.clear()
            #     break
            Q.append([tx,ty])
    #출발과 도착의 칸 개수를 빼줘야 원하는 거리가 나옴
    #but 도착하지 못하는 경우, 0
    if visit[ex][ey]: #0이아닌경우
        visit[ex][ey] -= 2
    
    print(visit[ex,ey])
