import sys
sys.stdin = open('input.txt','r')

#가로 세로 크기가 각각 100인 정사각형 도화지
#가로, 세로 크기 각각 10인 정사각형
#여러장 색종이 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하기

#색종이 수 입력
#색종이 왼쪽 하단 점의 x값, y값 입력

T = int(input())
arr = [[0]*100 for _ in range(100)] #흰도화지

for tc in range(1,T+1):
    x, y = map(int,input().split())
    result = x




# months = list(range(1,13))
# DAYs = [31,28,31,30,31,30,31,31,30,31,30,31]
# T = int(input())
# for tc in range(1,T+1):
#     ymd = input()
#     YEAR,Month,Day = ymd[0:4],ymd[4:6],ymd[6:8]
#     if int(Month) in months and int(Day) <= DAYs[int(Month)-1]:
#         result = YEAR +'/' + Month + '/' + Day
#         print('#{} {}'.format(tc,result))
#     else:
#         print('#{} {}'.format(tc,-1))

# months = list(range(1,13))
# days = [31,28,31,30,31,30,31,31,30,31,30,31]
# for t in range(1,int(input())+1):
#     ymd = input()
#     y,m,d = ymd[0:4],ymd[4:6],ymd[6:8]
#     if int(d)<=days[int(m)-1] and int(m) in months:
#         print(f'#{t} {y}/{m}/{d}')
#     else:
#         print(f'#{t} -1')