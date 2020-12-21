#1부터 N까지 숫자에서 홀수는더하고 짝수는 뺏을 때 최종 누적된 값 구하기
#1부터N까지 for문을 돌리면서
#한 빈리스트에 수들을 넣는데
#n값이 홀수는 -를 붙이고 전체 합을 구해보자

for tc in range(1,int(input())+1):
    arr = []
    for n in range(1,int(input())+1):
        if n % 2 == 0: #짝수일때 빼자, 앞에 -를 붙이자
           arr.append(-n)
        else:
            arr.append(n)
    print(f'#{tc} {sum(arr)}')

#의수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sum1 = 0
    for x in range(1, N+1):
        if x % 2 == 1:
            sum1 += x
        else:
            sum1 -= x
    print(f'#{tc} {sum1}')