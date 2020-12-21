'''
2020-11-30 15:30
NxN 몇칸 사과, 상하좌우 끝에 벽이 있음
뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
뱀 맨위,맨좌측에서 위치, 길이는 1, 처음에 오른쪽을 향함
뱀이동규칙
1. 몸 길이를 늘려 머리를 다음 칸에 위치시킴
2. 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
3. 만약 이동한 칸에 사과가 없다면, 몸 길이를 줄여서 꼬리가 위치한 칸을 비워줌
즉, 몸길이는 변하지 않음,
사과의 위치와 뱀의 이동경로가 주어질때 이 게임이 몇초에 끝나는지 계산

방향은 오른쪽부터! dir을 처음부터 pop해서  X를 -1씩 줄여나가며 0이됐을때 방향이 L(왼쪽)인지 D(오른쪽)인지 확인한 뒤 90도
우 -> L:상,D:하
하 -> L:우, D:좌
좌 -> L:하, D:상
상 -> L:좌,D:우
L 은 (d+3)%4, D는 (d+1)%4방향을 확인하면됨!!

뱀이 처음부터 이동할때 다음칸을 볼때 사과가 있으면 그 사과(2)를 0으로 바꾸고 뱀이 위치한 좌표 표시하며 계속하면서 움직임,
만약에 사과가 없다면 제일끝 뱀좌표pop함
만약 1인 백에 닿거나 자기몸에 부딪히면 게임 끝, 초 세어주기
'''

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque
di =[0,1,0,-1] #우하좌상
dj = [1,0,-1,0]
def snake(i,j):
    global time
    visited.append([i,j])
    pi,pj,d = i,j,0
    px,pd = dir.popleft()
    while True:
        ni = pi + di[d]
        nj = pj + dj[d]
        # print('ni,nj',ni,nj,visited)
        # print('px,pd,time',px,pd,time)
        time +=1
        if arr[ni][nj] == 1 or [ni,nj] in visited:
            return
        if arr[ni][nj] == 0:
            visited.popleft()
            visited.append([ni,nj])
        if arr[ni][nj] == 2:
            arr[ni][nj] = 0
            visited.append([ni,nj])
        pi,pj = ni,nj
        if px == time:
            if pd == 'L':
                d = (d+3)%4
            else:
                d = (d+1)%4
            if dir:
                px,pd = dir.popleft()



N = int(input())
# 1로 둘러싸서 벽을 만듦
arr = [[1]+[0 for j in range(N)]+[1] for i in range(N)]
arr.insert(0,[1]*(N+2))
arr.insert(N+1,[1]*(N+2))
#사과개수
K = int(input())
#사과 위치, 정수행, 정수열 1행1열부터 시작(여긴 사과없음)
for k in range(K):
    r,c = map(int,input().split())
    arr[r][c] = 2
# for x in arr:
#     print(x)
#뱀의 방향 변환 횟수
dir = deque()
L = int(input())
for l in range(L):
    #정수  X, 문자  C
    X,C = input().split()
    # 게임시작시간으로부터 X초가 끝난 뒤 왼쪽 'L'또는 오른쪽'D'로 90도 회전시킨다는 뜻
    dir.append([int(X),C])
visited = deque()
time = 0
snake(1,1)
print(time)