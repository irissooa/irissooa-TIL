'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

#1. [s(시작일자),s+days-1(종료일자).money] 이렇게 입력받아 list에 담는다.
#2. 종료일자를 기준으로 정렬한다.
#3. 다음 상담의 시작일자는 종료일자보다 커야 가능! 그리고 종료일자가 N을 넘기면 안됨!
근데 이러면 시작일자가 더 크지만 돈을 더주는 상담이 있어서 실패.///

돈을 기준으로 나열하고 전부 돌아보면 안되려나..? 방문처리하고 처음 선택을 계속 달리하고 전체를 보면서 고를 수 있는 경우의 수 전부 구하기
'''

import sys
sys.stdin = open('input.txt','r')
N = int(input())
info = []
for s in range(1,N+1):
    days, money = map(int,input().split())
    info.append([s,s+days-1,money])
# info.sort(key= lambda x:(x[1],-x[2]))
# print(info)
# start,end,money = info[0]
# total = money
# for i in range(1,N):
#     if info[i][0] > end and info[i][1] <= N:
#         start,end,money = info[i]
#         total += money
# print(total)
info.sort(key= lambda x:(-x[2],x[1]))
MAX = 0
for i in range(N):
    visited = [1]+[0 for _ in range(N)]
    start,end,money = info[i]
    if end > N:
        continue
    for s in range(start,end+1):
        # print(s,visited)
        visited[s] = 1
    idx = 0
    SUM = money
    # print(i,SUM)
    while idx < N:
        if sum(visited[start:end+1]) == 0 and end <= N+1:
            # print('??')
            SUM += money
            # print(SUM)
            #방문표시
            for s in range(start,end+1):
                if end <= N:
                    visited[s] = 1
        idx+=1
        if idx >= N:
            break
        # print(idx)
        start,end,money = info[idx]
    if SUM > MAX:
        MAX = SUM

print(MAX)

