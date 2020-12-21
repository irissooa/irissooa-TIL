#파스칼삼각형은 조합으로 푼다(이현우's 아이디어)
#펙토리얼 함수를 재귀로 만든다
#nCr = n!/r!*(n-r)!
#N번만큼 for문돌리면서 그 밑의 for문도 n번만큼 돌린다

import sys
sys.stdin = open("input.txt", "r")


#팩토리얼 재귀함수 만들기
def fact(n):
    if n <= 1: #n이 1이하이면 1을 return함
        return 1
    else:
        return n*fact(n-1)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            result = fact(i)/(fact(j)*fact(i-j))
            print(f'{int(result)}',end = ' ') #같은 i의 j들은 서로 띄어쓰고
        print() #i가 달라지면 줄바꿈
    # print()#각 테스트케이스들 끼리 줄바꿈

