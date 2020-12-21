'''
20:10->22:00
0->빈칸
1->벽
2->바이러스위치

바이러스 위치를 받아서 start지점으로 두고, start에 넣어둠! + 빈칸 개수 세어둠
start 개수 중 M개를 조합으로 뽑음
그리고 bfs돌리고 모든 빈칸에 바이러스를 퍼뜨리면 최소시간 갱신!
모든 빈칸에 퍼뜨릴 수 없으면 -1 출력
'''
import sys
sys.stdin = open('input.txt','r')
from collections import deque
INF = sys.maxsize


def comb(idx):
    global MIN,order
    if sum(sel) > M:
        return
    if idx == S:
        if sum(sel) != M:
            return
        ans = 0
        for i in range(S):
            if sel[i]:
                order.append(start[i])
        # print(order)
        ans = BFS(order)
        if ans != -1 and MIN > ans:
            MIN = ans
        return
    sel[idx] = 1
    comb(idx+1)
    sel[idx] = 0
    comb(idx+1)

di = [-1,1,0,0] #상하좌우
dj = [0,0,-1,1]
def BFS(q):
    times = [[0 for j in range(N)] for i in range(N)]
    MAX = -INF
    cnt= 0
    for x in q:
        i,j = x
        times[i][j] = -1
    while q:
        pi,pj = q.popleft()
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if times[ni][nj]:
                continue
            if virus[ni][nj] == 1:
                continue
            if virus[ni][nj] !=2:
                cnt+=1
            if times[ni][nj] == -1:
                continue
            if times[pi][pj] ==-1:
                times[ni][nj] = 1
            else:
                times[ni][nj] = times[pi][pj] + 1
            if not virus[ni][nj] and MAX < times[ni][nj]:
                MAX = times[ni][nj]
            q.append([ni,nj])
    if cnt != zero:
        MAX = -1
    # for x in times:
    #     print(x)
    # print(MAX)
    return MAX

N,M = map(int,input().split())
virus = [list(map(int,input().split())) for _ in range(N)]
start = deque()
order = deque()
zero = 0
MIN = INF
# for x in virus:
#     print(x)
#시작점을 담아주고 0인 값을 센다
for i in range(N):
    for j in range(N):
        if virus[i][j] == 2:
            start.append([i,j])
        if not virus[i][j]:
            zero += 1
S = len(start)
sel = [0] * S
#zero가 0이라면 안해줘도 되니까 바로 0출력
if not zero:
    print(0)
else:
    #조합으로 start중에서 M개를 뽑아서 BFS돌려주고, times중 최댓값이 작은거 갱신! -> 빈칸이 다 안채워지면 -1 출력
    comb(0)
    if MIN == INF:
        print(-1)
    else:
        print(MIN)
