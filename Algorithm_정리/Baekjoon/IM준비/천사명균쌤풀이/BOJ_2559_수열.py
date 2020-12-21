N, K = map(int, input().split())
# 온도 입력
temperature = list(map(int, input().split()))
# 초기 값
ans = sum(temperature[:K])
day = ans
for i in range(K, N):
    day += temperature[i]
    day -= temperature[i-K]
    if ans < day:
        ans = day

print(ans)
