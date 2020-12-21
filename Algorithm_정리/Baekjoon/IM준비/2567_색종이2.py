# '''
# 가로 세로 크기 100 정사각형
# 가로 세로 크기 10인 정사각형 색종이 여러장 붙인 후
# 색종이가 붙은 검은 영역의 둘레의 길이를 구하는 프로그램
# 색종이가 놓이는 순서대로 테두리에 수를 메기고
# 그다음 색종이가 놓일때 각 테두리 안에 자기 순서외의 숫자는 모두 0으로 바꿈!
# 근데 겹친 부분도 없애야 되므로 순서를 바꿔서도 check함수를 돌림
# '''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint

#
# #자기 테두리 영역 안에 0이아닌 다른수가 있는지 확인하는 함수
# def check(X,Y,order):
#     for i in range(Y,Y+10):
#         for j in range(X,X+10):
#             if paper[i][j] != 0 and paper[i][j] != order:
#                 paper[i][j] = 0
#
#     return
#
# #색종이 수
# N = int(input())
# #흰도화지
# paper = [[0 for j in range(100)] for i in range(100)]
# arr= []
# #0이 아닌 수 세기
# ans = 0
# cnt = 0 #맞닿은면의 개수 세기
# temp = []
# #색종이 위치
# #색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리 , 색종이의 아래쪽 변과 아래쪽 도화지의 아래쪽 변 사이의 거리
# for n in range(1,N+1):
#     #x(열),y(행)
#     x, y = map(int,input().split())
#     arr.append((x,y))
#     # print(x,y,n)
#     #색종이를 종이에 올림
#     for i in range(y,y+10):
#         for j in range(x,x+10):
#             #테두리에만 각 순서를 메김!
#             if i == y or i == y+9:
#                 if paper[i][j]:
#                     cnt+= 1
#                     temp.append((i,j))
#                 paper[i][j] = n
#
#             else:
#                 if j == x or j == x+9:
#                     if paper[i][j]:
#                         cnt+= 1
#                         temp.append((i,j))
#                     paper[i][j] = n
#     #자기 테두리 안에 자기 순서 외의 다른 수가 있다면 숫자를 0으로 바꿈
#     check(x,y,n)
# # print(paper)
# print(cnt)
# print(temp)
# # 자기 테두리 안에 자기 순서 외의 다른 수가 있다면 숫자를 0으로 바꿈->순서를 반대로 해서 다른 영역안에 있는 테두리를 다 지움!
# # 여기서 문제가 생김! 겹치는 부분의 꼭지점이 세어지지 않는다...이걸 어떻게 해결하지?
# for i in range(len(arr)-1,-1,-1):
#     check(arr[i][0],arr[i][1],i+1)
#     # print(i+1)
#
# #또 문제가 있다 -> 겹치는 부분이 같이 사라지는 문제! -> 어떻게 해결하지..ㅠ
#
# for i in range(100):
#     for j in range(100):
#         if paper[i][j] != 0:
#             print('둘레',i,j,ans)
#             ans += 1
# print(ans)
#
# for i in range(26)[::-1]:
#     for j in range(26):
#         print(paper[i][j],end=' ')
#     print()


#다시풀기 -> 방문, 델타 이용
'''
색종이가 놓이는 자리를 전부 True로 바꿈
델타 이용해서 True에서 이동한 위치가 False면 그 값을 세어주기!
만약 넘어간 곳이 범위 밖이라면 그래도 세어주기!
범위밖을 벗어나는 색종이는 없기 때문에 현재 위치가 끝이라 둘레를 세어줘야됨!
'''

#색종이 둘레 구하기
#델타
di = [0,0,1,-1] #우좌하상
dj = [1,-1,0,0]
def check(i,j):
    global width
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        #범위를 벗어난다면 테두리니까 +1해줌
        if ni < 0 or ni > 99 or nj < 0 or nj > 99:
            width += 1
            #벗어났으니 다음 for문으로 넘어감
            continue
        #다음 위치가 False라면 cnt를 해줌
        if paper[ni][nj] == False:
            width += 1


#색종이 수
N = int(input())
#색종이를 받을 배열
paper = [[False for j in range(100)] for i in range(100)]

#색종이 입력받음
for n in range(N):
    #x열, y행
    x,y = map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            paper[i][j] = True
width = 0 #둘레
for i in range(100):
    for j in range(100):
        #True이면 델타를 돌림
        if paper[i][j]:
            check(i,j)
for i in range(26)[::-1]:
    for j in range(26):
        print(paper[i][j],end=' ')
    print()

print(width)