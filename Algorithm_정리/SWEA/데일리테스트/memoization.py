N = int(input())
#내가 구하고 싶은 N까지 메모를 선언
memo = [-1] * (N+1)
#초기 2개의 값은 미리 초기화
memo[0] = 0
memo[1] = 1

def fibo(N):
    #-1이라는 말은 아직 값이 구해지지 않음이란 뜻,fibo를 구해서 저장시킴
    if memo[N] == -1:
        memo[N] = fibo(N-1) + fibo(N-2)
    #위에걸리지 않으면 구한 값을 바로 리턴
    return memo[N]

print(fibo(N))
