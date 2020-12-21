import sys
sys.stdin=open('input.txt','r')
from pprint import pprint

'''
또..다른 아이디어...
가로, 세로 자른 길이들을 담고 가장 큰 값들끼리 곱하기
'''
#
# #가로, 세로
# c,r = map(int,input().split())
# arr = [[1 for j in range(c)] for i in range(r)]
# # pprint(arr)
# #자를 점선의 개수
# N = int(input())
# C = [0,r] #가로 idx
# R = [0,c] #세로 idx
#
# for _ in range(N):
#     #가로인지 세로인지, 점선idx
#     dir, idx = map(int,input().split())
#     #가로
#     if dir == 0:
#         C.append(idx)
#     else: #세로
#         R.append(idx)
# R.sort()
# C.sort()
# # print(R,C)
# garo,sero = [],[]
# #
# #넓이를 어떻게 구하자ㅣ이이이이이이이이
# #가로는 리스트 안의 연속된 두개의 차, 세로도 마찬가지
# for rr in range(len(R)-1):
#     garo.append(R[rr+1]-R[rr])
#     # print('가로',garo)
#     for cc in range(len(C)-1):
#         sero.append(C[cc+1]-C[cc])
#         # print('세로',sero)
# print(max(garo)*max(sero))






'''
이거도 망함....다시푼다..
가로,세로 자를 배열의 idx를 각각 리스트에 저장
제일 작은 idx부터 잘라진 사각형의 넓이를 구함
넓이를 비교하며 가장 큰 값을 구함
'''
#가로, 세로
c,r = map(int,input().split())
arr = [[1 for j in range(c)] for i in range(r)]
# pprint(arr)
#자를 점선의 개수
N = int(input())
C = [0,r] #가로 idx
R = [0,c] #세로 idx
for _ in range(N):
    #가로인지 세로인지, 점선idx
    dir, idx = map(int,input().split())
    #가로
    if dir == 0:
        C.append(idx)
    else: #세로
        R.append(idx)
R.sort()
C.sort()
# print(R,C)
MAX = 0
#넓이를 어떻게 구하자ㅣ이이이이이이이이
#가로는 리스트 안의 연속된 두개의 차, 세로도 마찬가지
# for rr in range(len(R)-1):
#     garo = R[rr+1]-R[rr]
#     print('가로',garo)
#     for cc in range(len(C)-1):
#         sero = C[cc+1]-C[cc]
#         print('세로',sero)
#         area = garo*sero
#         print('넓이',area)
#         if area > MAX:
#             MAX = area
for cc in range(len(C)-1):
    sero = C[cc+1]-C[cc]
    # print('세로',sero)
    for rr in range(len(R)-1):
        garo = R[rr+1]-R[rr]
        # print('가로',garo)
        area = garo*sero
        # print('넓이',area)
        if area > MAX:
            MAX = area
print(MAX)
#


# DFS풀이 ....망
# di = [0,0,1,-1]#우좌하상
# dj = [1,-1,0,0]
# def DFS(i,j):
#     global cnt
#     visited[i][j] = True
#
#     for d in range(4):
#         ni = i + di[d]
#         nj = j + dj[d]
#         if arr[ni][nj] == 0:
#             continue
#         if visited[ni][nj]:
#             continue
#         cnt += 1
#         DFS(ni,nj)
#
# C,R=map(int,input().split())
# N=int(input())
# #전체 색종이 배열을 만듦
# arr=[[1]*C for _ in range(R)]
# #0으로 띠를 둘러줌
# arr.insert(0,[0]*C)
# arr.append([0]*C)
#
# for x in arr:
#     x.insert(0,0)
#     x.append(0)
# # pprint(arr)
#
# #색종이를 자르는 곳에 0으로 넣어주기
# for _ in range(N):
#     #가로,세로 & 점선번호
#     dir, idx = map(int,input().split())
#     #가로라면
#     if dir==0:
#         #해당 idx에 추가를 해주는데 가로에 추가된만큼 idx가 변동될수있음
#         #만약 앞에 0이 들어온게 있다면 idx에 그 수만큼 더해줘야됨..->이걸 어떻게 처리할까?
#         #idx앞에 0 이 있으면(제일앞 0 제외) 그 개수만큼 더해줌
#         plus = 1
#         for i in range(1,idx):
#             if arr[1][i] == 0:
#                 plus += 1
#         arr.insert(idx+plus,[0]*(len(arr[0])))
#         print('가로추가',plus)
#         pprint(arr)
#     #세로라면
#     else:
#         #세로도 마찬가지 idx를 어떻게 지정해줄까...
#         for x in arr:
#             # 해당 idx에 추가를 해주는데 세로에 추가된만큼 idx가 변동될수있음
#             # 만약 앞에 0이 들어온게 있다면 idx에 그 수만큼 더해줘야됨..->이걸 어떻게 처리할까?
#             # idx앞에 0 이 있으면(제일앞 0 제외) 그 개수만큼 더해줌
#             plus = 1
#             for i in range(1, idx):
#                 if arr[i][1] == 0:
#                     plus += 1
#             x.insert(idx+plus,0)
#         print('세로추가',plus)
#         pprint(arr)
# print()
# pprint(arr)
# #dfs돌리기
# visited = [[False for j in range(len(arr[0]))] for i in range(len(arr))]
# ans = []#넓이 값을 받을 리스트
# #세로값이 변동됐으니 len으로 그 값을 받음
# for i in range(len(arr)):
#     #가로값도 바꼈으니 arr의 첫번째 리스트의
#     for j in range(len(arr[0])):
#         if arr[i][j] == 1 and visited[i][j] == False:
#             cnt = 1
#             DFS(i,j)
#             ans.append(cnt)
# print(max(ans))