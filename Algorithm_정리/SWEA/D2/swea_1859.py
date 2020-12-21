#연속된 N일 동안의 물건의 매매가를 예측하여 알고 있음
#당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입 가능
#판매는 얼마든지 가능

import sys
sys.stdin = open("input.txt", "r")

#구매는 무조건 1만
#판매는 언제든 가능
#먼저 N일을 받고 하루하루 물건의 매매가를 받는다
#구매는 매매가의 *1, 판매는 매매가*모든구매개수 이익은 판매-구매
#만약 구매를 안하는 것이 낫다면 0을 출력

#정답자들 tip -> 뒤에서 부터 풀어라! WHY??
#고점보다 낮게 사서 고점에 파는게 이익
#제일 끝값을 고점 초기값으로 둬라
#내가 찾은 고점보다 크거나 같으면? 새로운 고점 갱신
#내가 찾은 고점보다 작다면? 이익, 해당 지점에서 사서 고점에 팔자

#문제 잘못이해! 판매는 언제든, 몇개든 할 수 있다.
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split()))
    MAX = price[-1] #현재 고점을 마지막값으로 둔다
    profit = 0 #이익(MAX-구매가)의 합
    for p in price[::-1]: #뒤에서부터 탐색
        if MAX > p: #고점보다 작은곳에서 1개씩 삼
            profit += MAX - p #이익들의 합을 구함
        else:
            MAX = p #MAX갱신

    print('#{} {}'.format(tc,profit))


#구글링한 해설..
# T = int(input())
# for i in range(T):
#     N = int(input())
#     mylist = list(map(int,input().split(' ')))[::-1] #뒤에서부터 탐색
#     answer = 0
#     now_max = mylist[0] #현재 가장 큰 값
#
#     for j in range(1,N):
#         if now_max > mylist[j]:
#             answer += now_max - mylist[j]
#         else:
#             now_max = mylist[j]
#     print('#{} {}'.format(i+1,answer))

#훈코드
# for t in range(1, int(input()) + 1):
#     profit = 0
#     N = int(input())
#     prices = list(map(int, input().split()))
#     pivot = prices[-1]
#     for i in range(N-2,-1,-1):
#         if pivot < prices[i]:
#             pivot = prices[i]
#         else:
#             profit += pivot - prices[i]
#     print(f'#{t} {profit}')