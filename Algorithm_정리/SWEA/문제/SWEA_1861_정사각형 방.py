'''
arr[i][j]방에 Aij가 적혀있음 이 숫자는 모든 방에 대해 서로 다름
이동하려는 방이 존재해야함, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야됨
처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있는가?

출력
처음 출발해야 하는 방 번호, 최대 몇개의 방을 이동할수있는지.
이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그중 가장 작은 수 출력
dfs -> 재귀에러 뜸
bfs로 풀기
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,0,1,-1] #우좌하상
dj = [1,-1,0,0]
# def DFS(i,j):
#     global cnt
#     visited[i][j] = True
#     # print(i,j)
#     for d in range(4):
#         ni = i + di[d]
#         nj = j + dj[d]
#         if ni < 0 or ni >= N or nj < 0 or nj >= N:
#             continue
#         #현재 값보다 1큰값이 아니면 지나감
#         if room[ni][nj] != room[i][j] + 1:
#             continue
#         if visited[ni][nj] == True:
#             continue
#         cnt += 1
#         DFS(ni,nj)

#재귀에러떠서... bfs로 풀기
def BFS(i,j):
    global cnt
    q = []
    #시작점 넣기
    q.append([i,j])
    # dist[i][j] = 1
    while q:
        #맨 앞의 원소를 담음
        temp = q.pop(0)
        pi,pj = temp[0],temp[1]
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            # 현재 값보다 1큰값이 아니면 지나감
            if room[ni][nj] != room[pi][pj] + 1:
                continue
            # if dist[ni][nj] != 0:
            #     continue
            cnt += 1
            q.append([ni,nj])
            # dist[ni][nj] = 1 + dist[pi][pj]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    #이동하는 방 최대 이동수
    MAX = 0
    for i in range(N):
        for j in range(N):
            # #몇개의 방을 이동할수 있는지 저장
            cnt = 1
            #방문배열 리셋
            # visited = [[False for j in range(N)] for i in range(N)]
            # dist = [[0 for j in range(N)] for i in range(N)]
            # DFS(i,j)
            BFS(i,j)
            if cnt > MAX:
                MAX = cnt
                START = room[i][j]
                # print(MAX_S,'최대값들')
            #같을 떄는 START값에 저장된 값보다 작은값에서 시작하면 START갱신
            elif cnt == MAX:
                if START > room[i][j]:
                    START = room[i][j]
    print('#{} {} {}'.format(tc,START,MAX))