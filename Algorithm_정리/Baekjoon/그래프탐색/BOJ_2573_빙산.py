'''
2020-12-10 11-
빙산이 주어짐, 0과 접한 개수만큼 빙산이 다 녹음 두덩어리 이상으로 분리되지 않으면 0출력
분리된다면 최소 시간 구하기

1. 빙산에 4방향으로 보면서 0개수만큼 빼고 temp배열에 담아주기
2. 모두 봤다면 temp를 보면서 덩어리가 나뉘어졌는지 확인
3. 다시 반복

BFS,DFS는 시간초과, 메모리초과가 난다...
시간초과를 어떻게 줄이지ㅠ
#배열을 만들어서 하지말고 [i,j,zero]를 담아줘서 전부 확인 후에 arr에 직접 i,j -zero해보자
'''
import sys
input = sys.stdin.readline
from collections import deque

di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def DFS(i,j):
    visited.add((i,j))
    zero = 0
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue
        if (ni,nj) in visited:
            continue
        if not arr[ni][nj]:
            zero+=1
            continue
        DFS(ni,nj)
    change.append([i,j,zero])


def BFS(i,j):
    q = deque()
    q.append([i,j])
    visited.add((i,j))
    while q:
        pi,pj = q.popleft()
        zero = 0
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if (ni,nj) in visited:
                continue
            if not arr[ni][nj]:
                zero+=1
                continue
            visited.add((ni,nj))
            q.append([ni,nj])
        change.append([pi,pj,zero])

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
year = 0
change = deque()
while True:
    cnt = 0
    # temp = [[0 for j in range(M)] for i in range(N)]
    visited = set()
    # 처음, 마지막은 0이니까 안봐도됨
    for i in range(1,N-1):
        for j in range(1,M-1):
            if arr[i][j] and ((i,j) not in visited) and cnt<2:
                cnt +=1
                # DFS(i,j)
                BFS(i,j)
    # print(change)
    if cnt >=2:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
    year += 1
    while change:
        i,j,zero = change.popleft()
        arr[i][j] -= zero
        if arr[i][j] <0:
            arr[i][j] = 0
    # for x in arr:
    #     print(x)