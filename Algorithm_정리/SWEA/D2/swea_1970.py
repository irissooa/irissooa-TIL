#거스름돈을 입력받고 거스름돈을 최소한의 개수로 줄 수 있는 방법
#단순하게..생각하면
#5만원, 만원, 5천, 천, 오백, 백, 오십, 십원 이렇게 범위를 정하고 그 사이면 그 값과 나눈몫 만큼 더해주고, 그 값만큼 빼면..되지않을까
#문자열에 그 개수만큼 공백과 함꼐 추가함

import sys
sys.stdin = open("input.txt", "r")



for tc in range(1,int(input())+1):
    N = int(input())
    str_remain = []
    cnt = 0
    if N >=50000:
        cnt = N // 50000
        N -= cnt * 50000
        str_remain.append(cnt)
    else :
        str_remain.append(0)
    if N >= 10000:
        cnt = N // 10000
        N -= cnt * 10000
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N >= 5000:
        cnt = N // 5000
        N -= cnt * 5000
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N>= 1000:
        cnt = N // 1000
        N -= cnt * 1000
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N >= 500:
        cnt = N // 500
        N -= cnt * 500
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N >= 100:
        cnt = N // 100
        N -= cnt * 100
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N >= 50:
        cnt = N // 50
        N -= cnt * 50
        str_remain.append(cnt)
    else:
        str_remain.append(0)
    if N >= 10 : #10원
        cnt = N // 10
        N -= cnt * 10
        str_remain.append(cnt)
    else:
        str_remain.append(0)

    print(f'#{tc}')
    STR = ''
    for s in str_remain:
        # STR += str(s)
        print(f'{str(s)}',end = ' ')
    print()

#내코드 줄이기
#거스름돈 리스트를 만든다
#리스트를 돌면서 입력된 N을 money에 나눈 몫을 세어주고 그 cnt를 어딘가에 저장함
#그리고 N을 그 나누어진 만큼 빼줌

money = [50000,10000,5000,1000,500,100,50,10]
for tc in range(1,int(input())+1):
    N = int(input())
    remain = ''
    for m in money:
        cnt = N//m #money하나씩 돌면서 몫이 그 거스름돈 개수이다
        remain += str(cnt) + ' ' #그 거스름돈 개수를 str에 공백과 함께 저장해줘라
        N -= cnt * m #N값을 다시 재설정 해줘라
    print(f'#{tc}\n{remain}')
#병훈 이렇게 줄여보쟈....
bills = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for t in range(1, int(input()) + 1):
    N = int(input())
    cnts = ''
    for bill in bills:
        cnt = N // bill
        N -= bill * cnt
        cnts += str(cnt) + ' '

    print(f'#{t}\n{cnts}')