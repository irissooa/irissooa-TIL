#Aj의 개수인 N개와 Bj의 개수인 M개를 입력받고
#Aj의 idx와 Bj의 idx에서 idx수가 작은것이 큰 idx범위 안에서
#마주보는 곱하고 모두 더한 값이 최대인 것 구하기

for tc in range(1,int(input())+1):
    N, M = map(int, input().split())
    Aj = list(map(int,input().split()))
    Bj = list(map(int,input().split()))
    MAX = []
    if N >= M:
        for i in range(N-M+1):  #큰 범위의 idx에 안 벗어나기 위해
            SUM = 0
            for j in range(M):
                SUM += Aj[i+j]*Bj[j]
            MAX.append(SUM)
    else: #M이 더 크면
        for i in range(M-N+1):  # 큰 범위의 idx에 안 벗어나기 위해
            SUM = 0
            for j in range(N):
                SUM += Aj[j] * Bj[i+j]
            MAX.append(SUM)
    print(f'#{tc} {max(MAX)}')

#병훈
for t in range(1, int(input())+1):
    N,M = map(int,input().split())
    shorter = list(map(int, input().split()))
    longer = list(map(int, input().split()))
    if N>M: #짧다고 설정한게 더 길면 두개 위치를 바꿔라
        N, M = M, N
        shorter,longer =longer, shorter
    MAX = 0
    for k in range(M-N+1):
        multi = 0
        for i in range(N):
            multi+=shorter[i]*longer[k+i]
        if MAX < multi: #MAX함수 안쓰고 알고리즘으로!
            MAX = multi
    print(f'#{t} {MAX}')