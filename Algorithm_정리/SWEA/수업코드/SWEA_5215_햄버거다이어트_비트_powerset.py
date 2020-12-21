for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split()) #재료수, 제한칼로리
    score, calorie = [], []

    #각각의 리스트에 담아놓기
    for _ in range(N):
        s, c = map(int, input().split())
        score.append(s)
        calorie.append(c)

    #최고의 맛 점수
    ans = 0
    #비트연산을 이용한 powerset
    #N개의 재료를 가지고 만들 수 있는 햄버거의 종류 2^N가지
    for i in range(1 << N):
        sum_score = 0
        sum_calorie = 0
        #재료검사
        for j in range(N):
            if i & (1 << j):
                sum_score += score[j]
                sum_calorie += calorie[j]
        #제한 칼로리가 넘지않으면
        if sum_calorie <= L:
            #현재 가지고 있는 값과 이번에 구한 값 비교후 더큰값으로
            ans = max(ans, sum_score)

    print("#{} {}".format(tc, ans))