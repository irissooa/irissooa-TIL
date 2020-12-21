import sys
sys.stdin = open("input.txt", "r")
#날짜계산
#월 일 월 일을 입력받고, 첫번째 날짜와 두번째 날짜의 차이를 구하라
#월일을 숫자로 바꿔라! 그러고 두개 빼고 1더하기...노가다밖에 생각안남...큰일ㅠ

Days = [31,28,31,30,31,30,31,31,30,31,30,31] #날짜들 나중에 (월-1)idx로 찾기

for tc in range(1,int(input())+1):
    M1, D1, M2, D2 = map(int,input().split())
    SUM1 = 0
    SUM2 = 0
    result = 0
    #M1+D1 구하기
    for i in range(M1-1): #해당 월은 날짜를 더하지 않고 D1를 더함
        SUM1 += Days[i] #해당 월 전까지 일 다 더하기
    SUM1 += D1 #M1전까지 모두 더한 것 + D1

    #M2+D2 구하기
    for i in range(M2-1):
        SUM2 += Days[i]
    SUM2 += D2

    #두 일의 차 구하기
    result = SUM2 - SUM1 +1 # 해당날도 더하기
    print(f'#{tc} {result}')

#병훈 와...이래풀면 되는구낭...
days = [31,28,31,30,31,30,31,31,30,31,30,31]
for t in range(1, int(input())+1):
    m1,d1,m2,d2 = map(int,input().split())
    print(f'#{t} {sum(days[m1-1:m2-1])-d1+d2+1}')