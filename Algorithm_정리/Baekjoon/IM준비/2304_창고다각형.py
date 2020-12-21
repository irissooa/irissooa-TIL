# '''
# 소요시간 2020/10/18/22:50
# 기둥을 순서대로 재배열하고 제일 첫기둥을 기준으로
# 다음 기둥으로 갈수록 커지면 높이, 위치 갱신하고 지붕 너비 더함
# 만약 다음 기둥이 작다면 이후 모든 기둥들을 훑어보면서 자기보다 더 높은것이 있는지 찾고 있다면 위 과정 반복
# 없다면 그다음으로 가장높은 곳을 기준으로 지붕 너비를 더함 그리고 또 반복
# '''
import sys
sys.stdin = open('input.txt','r')
#
# def check(r):
#     global roof,now,p_height
#     #다음 기둥까지의 면적
#     roof += (column[r][0]-now)*p_height
#     # print(column[r][0],now)
#     # print('H',p_height,'지붕',roof,'현위치',now)
#     #현재 기둥 높이,위치를 갱신
#     p_height = column[r][1]
#     now = column[r][0]
#     return
#
# #기둥 개수
# N = int(input())
# # 위치,높이 담을 list
# column = []
# MAX = 0#최대 높이
# for n in range(N):
#     #왼쪽 면의 위치 L, 높이 H
#     column.append(list(map(int,input().split())))
#     if column[n][1] > MAX:
#         MAX = column[n][1]
# #위치별로 다시 정렬
# column = sorted(column)
# # print(column)
# # 처음 지붕 높이는 제일 처음 기둥의 높이로 설정
# p_height = column[0][1]#유지될 높이
# now = column[0][0]#위치
# roof = 0 #초기 지붕면적
# for r in range(1,len(column)):
#     # print('현위치',now,'H',p_height,'지붕',roof)
#     #다음 기둥이 현재 높이보다 높으면
#     if column[r][1] > p_height:
#         # print(p_height,'왜10아님?')
#         # roof += column[r][1]
#         check(r)
#         continue
#     #다음 기둥이 현재기둥보다 낮다면 남은 기둥높이들 중 제일 높은것을 현재 높이로 함
#     else:
#         if p_height == MAX:
#             roof+=p_height
#         for nr in range(r,len(column)):
#             #남은것들 중 현재 높이보다 높다면
#             second = [0,0]#아니라면 그다음으로 높은것 넣을 변수
#             if column[nr][1] > p_height:
#                 check(nr)
#                 # print(p_height)
#                 #찾았으니 이 for문을 나와야됨
#                 break
#             else:
#                 if column[nr][1] > second[1]:
#                     second = column[nr]
#
#         #현재 높이보다 높은 것이 없으면 그다음으로 높은 것을 찾아야됨!
#         else:
#             # print(second,p_height,'왜여기..?')
#             p_height=second[1]
#             # print(second[0]-now-1)
#             roof += (second[0]-now)*p_height
#             now = second[0]
#             # print('현위치',now,'H',p_height,'지붕',roof)
#         #종료조건, 현재위치가 가장 마지막 위치라면 끝
#         if now == column[len(column)-1][0]:
#             break
#
#
# print(roof)
#

#오른쪽 왼쪽에서 부터 제일 높은곳으로 높이 갱신하면서 오기기
# #기둥 개수
N = int(input())
# 위치,높이 담을 list
column = []
MAX = [0,0]#최대 높이 위치,높이
for n in range(N):
    #왼쪽 면의 위치 L, 높이 H
    column.append(list(map(int,input().split())))
    if column[n][1] > MAX[1]:
        MAX = column[n]
#위치별로 다시 정렬
column = sorted(column)
# print(column)
MAX_idx = column.index(MAX)
# print(MAX,MAX_idx)
l_height = [0,0]
r_height = [0,0]
roof=0
#왼쪽에서부터 높이 갱신하며 너비 구하기
for l in range(MAX_idx+1):
    #작은건 어차피 MAX_idx까지 갈거기 때문에 넘어감
    if column[l][1] >= l_height[1]:
        l_height = column[l]
        # print('lh',l_height[1])
        # print('l',roof)
    roof += l_height[1]
#오른쪽에서부터 높이 갱신하며 너비 구하기
for r in range(column[len(column)-1][0],MAX_idx,-1):
    if column[r][1] >= r_height[1]:
        # print('확인',r,column[r][1])
        r_height = column[r]
        # print('rh',r_height[1])
        # print('r',roof)
    roof += r_height[1]

print(roof)

#하..코드봄..ㅠ
# N = int(input())
# arr = []
# height = [0]*1001
# for n in range(N):
#     L,H = map(int,input().split())
#     arr.append(L)
#     height[L] = H
# # print(height)
# start = min(arr)
# end = max(arr)
# # print(start,end)
# l_MAX = 0
# roof = 0
# # 왼쪽에서 최댓값을 계속 갱신하면서 제일높은 높이일때 쭉 끝까지 다 더함
# for l in range(start,end+1):
#     if height[l] > l_MAX:
#         l_MAX = height[l]
#     roof += l_MAX
# # print(l_MAX)
# r_MAX = 0
# minusroof = 0
# # 오른쪽에서 최댓값을 갱신하면서 오는데 l_MAX에서 r_MAX를 빼준값을 쭉 더해서 나중에 roof에서 뺀다!(불필요한 너비 제거)
# for r in range(end,start,-1):
#     if height[r] > r_MAX:
#         r_MAX = height[r]
#         #최댓값이 같을때까지만 반복문 돈다
#         if r_MAX == l_MAX:
#             break
#     minusroof += (l_MAX-r_MAX)
# print(roof-minusroof)
