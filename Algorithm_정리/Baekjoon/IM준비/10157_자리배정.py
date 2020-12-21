'''
대기번호가 달팽이 채우기 처럼 상, 우, 하,좌 순서로 번호가 매겨진다
여기서 좌표 x,y 는 열,행값이다!
1,1부터 방문하면서 좌표모습으로 봤을 때 우, 하, 좌 상으로 이동!
방문하지 않았으면서 배열내에서 우, 하 , 좌, 상 순으로 번호를 매기며 그 방문배열에 번호를 매기며
K번째가 됐을 때 (x,y)를 출력
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint

# # #델타, 우하좌상
# di = [0,1,0,-1]
# dj = [1,0,-1,0]
# def check(i,j):
#     global num,result
#     #방문했으니 방문표시
#     num += 1
#     visited[i][j] = num
#     #종료조건
#     if num == K:
#         # print('들어왓따')
#         result=[i,j]
#         # return result
#     print(num,i,j)
#     #델타이동
#     for d in range(4):
#         ni = i + di[d]
#         nj = j + dj[d]
#         # #K가 num으로 나눴을 때 1이하가 아니면 건너뜀
#         # if K // num >1:
#         #     continue
#         #범위밖이라면 건너뜀
#         if ni < 1 or ni > C or nj <1 or nj > R:
#             continue
#         #방문한 곳이라면 지나감
#         if visited[ni][nj]:
#             continue
#         check(ni,nj)

#공연장 격자 크기 C,R
C,R = map(int,input().split())
#방문배열
visited =[[False for j in range(R)] for i in range(C)]
#관객 대기번호
K = int(input())
num = 1

# 번호를 매김
#관객에게 좌석을 배정할 수 없는 경우 0 출력
if K >C*R:
    print(0)
    # exit()
else:
    #델타, 우하좌상
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    i,j,d = 0,0,0

    while True:
        visited[i][j] = num
        if num == K:
            print(i+1,j+1)
            break
        num += 1
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < C and 0 <= nj < R and visited[ni][nj] == False:
            i,j = ni,nj

        else:
            d = (d+1) % 4
            i += di[d]
            j += dj[d]
            # continue
        # if visited[ni][nj]:
        #     d = (d+1)%4
        #     i += di[d]
        #     j += dj[d]
        #     continue
# print(visited)





    pprint(visited)
    # print(result[0],result[1])
