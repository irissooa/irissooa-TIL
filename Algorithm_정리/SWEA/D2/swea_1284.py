# A,B 두 수도 회사 중 수도요금 적게 부담해도 되는 회사를 고르자
# A사는 1L당 P원
#B사는 R리터까지는 Q원, 이후부터는 1L당 S원
#한달간 사용하는 수도의 양이 WL
#P,Q,R,S,W를 입력받는다
#A는 W*P원
#B는 W가 R이하면 Q원 이상이면 (W-R)*S를 해줌

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    P,Q,R,S,W = map(int,input().split())
    A = P*W
    money = 0
    if W <= R :
        B = Q
    else:
        B = Q + (W-R)*S
    if A > B:
        money = B
    else:
        money = A
    print(f'#{tc} {money}')

#병훈
for t in range(1,int(input())+1):
    P,Q,R,S,W = map(int,input().split())
    A = P*W
    B = Q if W<=R else Q+(W-R)*S
    ans = A if A<B else B
    print(f'#{t} {ans}')

#의수
'''
P : A사의 1L당 요금
Q : B사의 기준점 이하 요금(기준요금)
R : B사의 기준점
S : B사의 기준점 이상 요금(L당요금)
W : 삼성전자 사원 종민이의 수도 사용량(L)
'''

T = int(input())
for tc in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    # A사의 수도요금 계산
    fee_a = P * W

    # B사의 수도요금 계산
    if W >= R:  # 기준점 이상일때 요금
        fee_b = Q + ((W - R) * S)

    else:  # 기준점 이하일때 요금
        fee_b = Q

        # python 시험준비하면서 배운 한줄작성을 써보자
    print(f'#{tc} {fee_b}') if fee_a >= fee_b else print(f'#{tc} {fee_a}')
