'''
2020-11-28 21:07
NxN인 도시,각 칸 빈칸(0), 치킨집(2), 집(1) 중 하나
r행 c열 1부터 시작
치킨거리 = 집과 가장 가까운 치킨집 사이의 거리(|r1-r2|+|c1-c2|)
도시의 치킨거리는 모든 집의 치킨 거리의 합
M개의 치킨집만 고르고 나머지 치킨집 없애야 됨
어떻게 고르면 도시의 치킨 거리가 가장 작게 될까
출발점인 2를 전부 start에 담는다,
1인 점을 담고, 조합으로 3개의 좌표를 뽑는다
start와 store의 조합을 구한뒤 각각의 거리들을 구하고, 최소값을 뽑자!!!
'''

import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline


def comb(idx):
    global cnt,MIN
    # print(cnt,sel)
    temp = 0
    if cnt == M:
        # print(sel)
        # visited = [0]*len(store)
        for s in range(len(start)):
            # print('--MIN---',MIN)
            minans = sys.maxsize

            for e in range(len(store)):
                if sel[e]:
                    si,sj = start[s]
                    ei,ej = store[e]
                    ans = abs(si-ei) + abs(sj-ej)
                    if minans > ans:
                        minans = ans
                    # print(s,e,ans,minans,temp)
            temp += minans
            if temp > MIN:
                return
        if MIN > temp:
            MIN = temp
        return
    if idx == len(store):
        return
    sel[idx] = store[idx]
    cnt += 1
    comb(idx+1)
    sel[idx] = 0
    cnt -=1
    comb(idx+1)



N, M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
start,store = deque(),deque()
for i in range(N):
    for j in range(N):
        #집
        if city[i][j] == 1:
            start.append([i+1,j+1])
        #치킨집
        if city[i][j] == 2:
            store.append([i+1,j+1])
# print('start',start)
# print(N,M,'store',store)
# for x in city:
#     print(x)
sel = [0]*len(store)
cnt = 0 #몇개뽑았는지 세어줌
MIN = sys.maxsize
# visit = [0]*len(store)
comb(0)
print(MIN)