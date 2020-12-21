'''
방문하지 않은, 주변을 보면서 맨 왼쪽에서 오른쪽 아래로 도착하게함! bfs(최소)
dist에 합을 넣음
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,1]#우하
dj = [1,0]
def BFS(i,j):
    dist[i][j] = numbers[i][j]
    q = [(i,j)]
    while q:
        pi,pj = q.pop(0)
        for d in range(2):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            #다음값에 들어갈 합이 현재까지 누적합 + 현재값보다 크다면 굳이 갈필요 없음, pass
            if dist[ni][nj] < dist[pi][pj] + numbers[ni][nj]:
                continue
            
            #누적합 갱신
            dist[ni][nj] = dist[pi][pj] + numbers[ni][nj]
            q.append((ni,nj))



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = []
    dist = [[987654321 for j in range(N)] for i in range(N)]
    for n in range(N):
        numbers.append(list(map(int,input().split())))

    # print(numbers)
    BFS(0,0)
    # print(dist)
    print('#{} {}'.format(tc,dist[N-1][N-1]))
