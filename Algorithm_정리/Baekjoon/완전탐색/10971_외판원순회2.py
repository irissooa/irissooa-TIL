'''
#1. cost배열의 idx(0,1..N-1)까지의 순열을 구함! -> 각 순서를 list에 list로 담음
하지만 순회하기 때문에 0으로 시작하는 순열만 구하면 됨!!
#2. cost[i][j]는 i도시에서 j도시까지 가는 비용을 나타냄, i,j에 각 순서를 담음
예를들어 [0,1,2,3] 순서면
total = cost[0][1] + cost[1][2] + cost[2][3] + cost[3][0]이다.
여기서 cost값이 0 이면 길이없음! 안됨!!
이렇게 해서 total이 최소값인 것을 구하라!
'''
import sys
sys.stdin = open('input.txt','r')

from itertools import permutations

# #순열 구하는 함수
# #cost의 idx, 순열을 담을 list 길이, 방문표시할 리스트 길이
# def perm(nidx,p_len,v_len):
#     global idxLists
#     if nidx == p_len:
#         print(p)
#  이렇게 하니까...출력되는 p가 추가되는게 아니라..마지막 p가 여러번 append돼있다..ㅠ
#         idxLists.append(p)
#         print(idxLists)
#         return
#     for i in range(v_len):
#         if not v[i]:
#             v[i] = 1
#             p[nidx] = cost_idx[i]
#             perm(nidx+1,p_len,v_len)
#             v[i] = 0

N = int(input())
cost =[]
for _ in range(N):
    cost.append(list(map(int,input().split())))
cost_idx = [i for i in range(N)]
#순열을 담을 리스트
idxLists = []
for i in list(permutations(cost_idx,N)):
    #어차피 순환할거니까 앞이 0인 idx만 순열로 뽑기
    if i[0]:
        break
    idxLists.append(i)
# print(idxLists)
#idx 순열 둘러보면서 MIN값 찾기
MIN = 987654321
for idx in idxLists:
    total=0
    #마지막에 자신한테로 돌아와야됨, 그래서 처음부터 -1,0idx부터 더해줌!
    for i in range(len(idx)):
        if cost[idx[i-1]][idx[i]]:
            total += cost[idx[i-1]][idx[i]]
        #값이 0이면 다음 idx로 넘어가기, MIN갱신못하게 total최대값으로 줌
        else:
            total = 987654321
            break
    if MIN > total:
        MIN = total
print(MIN)
