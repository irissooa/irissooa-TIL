def cook(idx):
    global ans
    if idx >= N:
        sum_calorie = 0
        sum_score = 0
        # 해당 햄버거 확인
        for i in range(N):
            if sel[i]:
                sum_score += score[i]
                sum_calorie += calorie[i]
        if sum_calorie <= L:
            ans = max(ans, sum_score)
        return

    # 재료 뽑고 가기
    sel[idx] = True
    cook(idx + 1)

    # 재료 안뽑고 가기
    sel[idx] = False
    cook(idx + 1)


for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split())  # 재료수, 제한칼로리
    score, calorie = [], []

    # 각각의 리스트에 담아놓기
    for _ in range(N):
        s, c = map(int, input().split())
        score.append(s)
        calorie.append(c)

    # 최고의 맛 점수
    ans = 0
    # 해당 재료를 사용했는지 안했는지 체크하기 위한 리스트
    sel = [False] * N
    cook(0)

    print("#{} {}".format(tc, ans))
