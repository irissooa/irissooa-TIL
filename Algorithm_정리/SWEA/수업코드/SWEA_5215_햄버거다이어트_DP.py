#훗날 dp 기법 중 0/1 knapsack을 공부한 뒤 확인하기

for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    # 0/1 knapsack 인덱스 맞추려고 한칸씩 채우기
    score, calorie = [0] * (N + 1), [0] * (N + 1)
    for i in range(1, N + 1):
        s, c = map(int, input().split())
        score[i] = s
        calorie[i] = c

    #따로 설명을 하지 않았기 때문에
    #그림을 그려서 확인을 해보시기 바랍니다.
    dp = [[0] * (L + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, L + 1):
            if j < calorie[i]:
                # 현재 사용하려는 재료의 칼로리보다 j가 작다면 위의 값을 가져온다.
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - calorie[i]] + score[i])
    print('#{} {}'.format(tc, dp[N][L]))
