'''
처음에는 완전탐색으로 풀었는데 시간초과가 남
찾아보니까 '투포인터 알고리즘'을 이용함!
'''
import sys
sys.stdin = open('input.txt','r')
#수열의 개수N, 찾고자하는 부분합M
N,M= map(int,input().split())
#수열리스트
nums = list(map(int,input().split()))
#투포인터 알고리즘으로 구현
#더할떄 처음값을 뺴주고 다음값을 더해주면 시간을 적게 들이고 그 구간의 합을 구할 수 있다!
#중간 합을 넣을 변수
interval_sum = 0
cnt = 0 #찾고자하는 부분합의 개수를 담을 변수
#끝점
end = 0

#시작점
for start in range(N):
    #중간합이 M을 넘어가면 안됨, 그리고 end가 N을 넘으면 안됨
    while interval_sum < M and end < N:
        #interval_sum에 끝값을 더해줌
        interval_sum += nums[end]
        #end를 늘려감
        end+=1
    #만약에 그 부분합이 M과 같다면 cnt+1해주고 첫값을 뺴줌
    if interval_sum == M:
        cnt+=1
    interval_sum -= nums[start]
print(cnt)




















# # print(nums)
# cnt = 0
# interval_sum=0
# end = 0
# #start를 차례대로 증가시키며 반복
# for start in range(N):
#     #end를 가능한만큼 이동시키기
#     while interval_sum < M and end < N:
#         interval_sum += nums[end]
#         end += 1
#     #부분집합 M일때 카운트 증가
#     if interval_sum == M:
#         cnt+=1
#     #end가 멀어질때 제일 앞의 수를 뺴면서 합을 구함
#     interval_sum -= nums[start]
# print(cnt)
#
# #처음에 풀었던 완전탐색...시간초과
# # for i in range(N):
# #     total = 0
# #     for j in range(i,N):
# #         # print(j)
# #         total += nums[j]
# #         if total == M:
# #             cnt+=1
# #             break
# # print(cnt)