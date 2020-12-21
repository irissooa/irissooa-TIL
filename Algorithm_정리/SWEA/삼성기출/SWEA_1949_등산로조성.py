'''
2020-12-02 19:10
NxN 최대한 긴 등산로를 만들 계획
각 숫자는 지형의 높이
등산로를 만드는 규칙
1. 가장 높은 봉우리에서 시작
2. 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로또는 세로 방향으로 연결
즉, 높이가 같은곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가
3. 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K깊이만큼 지형을 깎는 공사를 할 수 있다

가장 긴 등산로를 찾아 그 길이를 출력
dfs 돌려서 제일 높은 봉우리에서 시작하고, 자기 수보다 낮은 칸으로만 dist센다
K를 같이 들고가면서 하나씩 다 꺠봄 깬곳 방문처리.. 깨는 것도 1~K번...이니까 방문처리를 그 개수만큼 하고
K만큼 했으면 거긴 지나가고 다른 곳 깨고,,, 엄청 많은 경우의 수 있을 듯...ㅎ
그렇게 해서 길이가 가장 긴것 갱신
'''
import sys
sys.stdin = open('input.txt','r')
from collections import deque

di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]

def mountain(i,j,k,l):
    global longest
    pi,pj,pk = i,j,k
    visited[pi][pj] = True
    # print('-pi,pj,pk,MAP[pi][pj],l-')
    # print(pi,pj,pk,MAP[pi][pj],l)
    if longest < l:
        longest = l
    for d in range(4):
        ni = pi + di[d]
        nj = pj + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if visited[ni][nj]:
            continue
        if MAP[ni][nj] >= MAP[pi][pj] and pk:
            for nk in range(1,K+1):
                if MAP[ni][nj]-nk >= MAP[pi][pj]:
                    continue
                MAP[ni][nj] -= nk
                # print('-K썼다 ni,nj,nk,MAP[ni][nj],l-')
                # print(ni, nj, nk, MAP[ni][nj], l+1)
                visited[ni][nj] = True
                mountain(ni,nj,0,l+1)
                visited[ni][nj] = False
                MAP[ni][nj] += nk
                # print('-K끝 ni,nj,nk,MAP[ni][nj],l-')
                # print(ni, nj, nk, MAP[ni][nj], l+1)
        if MAP[ni][nj] >= MAP[pi][pj]:
            continue
        # print('-ni,nj,pk,MAP[ni][nj],l-')
        # print(ni, nj, pk, MAP[ni][nj], l+1)
        # visited[ni][nj] = True
        mountain(ni,nj,pk,l+1)
        # visited[ni][nj] = False
    visited[pi][pj] = False

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    highest = deque()
    high = 0
    longest = 1
    for i in range(N):
        for j in range(N):
            if MAP[i][j] > high:
                high = MAP[i][j]
                highest = deque()
                highest.append([i,j])
            elif MAP[i][j] == high:
                highest.append([i,j])
    # print(highest,high)
    # for x in MAP:
    #     print(x)
    visited = [[False for j in range(N)] for i in range(N)]
    for r,c in highest:
        # visited[r][c] = True
        mountain(r,c,K,1)
        # visited[r][c] = False

    print('#{} {}'.format(tc,longest))