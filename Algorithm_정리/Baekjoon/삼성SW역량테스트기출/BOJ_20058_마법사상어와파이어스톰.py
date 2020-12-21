'''
20-12-13 18:25-20(잠시뷰...22:40)+14일 19-20
L의 크기에따라 arr을 2**L의 정사각형을 arr에서 나눠서 그 부분을 시계방향으로 90도 회전
파이어스톰을 시전하려면 단계L을 정함
파이어스톰을 Q번 시전
전부 회전시킨 다음, 각 칸마다 상하좌우를 봤을대 얼음이 없는 0 인 값이 하나라도 있으면 얼음의 양이 1줄어듦
모든 파이어스톰(L의 수만큼 돌린다음)
1. 남아있는 얼음 A[r][c]의 합
2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
구해라

1. 2**N정사각형 배열을 temp로 만듦
2. 각 범위만큼 돌릴건데 arr[i][j] = temp[j][2**L-1-i]의 위치에 가는데
for i in range(0,2**N,2**L); for j in range(0,2**N,2**L);for r in range(2**L);for c in (2**L)
arr[i+r][j+c] = temp[i+c][j+2**L-1-r] 에 담는다
3. 각 칸을 회전시킬때 arr[i][j]가 0이 아닌 값을 q에 바뀐 좌표로 담아줌
4. 회전을 다한 뒤, q에 담긴 값들을 돌리면서 상하좌우에얼음이 아닌것이 2개이상 있으면 그 값을 -1해주고 그 값이 0이 아니면 다시 nextq에담아줌!
5. L을 전부 돌린 후 q에 담긴 값을 돌려보면서 연결된 덩어리 개수를 구하고 MAX값 갱신

'''
import sys
input = sys.stdin.readline
from collections import deque

di = [-1,1,0,0] #상하좌우
dj = [0,0,-1,1]
def rotate(L):
    temp = [[0 for j in range(2**N)] for i in range(2**N)]
    # 돌림
    q = deque()
    for i in range(0,2**N,2**L):
        for j in range(0,2**N,2**L):
            for r in range(2**L):
                for c in range(2**L):
                    temp[i+c][j+2**L-1-r] = arr[i+r][j+c]
                    if arr[i+r][j+c]:
                        q.append((i+c,j+2**L-1-r))

    #q를 바탕으로 상하좌우 돌아보며 얼음이 아닌것이 2개이상 있으면 1줄어든다.
    nextq = deque()
    while q:
        pi,pj = q.popleft()
        cnt = 0
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= 2**N or nj < 0 or nj >= 2**N:
                cnt += 1
                continue
            if not temp[ni][nj]:
                cnt += 1
                continue
        if cnt >=2:
            nextq.append((pi,pj))
    #한번에 1씩 줄여주기 -> 이거때문에 시간이 엄청 오래 걸렸따...ㅠ문제이해가 잘안된다,,,
    while nextq:
        pi,pj = nextq.popleft()
        temp[pi][pj] -=1
        if temp[pi][pj] < 0:
            temp[pi][pj] = 0
    return temp

#bfs로 안하면 메모리 초과남
def check(pi,pj):
    global MAX,cnt
    q = deque()
    q.append((pi,pj))
    visited[pi][pj] = True
    while q:
        pi,pj = q.popleft()
        cnt+=1
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= 2**N or nj < 0 or nj >= 2**N:
                continue
            if visited[ni][nj]:
                continue
            if not arr[ni][nj]:
                continue
            visited[ni][nj] = True
            q.append((ni,nj))
    if cnt > MAX:
        MAX = cnt
    return

N,Q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(2**N)]
L_info = list(map(int,input().split()))

#돌리고 arr 다시 갱신
for l in L_info:
    arr = rotate(l)

# L다돌아본 뒤 얼음 뭉치개수 구하기
MAX = 0
visited = [[False for j in range(2**N)] for i in range(2**N)]
SUM = 0
for i in range(2**N):
    for j in range(2**N):
        SUM+=arr[i][j]
        if not visited[i][j] and arr[i][j]:
            cnt = 0
            check(i,j)

print(SUM)
print(MAX)