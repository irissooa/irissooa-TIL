'''
M개 반복문을 돌면서
M의 수보다 작지만 가장 큰수를 뽑아야됨
가져갈수있는 N이 없으면 0 출력
'''
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    #컨테이너수, 트럭수
    N,M = map(int,input().split())
    #N개 화물무게
    weight = list(map(int,input().split()))
    #M개의 적재용량
    volumn = list(map(int,input().split()))
    # print('w',weight)
    # print('v',volumn)
    result = []
    for i in range(M):
        MAX = 0
        for j in range(len(weight)):
            if volumn[i] >= weight[j]:
                if MAX < weight[j]:
                    MAX = weight[j]
        if MAX:
            result.append(MAX)
            weight.pop(weight.index(MAX))
    # print(result)
    print('#{} {}'.format(tc,sum(result)))