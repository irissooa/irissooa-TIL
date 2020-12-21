'''
모르겠어서 보고 풀었다ㅠㅠㅠ
#1. n개의 원판이 있을 때, n-1개의 원판 즉, 맨 밑의 원판을 제외하고 나머지 원판을 1->2번으로 옮긴뒤
맨 밑의 원판을 1번에서 3번으로 옮김
#2. n-1개의 원판들을 다시 2번에서 3번으로 옮김

이해는 하겠는데...넘 어렵....ㅠㅠㅠㅠㅠㅠ다시짤수있을까아아ㅏ...헣....
'''
def move(n,one,two,three):
    #종료 n이 1이되면 맨 밑의 원판을 1번에서 3번으로 옮기니 one,three출력
    if n == 1:
        # print(n,'11',one,three,two)
        print(one,three)
    else:
        #n-1(맨밑원판 제외)의 원판을 1번에서 2번으로 옮김
        move(n-1,one,three,two)
        print(one,three)
        # print(n,'22',one,three,two)
        move(n-1,two,one,three)

N = int(input())
one = [i for i in range(1,N+1)[::-1]]
SUM = 1
for i in range(N-1):
    SUM = SUM*2 + 1
print(SUM)
move(N,1,2,3)
