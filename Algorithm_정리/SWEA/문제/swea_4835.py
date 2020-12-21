T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    ajs = list(map(int,input().split())) #list 만듦
    sums = []
    
    for idx in range(N-M+1): #ajs idx를 돌림
        sum_n = 0
        for i in range(idx, idx+M) : #해당 idx부터 M번째까지 더함
            sum_n += ajs[i]
        sums.append(sum_n)
    max_n = sums[0]
    min_n = sums[0]
    for s in sums:
        if max_n < s:
            max_n = s
        elif min_n > s:
            min_n = s
    print(f'#{tc} {max_n-min_n}')

#누적합으로 구하기
#구간합
# lengh = int(input())
# for l in range(1,lengh+1):
#     N,M = list(map(int,input().split()))
#     numbers = list(map(int,input().split()))
#     #누적합구하기
#     sum_num = [0]*(N+1)
#     for i in range(1,N+1):
#         sum_num[i] = numbers[i-1] + sum_num[i-1]
#     #M번째를 최댓값과 최솟값으로 설정
#     min_num = max_num = sum_num[M]
#     #반복문을 돌면서 최솟값과 최댓값 찾기
#     for i in range(M,N+1):
#         min_num = min(min_num, sum_num[i]-sum_num[i-M])
#         max_num = max(max_num,sum_num[i]-sum_num[i-M])
#     #결과출력
#     print(f'#{l} {max_num-min_num}')