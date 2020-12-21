'''
처음에는 NxN땅 모두 양분5씩
M개의 나무를 심었다
봄 -> 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
각 나무는 자기칸의 양분만 먹고, 여러 나무가 있을 경우 나이가 어린 나무부터 양분을 먹음
만약, 땅에 양분이 부족하다면 그 나무는 바로 죽고 여름에 죽은나무//2만큼 양분 추가
가을 -> 나무 번식, 번식하는 나무는 나이가 5의배수여야함, 인접한 8개 칸에 나이가 1인 나무가 생김
겨울 -> 땅을 돌아다니며 땅에 양분 추가, 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어짐
K년이 지난 후 살아있는 나무 개수?
'''
import sys
sys.stdin= open('input.txt','r')
input = sys.stdin.readline
import heapq
from collections import deque

di = [-1,1,0,0,-1,1,-1,1]#상하좌우,우상대,우하대,좌상대,좌하대
dj = [0,0,-1,1,1,1,-1,-1]

def year():
    # print('--봄--')
    # for x in tree:
    #     print(x)
    for i in range(N):
        for j in range(N):
            food = land[i][j]
            temp = deque()
            if not tree[i][j]:
                continue
            while tree[i][j]:
                # print(type(tree[i][j]),i,j)
                t = tree[i][j].popleft()
                # print(i,j,t)
                ans = food-t
                # 여름 만약 양분이 부족하면 그 t//2만큼 양분 추가
                if ans < 0:
                    # print('---여름--')
                    land[i][j] += t//2
                    # print(t,t//2,land[i][j])
                # 봄 , 나이추가해서 다시 넣기
                else:
                    temp.append(t+1)
                    # print('나이듦',temp,ans)
                    land[i][j] = ans
                    food = ans
            # heapq.heapify(temp)
            # print(temp)
            tree[i][j].extend(temp)
            # for t in temp:
            #     heapq.heappush(tree[i][j],t)
            # print(i,j,tree[i][j])
    # for x in tree:
    #     print(x)
#     가을
#     print('----가을----')
    for i in range(N):
        for j in range(N):
            if not tree[i][j]:
                continue
            for t in tree[i][j]:
                # 나무가 5의 배수라면
                # print(t)
                # print(t)
                # print(tree[i][j])
                if not t % 5:
                    pi,pj = i,j
                    for d in range(8):
                        ni = pi + di[d]
                        nj = pj + dj[d]
                        if ni < 0 or ni >= N or nj < 0 or nj >= N:
                            continue
                        tree[ni][nj].insert(0,1)
#    겨울
#     print('---겨울----')
    for i in range(N):
        for j in range(N):
            land[i][j] += A[i][j]
    # for x in land:
    #     print(x)

N,M,K = map(int,input().split())
tree = [[deque() for j in range(N)] for i in range(N)]
land = [[5 for j in range(N)] for i in range(N)]
# 각 칸에 추가되는 양분의 양
A = deque()
# print('----땅양분----')
# for x in land:
#     print(x)
for _ in range(N):
    A.append(list(map(int,input().split())))
# print('----A-----')
# for x in A:
#     print(x)
info = deque()
for _ in range(M):
    # 심은 나무 i,j,나이age
    info.append(list(map(int,input().split())))
for t in info:
    i,j,age = t
    tree[i-1][j-1].append(age)

# print('----나무----')
# for x in tree:
#     print(x)
for _ in range(K):
    year()
cnt = 0
# for x in tree:
#     print(x)
for i in range(N):
    for j in range(N):
        if tree[i][j]:
            for t in tree[i][j]:
                cnt += 1
print(cnt)