'''
온도가 정수의 수열로 주어짐, 연속적인 며칠 동안의 온도의 합이 가장 큰 값
매일 측정한 온도가 정수의 수열로 주어짐
연속적인 며칠 동안의 온도의 합이 가장 큰 값?
N개 중에 처음부터 K개씩 잘라서 합을 구함,
근데 그 K개의 합들 중 최대값!
'''
import sys
sys.stdin = open('input.txt','r')


#온도를 측정한 전체 날짜의 수 N, 합을 구하기 위한 연속적인 날짜의 수 K
N, K = map(int,input().split())
#매일 측정한 온도 N개
temp = list(map(int,input().split()))

#N개를 k개씩 잘라서 합을 구하는데 그것의 최댓값!
# MAX = 0#Max인 값을 넣음
#아래 for문 시간초과남....
# for i in range(0,N-K):
    # SUM = sum(temp[i:i+K])
    # print(SUM)
    # if SUM > MAX:
    #     MAX = SUM
# 질문검색 힌트 -> 다음 수의 부분합을 구할 때 이전 부분합에서 젤 첨 수 빼고, 그다음 수 더하기
SUM = sum(temp[:K])#처음 k개의 부분합
MAX = SUM #일단 처음 SUM값을 넣어둠
for i in range(K,N):
    start = temp[i-K]
    SUM = SUM - start + temp[i]
    # print(start,SUM)
    if SUM > MAX:
        MAX = SUM
print(MAX)