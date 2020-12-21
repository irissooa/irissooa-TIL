'''
2020-12-03 15:20 -16:30
두명의 손님에게 음식 제공
최대한 비슷한 맛의 음식 만들어야됨
N개의 식재료, 식재료 각각 N//2로 나누어 두개의 요리 만듦 A,B
A,B의 차이가 최소가 되도록 재료를 배분!
각 음식의 맛은 Sij(식재료i,j)의 합
A,B차 최솟값 구하기

N//2개로 재료를 뽑고 합구함(A), 안뽑힌 것 합구함(B) -> 2중for문
두개의 차 최소 갱신
'''
import sys
sys.stdin = open('input.txt','r')

#각 값들의 합 구하기
def calc(select,opsselect):
    global MIN
    SUM,OSUM = 0,0
    for i in range(N//2):
        for j in range(i+1,N//2):
            pi,pj = select[i],select[j]
            SUM += food[pi][pj] + food[pj][pi]
            oi,oj = opsselect[i],opsselect[j]
            OSUM += food[oi][oj] + food[oj][oi]

    if MIN > abs(SUM-OSUM):
        MIN = abs(SUM-OSUM)
    return


def choose(idx,sidx):
    if sidx == N//2:
        opssel = []
        for i in range(N):
            if i not in sel:
                opssel.append(i)
        # print('결과',sel,opssel)
        calc(sel,opssel)
        return
    if idx == N:
        return
    sel[sidx] = idx
    choose(idx+1,sidx+1)
    sel[sidx] = 0
    choose(idx+1,sidx)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    food = [list(map(int,input().split())) for _ in range(N)]
    sel=[0]*(N//2)
    MIN = 987654321
    choose(0,0)
    print('#{} {}'.format(tc,MIN))