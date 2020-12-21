# 숫자 N을 입력받고 소수인 2,3,5,7,11 중 작은 소인수부터 차례로나누며 몫이 소수가 되면 멈춤
#나눈 소수들과 마지막 몫을 곱으로 나타냄
# 그소수들의 지수들을 출력하라

#숫자 N을 입력받고  소수 2,3,5,7,11을 리스트로 만듦
#숫자N을 리스트중 작은 소수들 순으로 나눔
#나누어떨어지지 않을 때까지 나눈 것의 수를 셈
#나누어떨어지지 않는다면 다음 수로 나눔 그렇게 개수를 세서 출력!!

import sys
sys.stdin = open("input.txt", "r")

numbers = [2,3,5,7,11]
for tc in range(1,int(input())+1):
    N = int(input())
    p_num = []
    for number in numbers:
        cnt = 0
        while True:
            if N % number == 0:
                N //= number
                cnt += 1
            else:
                break
        p_num.append(cnt)
    p_num = ' '.join(map(str,p_num))
    print(f'#{tc} {p_num}')