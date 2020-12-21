'''
서점에는 높이가 B인 선반이 하나 있음
N명의 점원들, 각 점원의 키 Hi로 나타냄, 탑을 쌓아서 선반 위의 물건을 사용하기로 함
점원들이 쌓는 탑은 점원 1명 이상으로 이루어짐
탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명이상이면 그 탑을 만든 모든 점원의 키의 합과 같음
탑의 높이가 B이상, 선반 위의 물건을 사용하는데 탑의 높이가 높을수록 위험
높이가 B이상인 탑중에서 높이가 가장 낮은 탑은?

부분집합..이용..해서 sum이 B이상인 것 중 가장 작은 값!

'''
import sys
sys.stdin = open('input.txt','r')

def powerset(idx,sum_num):
    global MIN
    #이미 값이 MIN보다 크면 끝냄
    if sum_num > MIN:
        # print(sum_num)
        return
    if idx == N:
        total = 0
        for i in range(N):
            if ans[i]: #값이 존재할때
                total += height[i]
        # print(total)
        if total >= B:
            # print(total)
            if MIN > total:
                MIN = total
        return


    #k번째 선택
    ans[idx] = 1
    powerset(idx+1,sum_num)
    #k번째 비선택
    ans[idx] = 0
    powerset(idx+1,sum_num)

T = int(input())
for tc in range(1,T+1):
    #점원, 높이
    N,B = map(int,input().split())
    height = list(map(int,input().split()))
    #점원들 키의 합
    S = sum(height)
    ans = [0]*N
    MIN = S
    sum_num = 0
    # print(S)
    powerset(0,0)


    print('#{} {}'.format(tc,MIN-B))