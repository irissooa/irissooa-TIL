def cook(idx, sum_score, sum_calorie):
    global ans
    # 제한 칼로리 넘어가면 더이상 의미 없으므로 return
    if sum_calorie > L:
        return
    # 여기서 정답 갱신 가능
    if idx == N:
        if sum_score > ans:
            ans = sum_score
        return

    # 재료 뽑고가고
    cook(idx + 1, sum_score + score[idx], sum_calorie + calorie[idx])
    # 안뽑고 가고
    cook(idx + 1, sum_score, sum_calorie)


for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split())  # 재료수, 제한칼로리
    score, calorie = [], []

    # 각각의 리스트에 담아놓기
    for _ in range(N):
        s, c = map(int, input().split())
        score.append(s)
        calorie.append(c)
    ans = 0
    cook(0, 0, 0)  # 인덱스, 중간 점수, 중간 칼로리

    print("#{} {}".format(tc, ans))
