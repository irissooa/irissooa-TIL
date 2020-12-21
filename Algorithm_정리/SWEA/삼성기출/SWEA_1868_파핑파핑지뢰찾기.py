'''
2020-12-02 11:40
표의 각 칸에는 지뢰가 있을 수도 있고, 없을 수도 있음
각 칸을 클릭했을때 지뢰가 있다면 파핑 파핑! 소리와 함께 끝남
지뢰가 없는 칸이라면 변이 맞닿아있거나 꼭지점이 맞닿아 있는 최대 8칸에 대해
몇 개의 지뢰가 있는지 0~8사이의 숫자로 클릭한 칸에 표시됨
만약 이 숫자가 0이라면 근처의 8방향에 지뢰가 없다는 것이 확장돼 그 방향의 칸도 자동으로 숫자를 표시해줌
지뢰의 위치를 알 수 잇을때
지뢰를 '*'로, 지뢰가 없는칸을 '.'로, 클릭한 지뢰가 없는 칸을 'C'로 나타냈을때
표가 어떻게 변하나?
파핑파핑 지뢰찾기를 할때 표의 크기와 표가 주어지고, 지뢰가 있는칸을 제외한
다른 모든 칸의 숫자들이 표시되려면 최소 몇 번 클릭을 해야하는지 구해라

8방향으로 보는데 주변에 지뢰의 개수를 세고 MAP에 입력해줌
0인 것 먼저 클릭
나머지 지뢰가 아닌것 클릭
'''
import sys
sys.stdin = open('input.txt','r')
from collections import deque
di = [-1,1,0,0,-1,1,-1,1] #상하좌우, 우상대 우하대 좌상대 좌하대
dj = [0,0,-1,1,1,1,-1,-1]

# 지뢰수 찾아 2차원리스트 갱신
def find(i,j):
    q = deque()
    q.append([i,j])
    while q:
        pi,pj = q.popleft()
        cnt = 0
        for d in range(8):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if MAP[ni][nj] == '*':
                cnt += 1
                continue
        MAP[pi][pj] =cnt

def click(i,j):
    q = deque()
    q.append([i,j])
    visited[i][j] = True
    while q:
        pi,pj = q.popleft()
        for d in range(8):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if visited[ni][nj]:
                continue
            if MAP[ni][nj] == 0:
                q.append([ni,nj])
            visited[ni][nj] = True



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]
    visited = [[False for j in range(N)] for i in range(N)]
    ans = 0
    zeroList = deque()
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == '.':
                find(i,j)
            if MAP[i][j] == 0:
                zeroList.append([i,j])
    # print(zeroList)
    for r,c in zeroList:
        if not visited[r][c]:
            click(r,c)
            ans += 1
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and MAP[i][j] != '*':
                ans+=1

    # for x in MAP:
    #     print(x)
    print('#{} {}'.format(tc,ans))