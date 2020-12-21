'''
정사각형으로 이루어진 섬과 바다
섬의 개수를 세는 프로그램
가로,세로,대각선 방향 이동 가능 -> 8방향델타
dfs로 붙어있는 섬의 개수 출력
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
sys.setrecursionlimit(10**6)

di =[0,1,0,-1,-1,1,-1,1]#우하좌상 우상대 우하대 좌상대 좌하대
dj = [1,0,-1,0,1,1,-1,-1]
def DFS(i,j):
    visited[i][j] = True
    for d in range(8):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= h or nj < 0 or nj >= w:
            continue
        if visited[ni][nj]:
            continue
        if not MAP[ni][nj]:
            continue
        DFS(ni,nj)

while True:
    #지도 너비 w, 높이 h
    w,h = map(int,input().split())
    #입력의 마지막 줄에는 0 두개가 주어짐
    if w == 0 and h == 0:
        break
    MAP = []
    visited = [[False for j in range(w)] for i in range(h)]
    #h개 줄 지도 1:땅,0은바다
    for _ in range(h):
        MAP.append(list(map(int,input().split())))
    print(h,w)
    pprint(MAP)
    num = 0
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1 and not visited[i][j]:
                DFS(i,j)
                num +=1
    print(num)