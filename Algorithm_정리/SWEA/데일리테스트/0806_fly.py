#N*N 2차 배열을 만든다
#그 안의 숫자는 파리의 개수
#M*M 배열은 for문으로 N*N 안을 돌면서 그안에 들어있는 값들의 합을 구함
#M배열의 총 합이 가장 큰 값 구하라
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flies =[]
    #N*N배열에 값을 넣어 만듦
    for n in range(N): #N번 반복할거야
        fly = list(map(int,input().split()))
        flies.append(fly)

    #M*M배열을 구하기
    #시작점을 for문으로 만든다
    #주의! idx값(N)d을 넘어가지 않게 만듦
    MAX = 0
    #시작점(j이 가로, i가 세로) ****제발 적을때 세로부터!
    for i in range(N-M+1): #N-M한 것을 포함해야되니까 +1
        for j in range(N-M+1):
            SUM = 0 #M안의 합
            # N안에 반복될 M값들
            for m in range(i,i+M):
                for n in range(j,j+M):
                    SUM += flies[m][n]
            if MAX < SUM:
                MAX = SUM
    print(f'#{tc} {MAX}')


#병훈
def M(arr,n,m):
    MAX = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            flies = 0
            for k in range(m):
                flies += sum(arr[i+k][j:j+m]) ##이코드 대박...
            if MAX < flies:
                MAX = flies
    return MAX
for t in range(1,input()+1):
    n,m = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    print(f'#{t} {M(arr,n,m)}')