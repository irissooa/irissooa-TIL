'''
NxM연구소 바이러스 상하좌우로 퍼져나감, 새로 세울수 있는 벽 3개!
0은 빈칸, 1은 벽, 2는 바이러스
바이러스가 퍼질 수 없는 곳, 안전영역! 그 크기가 최대인 것을 구해라
완전탐색...0인것들 중 3곳씩만 1로 바꾼뒤 바이러스가 얼마나 퍼지는지 bfs돌리고, 0인곳 세기! 최댓값 갱신
'''
import sys
from collections import deque
import copy
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

#조합!
def comb(idx,sidx):
    if sidx == 3:
        wall = []
        for s in sel:
            wall.append([bin[s][0],bin[s][1]])
        temp = copy.deepcopy(start)
        BFS(temp,wall)
        return
    if idx == len(bin):
        return
    sel[sidx] = idx
    comb(idx+1,sidx+1)
    sel[sidx] = 0
    comb(idx+1,sidx)

di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]
def BFS(q,sel):
    global MAX
    visited = [[False for j in range(M)] for i in range(N)]
    #처음시작점 방문처리
    for v in q:
        i,j = v
        visited[i][j] = True
    #조합으로 뽑은 수 방문 처리(벽이 됐기 때문)
    for s in sel:
        i,j = s
        visited[i][j] = True
    # print(sel,q)
    cnt = zero
    while q:
        if cnt <=MAX:
            break
        pi,pj = q.popleft()
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if visited[ni][nj]:
                continue
            if laboratory[ni][nj] == 1:
                continue
            if not visited[ni][nj] and not laboratory[ni][nj]:
                cnt+=1
            if cnt <= MAX:
                break
            # print(ni,nj)
            visited[ni][nj] = True
            q.append([ni,nj])
    # print('여기안오니')
    ans = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and not laboratory[i][j]:
                # print(ans,'여긴!!!!')
                ans += 1
    # for x in visited:
    #     print(x)

    if MAX < ans:
        MAX = ans
    return

N,M = map(int,input().split())
laboratory = [list(map(int,input().split())) for _ in range(N)]
start = deque()
bin = deque()
MAX = 0
#0인곳과, start(바이러스가 있는곳)위치 담기
for i in range(N):
    for j in range(M):
        if laboratory[i][j] == 2:
            start.append([i,j])
        if laboratory[i][j] == 0:
            bin.append([i,j])
zero = len(bin)-3
sel = [0]*3
comb(0,0)
print(MAX)


